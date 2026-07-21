Step 1: Download Redis for Windows
	1- Go to https://github.com/tporadowski/redis/releases
	2- Download the latest .zip file (e.g., Redis-x64-xx.zip).
	3- Extract the ZIP file to C:\Redis.
Step 2: Start Redis
	1- Open Command Prompt as Administrator.	
	2- Navigate to the Redis folder on powershell: 
			cd C:\Redis
	3- Run Redis Server on powershell: 
			redis-server.exe
    4- Open another Command Prompt and run:
    		redis-cli.exe
    5- Test Redis:	
    		ping

    		If you get PONG, Redis is working!				

