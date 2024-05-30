#!/bin/python

import os
import subprocess
import urllib.request
import zipfile
import platform
import argparse

def check_root():
    if os.geteuid() != 0:
        print("This script requires elevated permissions. Please run it with sudo.")
        exit()

# Function to check if a command exists
def command_exists(command):
    try:
        subprocess.run([command], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        return False

# Function to install required software
def install_software():
    print("Installing required software...")
    
    if platform.system() == "Windows":
        # Check and install JDK
        if not command_exists("java -version"):
            print("JDK is not installed. Please install JDK manually.")
            if not command_exists("mvn -version"):
                print("Maven is also not installed. Please install Maven manually.")
            exit()
        else:
            print("JDK is already installed.")
        
        # Check and install Maven
        if not command_exists("mvn -version"):
            print("Maven is not installed. Please install Maven manually.")
            exit()
        else:
            print("Maven is already installed.")
        
        # Check and install GlassFish
        if not command_exists("asadmin version"):
            print("GlassFish is not installed. Downloading and installing...")
            url = "https://download.eclipse.org/ee4j/glassfish/glassfish-6.1.0.zip"
            urllib.request.urlretrieve(url, "glassfish-6.1.0.zip")
            with zipfile.ZipFile("glassfish-6.1.0.zip", "r") as zip_ref:
                zip_ref.extractall("C:\\glassfish")
            os.environ["PATH"] += ";C:\\glassfish\\glassfish6\\glassfish\\bin"
        else:
            print("GlassFish is already installed.")
    else:
        # Unix-based installation
        if not command_exists("java -version"):
            print("JDK is not installed. Installing...")
            subprocess.run(["sudo", "apt-get", "update"], check=True)
            subprocess.run(["sudo", "apt-get", "install", "-y", "openjdk-11-jdk"], check=True)
            os.environ["PATH"] += f":/usr/bin/java"
        else:
            print("JDK is already installed.")
        
        if not command_exists("mvn -version"):
            print("Maven is not installed. Installing...")
            subprocess.run(["sudo", "apt-get", "install", "-y", "maven"], check=True)
            os.environ["PATH"] += f":/usr/bin/mvn"
        else:
            print("Maven is already installed.")
        
        if not command_exists("asadmin version"):
            print("GlassFish is not installed. Installing...")
            url = "https://download.eclipse.org/ee4j/glassfish/glassfish-6.1.0.zip"
            urllib.request.urlretrieve(url, "glassfish-6.1.0.zip")
            with zipfile.ZipFile("glassfish-6.1.0.zip", "r") as zip_ref:
                zip_ref.extractall("/opt")
            os.symlink("/opt/glassfish6/glassfish", "/usr/local/bin/asadmin")
        else:
            print("GlassFish is already installed.")

# Function to create a Spring project using Maven
def create_spring_project():
    project_name = input("Enter the project name: ")
    base_package_name = input("Enter the base package name (e.g., com.example): ")

    print("Creating Spring project...")
    subprocess.run([
        "mvn", "archetype:generate",
        f"-DgroupId={base_package_name}",
        f"-DartifactId={project_name}",
        "-DarchetypeArtifactId=maven-archetype-quickstart",
        "-DinteractiveMode=false"
    ], check=True)
    
    os.chdir(project_name)
    
    # Add Spring and Jersey dependencies to pom.xml
    with open("pom.xml", "a") as pom_file:
        pom_file.write('''
<dependencies>
  <dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>5.3.9</version>
  </dependency>
  <dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-web</artifactId>
    <version>5.3.9</version>
  </dependency>
  <dependency>
    <groupId>org.glassfish.jersey.core</groupId>
    <artifactId>jersey-server</artifactId>
    <version>3.0.3</version>
  </dependency>
  <dependency>
    <groupId>org.glassfish.jersey.containers</groupId>
    <artifactId>jersey-container-servlet-core</artifactId>
    <version>3.0.3</version>
  </dependency>
  <dependency>
    <groupId>org.glassfish.jersey.inject</groupId>
    <artifactId>jersey-hk2</artifactId>
    <version>3.0.3</version>
  </dependency>
</dependencies>
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-compiler-plugin</artifactId>
      <version>3.8.1</version>
      <configuration>
        <source>11</source>
        <target>11</target>
      </configuration>
    </plugin>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-war-plugin</artifactId>
      <version>3.2.3</version>
      <configuration>
        <failOnMissingWebXml>false</failOnMissingWebXml>
      </configuration>
    </plugin>
  </plugins>
</build>
''')
    
    # Create directories for different layers
    package_dir = base_package_name.replace('.', '/')
    os.makedirs(f"src/main/java/{package_dir}/config", exist_ok=True)
    os.makedirs(f"src/main/java/{package_dir}/controller", exist_ok=True)
    os.makedirs(f"src/main/java/{package_dir}/service", exist_ok=True)
    os.makedirs(f"src/main/java/{package_dir}/repository", exist_ok=True)
    os.makedirs("src/main/webapp/WEB-INF", exist_ok=True)
    
    # Create Spring configuration class
    with open(f"src/main/java/{package_dir}/config/AppConfig.java", "w") as app_config_file:
        app_config_file.write(f'''
package {base_package_name}.config;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@ComponentScan(basePackages = "{base_package_name}")
public class AppConfig {{
}}
''')
    
    # Create Jersey configuration class
    with open(f"src/main/java/{package_dir}/config/JerseyConfig.java", "w") as jersey_config_file:
        jersey_config_file.write(f'''
package {base_package_name}.config;

import org.glassfish.jersey.server.ResourceConfig;
import org.springframework.stereotype.Component;

@Component
public class JerseyConfig extends ResourceConfig {{
  public JerseyConfig() {{
    packages("{base_package_name}.controller");
  }}
}}
''')
    
    # Create example Jersey controller
    with open(f"src/main/java/{package_dir}/controller/ExampleController.java", "w") as example_controller_file:
        example_controller_file.write(f'''
package {base_package_name}.controller;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import org.springframework.stereotype.Component;

@Component
@Path("/example")
public class ExampleController {{

  @GET
  @Produces(MediaType.TEXT_PLAIN)
  public String getExample() {{
    return "Hello, World!";
  }}
}}
''')
    
    # Create web.xml for Jersey configuration
    with open("src/main/webapp/WEB-INF/web.xml", "w") as web_xml_file:
        web_xml_file.write(f'''
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_3_1.xsd" version="3.1">
  <display-name>{project_name}</display-name>

  <servlet>
    <servlet-name>jersey-servlet</servlet-name>
    <servlet-class>org.glassfish.jersey.servlet.ServletContainer</servlet-class>
    <init-param>
      <param-name>jersey.config.server.provider.packages</param-name>
      <param-value>{base_package_name}.controller</param-value>
    </init-param>
    <load-on-startup>1</load-on-startup>
  </servlet>

  <servlet-mapping>
    <servlet-name>jersey-servlet</servlet-name>
    <url-pattern>/api/*</url-pattern>
  </servlet-mapping>

  <context-param>
    <param-name>contextConfigLocation</param-name>
    <param-value>/WEB-INF/applicationContext.xml</param-value>
  </context-param>

  <listener>
    <listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
  </listener>
</web-app>
''')
    
    # Create applicationContext.xml for Spring configuration
    with open("src/main/webapp/WEB-INF/applicationContext.xml", "w") as application_context_file:
        application_context_file.write(f'''
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
           http://www.springframework.org/schema/beans/spring-beans.xsd
           http://www.springframework.org/schema/context
           http://www.springframework.org/schema/context/spring-context.xsd">

    <context:component-scan base-package="{base_package_name}" />

</beans>
''')

# Function to configure GlassFish
def configure_glassfish(project_name):
    print("Configuring GlassFish...")
    subprocess.run(["asadmin", "start-domain"], check=True)
    subprocess.run(["asadmin", "create-domain", "--nopassword", "true", "mydomain"], check=True)
    subprocess.run(["asadmin", "create-application", "--contextroot", f"/{project_name}", "--name", project_name, f"target/{project_name}.war"], check=True)
    subprocess.run(["asadmin", "deploy", "--name", project_name, f"target/{project_name}.war"], check=True)

def main():
    parser = argparse.ArgumentParser(description="Spring Jersey Project Creator")
    parser.add_argument("command", choices=["help", "run", "check"], help="Command to execute")
    parser.add_argument("-s", "--skipInstall", help="skips the install/check phase when running \"run\"")
    args = parser.parse_args()

    if args.command == "help":
        parser.print_help()
    elif args.command == "run":
        check_root()
        if !args.skipInstall #execute install if flag is not set
            install_software()
        create_spring_project()
        configure_glassfish()
        print("Spring project setup complete.")
        print("You can build the project by running: mvn clean install")
    elif args.command == "check":
        check_root()
        install_software()
        print()
        print("All software needed to run this installer are propperly installed")

if __name__ == "__main__":
    main()

# Main script
#install_software()
#create_spring_project()
#configure_glassfish(input("Enter the project name again for GlassFish configuration: "))

#print("Spring project setup complete.")
#print("You can build the project by running: mvn clean install")