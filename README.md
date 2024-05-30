# Spring Jersey Creator

This script automates the setup and installation of a Spring and Jersey environment. It checks for the required software (JDK, Maven, and GlassFish) and installs them if they are not present on the system.

## Prerequisites

- Python 3.x
- Elevated permissions (run with sudo on Unix-based systems)
- Internet connection (for downloading required software)

## Features

- Checks for JDK, Maven, and GlassFish
- Installs JDK, Maven, and GlassFish if not already installed
- Supports both Windows and Unix-based systems

## Usage

### Basic Usage

To run the script, use the following command:

```bash
python springJerseyCreator.py
```

### Arguments

The script accepts optional arguments:

- `--skipInstall`: Skips installation step if the "run" command is executed.

Example:

```bash
python springJerseyCreator.py --force-install
```

## How It Works

1. **Check Root Permissions**:
   The script requires elevated permissions to install software. It will prompt you to run it with `sudo` if not already running with elevated permissions.

2. **Check Command Existence**:
   The script checks if `java`, `mvn`, and `asadmin` commands exist on your system.

3. **Install Software**:
   - **Windows**:
     - Checks for JDK and Maven, prompts for manual installation if not found.
     - Downloads and installs GlassFish if not already installed.
   - **Unix-based Systems**:
     - Installs JDK, Maven, and GlassFish using package managers (`apt`, `yum`, etc.)

## Platform Specifics

- **Windows**: 
  - If JDK or Maven is not installed, the script will prompt you to install them manually.
  - Downloads GlassFish from the official website and sets the PATH environment variable.

- **Unix-based Systems**: 
  - Installs required software using system package managers.
  - Sets up GlassFish environment variables.

## Troubleshooting

- **Permission Denied**: Ensure you are running the script with elevated permissions.
- **Missing Software**: Ensure you have an active internet connection for downloading required software.
- **Unsupported OS**: The script currently supports Windows and Unix-based systems only.

## License

This project is licensed under the MIT License - see the LICENSE file for details.


                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                ███                 
                                                                             ██████                 
                                                                         ██████████                 
                               ██                                    ███████ ██████                 
                              ██████                              ██████  ██████████                
                             █████████                        ███████  █  ███ ██████                
                           ███████ █████                   ██████       ████ ███  ██                
                          ███ █████   ████               ██████    █   ███  ███   ██                
                         ███████ ██ █  █████             ██████    ██ █████ ██    ██                
                        ███  ███ ████ ███ ████          █████ █    ████    ███ █████                
                       ███ █████ ████████  ███         ███ ██ ██   ███    ███  █████                
                     ████  ████ ████████ █████         ██  █████ ████     ██      ██                
                    ████████ ██  █████  ███ ███       ███   ██  ████████████████████                
                     ███████ ████  ██  ████████      █████  ██████   ████████     ███               
                     ████████████  ████████  ██     ███ ██   ███    ██████        ███               
                     ██  █████████████████  ███     ██   ██ ███████  █████         ██               
                     ██     ████████████  █████    ███      ██   ████████████████████               
                     ███  █████  ██ ███  ██  ██   ███   ██ ██    ███████████████████                
                      ██  ████████████  ██  ████  ██     ██████  ███████         ███                
                      ██ ████████████████  ██ ██ ██      ██████████ ███████     ███                 
                      ██ ███████████ ██   ██  █████  ██  ██████████████████     ██                  
                      ██  ██████████ ██ ███ █ ████    ██████████   ██████████  ██                   
                      ███████████████████  ███████     ██████████ ███████████████                   
                       ██  █████████████ ██ ████ ██    ████   ██████████████████                    
                       ██   ██████████████ █████ ██   ██████████ ██      ██████                     
                       ██  ██████████ ███ █████   ██ ███   ███████████████████                      
                       ██   █████████ ██ ██ ██     █████   ████████████    ██                       
                       ███  █████████ ████ ███   ██ ████████ ██████████   ███                       
                        ██   ████████ ███ ███ ██  ████   ███████████████████                        
                        ██   ████████  ██ ██   █  ███        ██████████████                         
                        ██    ██████   ████    ██ ██   ███  ██████████  ██                          
                        ██    ████ ████████     ████   ███████████████ ██                           
                     ██████   ████ ███████  █   ███████    ████████   ███                           
                  █████████     ██ ██████   ██  ██  ██████████████   ███                            
                ████   ████    ███████████   █████       ███   █     ██                             
                ██   ██████    █████████ █   ██████████  ████████   ██                              
               ██        ███    █████ ██ ██   ██    ███████        ███                              
              ███        ███    █████████ ██ █████     █████████  ███                               
              ██         ███     ████████  ████████   ███        █████                              
              ██       ██ ██     ███   ███  ██        ██     ██  ██████████                         
             ████      █  ██████████   ███ ██████    ██████████ ███ ██  █████                       
             ██ ██           ████████████████ █████ ███        ███  ███    ███                      
             ██  █              ██      ████      ███████████████     ██    ███                     
             ██                  ██      ████      █████████████       ██    ███                    
            ██     █              ██████   ██████ ███   ███████             ███████                 
           ███     ███████         ████       █████████████████           █████████                 
           ██        ████████                    ████                ████████   ██                  
          ██   ███         █                                    █████████       ██                  
          ███   ████              ██         █████        ███    █         ██  ███                  
           ████    ███            ███████     ███████████████          ██████  ██                   
             █████   ██   ████  ██   ███           ██████    █████████████    ██                    
                 ███       ███████                            ████████        ██                    
                  ██              █                          █               ██                     
                   ██    █     ████             ██████  ██████              ███                     
                   ███  █████████       ███      ███████████               ███                      
                    ██████   █     █████████████              ███████████████                       
                      ███████████████         █████        █████    ███████                         
                                                 ████████████                                       
                                                     ██████                                         
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    

## Acknowledgements

- [GlassFish](https://glassfish.org/)
- [Maven](https://maven.apache.org/)
- [OpenJDK](https://openjdk.java.net/)
