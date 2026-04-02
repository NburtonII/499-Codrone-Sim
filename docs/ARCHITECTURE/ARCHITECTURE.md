# Architecture Overview
This Document serves to equip readers and the development team to understand the codebase of the project. Use this document to navigate the repository and contribute as needed. 

## Project Structure
[Project Root]/
├──  docs/                                #This contains the documentation produced during development.
|    ├──  ARCHITECTURE/                   #Contains this document and other documents on the structure of the project
|    ├──  BUILD INFO/                     #documentation detailing the build details
|    ├──  Presentation/                   #the presentations produced at the end of every week
|    ├──  Sprints/                        #the sprint plans produced at the beginning of every week
|    ├──  Templates/                      #Contains the templates for the documentation 
├──  examples/                            #Contains test Run programs for the SDK
├──  missions/                            #Contains preprogrammed instructions for drone movement
├──  runs/                                #Data produced for each run
|    ├── RunCommands/                     #Running logs for each run command
|    ├── RunTelemetry/                    # Telemetry data the drone produces for each run.
|    ├── Startup.json/                    # Startup information for each run
├──  sdk/                                 #Contains the Python Client and scripts that interact with the simulation. 
|    ├──  client/                         #Client scripts and libraries that connect to the sim and control the drone
|          ├── cpp                        #Airsim Client CPP files
|          ├── projectairsim              #Arisim python Libraries and build files
|          ├── Python                     #Example Scripts written by IAMAI
|          ├── simConfig                  #Configuration files for the drone scripts
|    
├── sim/                                  #Holds Unreal project files
|    ├──  Build/Windows                   #Contains the weekly build files
|    ├──  Config                          #Configuration files for unrela
|    ├──  Content                         #Models and ussets used in the Unreal simulation
|    ├──  Plugins                         #Plugins used, specifically the projectairsim project.
|    ├──  CodroneSim.uproject             #Airism project
├── tests                                 #Holds tests missions
├── tools                                 #(Not used yet)
├── .gitattributes                        #Holds our git methods
├──  .gitignore                           #Details which files to ignore when we push
├──  README.md                            #Project description and credits
├──  projectairsim_client.log             #Log of the commands and events that happened on the previous run



## Core Technologies

The codrone airsim uses the following components

##### Unreal Engine

This acts as our main physics and graphics engine.

##### Project Airsim

This is how we simulate our drone. It was created by IAMAI to simulate vehicles in various game engines. It creates a server in Unreal and allows us to connect to it through Python and send commands to a simulated Drone.

##### Python
Python is our main scripting language. It communicates well with Project Airsims API's.
