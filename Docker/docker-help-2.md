### Basic Docker Commands

    C:\> docker -v  / docker --version   # Check Docker version  
    C:\> docker info                     # Get system-wide Docker information
    C:\> docker help                     # Get help on a specific command (e.g., `docker help run`) 
  
### Working with Images   

    docker images                       # List all images
    docker pull <image>                 # Download an image from Docker Hub
    docker build -t <name> .            # Build an image from a Dockerfile in current dir
    docker tag <image> <repo:tag>       # Tag an image for a repository  
    docker rmi <image>                  # Remove an image
    docker history <image>              # Show history of an image
    docker inspect <image>              # View detailed info 

### Working with Containers

    docker ps                           # List running containers
    docker ps -a                        # List all containers (including stopped)  
    docker run <image>                  # Run a container from an image
    docker run -d <image>               # Run container in detached mode  
    docker run -it <image>              # Run container in interactive mode
    docker exec -it <container> bash    # Access a running container  
    docker stop <container>             # Stop a running container 
    docker start <container>            # Start a stopped container
    docker restart <container>          # Restart a container  
    docker rm <container>               # Remove a container
    docker inspect <container>          # View detailed info

### Container Logs & Monitoring

    docker logs <container>          # View logs of a container
    docker logs -f <container>       # Follow logs in real time
    docker top <container>           # Show running processes inside a container 
    docker stats                     # Show real-time stats of running containers
    docker inspect <container>       # Get detailed info about a container
    docker events                    # Show real-time Docker events 

### Docker Networks

    docker network ls                               # List all networks  
    docker network create <name>                    # Create a new network 
    docker network inspect <name>                   # View details of a network 
    docker network connect <net> <container>        # Connect a container to a network 
    docker network disconnect <net> <container>     # Disconnect a container  

### Volumes & Persistent Storage

    docker volume ls                        # List all volumes 
    docker volume create <name>             # Create a volume
    docker volume inspect <name>            # Inspect a volume 
    docker volume rm <name>                 # Remove a volume 
    docker run -v <volume>:/path <image>    # Mount a volume in a container

### Docker Compose

    docker-compose up                 # Start services in docker-compose.yml 
    docker-compose up -d              # Start services in detached mode  
    docker-compose down               # Stop and remove all services 
    docker-compose ps                 # List running services 
    docker-compose logs               # View logs from services

### Cleaning Up

    docker system prune               # Remove unused images, containers, and networks
    docker image prune -a             # Remove all unused images
    docker container prune            # Remove all stopped containers
    docker volume prune               # Remove all unused volumes 





    install docker desktop on windows server 2022

Installing Docker Desktop on Windows Server 2022 is not officially supported. Docker Desktop is primarily designed for Windows 10/11 and Windows Server is not a supported platform. However, you can install Docker Engine (without Docker Desktop) on Windows Server 2022.

If you specifically need Docker Desktop, you may try workarounds, but Docker Engine is the recommended approach.

Install Docker Desktop on Windows Server 2022 (Workaround)
If you need Docker Desktop (with GUI and Linux containers), you can try the following unsupported workaround:

Step 1: Install Hyper-V

	Docker Desktop requires Hyper-V, which is available on Windows Server 2022:

	powershell
	Install-WindowsFeature -Name Hyper-V -IncludeAllSubFeature -Restart

	If Windows Server is running as a virtual machine, you must enable nested virtualization in PowerShell (on the host machine):
Step 2: Enable Nested Virtualization (If Running on a VM)

	powershell
	Set-VMProcessor -VMName delhidev1srv1 -ExposeVirtualizationExtensions $true

Step 3: Download and Install Docker Desktop

	Download Docker Desktop from the official site:
    https://www.docker.com/products/docker-desktop/
