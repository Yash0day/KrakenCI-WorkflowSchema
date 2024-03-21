def stage(ctx):
    return {
        "parent": "root",
        "triggers": {
            "repo": {
                "url": "https://github.com/Cloudzero9/Kraken_Webapp.git",
                "branch": "main",
                "interval": "60m"
            }
        },
        "parameters": [],
        "configs": [],
        "jobs": [{
            "name": "Clone git repo and build",
            "steps": [
            {
                    "tool": "git",
                    "checkout": "https://github.com/Cloudzero9/Kraken_Webapp.git",
                    "destination": "kraken",
                    "branch": "main"
            },   

            {
                "tool": "shell",
                "cwd": "kraken",
                "cmd": "ls -la",                
                "user": "catchyash007",
            },
            {
                "tool": "shell",
                "cwd": "kraken",
                "cmd": "sudo apt-get update",                
                "user": "catchyash007",
            },
                {
                "tool": "shell",
                "script": """
                    # Check if pip3 is installed
                    if ! command -v pip3 &> /dev/null ; then
                        echo "pip3 is not installed. Installing..."
                        
                        sudo apt-get install -y python3-pip 
                    else
                        echo "pip3 is already installed."
                    fi

                """,              
                "user": "catchyash007",
            }, 
             {
                "tool": "shell",
                "cwd": "kraken",
                "cmd": "pip3 install robotframework robotframework-seleniumlibrary robotframework-requests",                
                "user": "catchyash007",
            },
             {
                "tool": "shell",
                "cwd": "kraken",
                "cmd": "robot --nostatusrc -x junit.xml *.robot",                
                "user": "catchyash007",
            },
             {
                "tool": "junit_collect",
                "cwd": "kraken",
                "file_glob": "junit.xml",                
                
            },
           

             {
                "tool": "shell",
                "cwd": "kraken",
                "script": """
                      # Check if flask is installed
                    if python3 -c "import flask" &> /dev/null ; then
                        echo "Flask is already installed."
                    else
                        echo "Installing Flask..."
                        sudo pip3 install flask  
                    fi
                
                """,                
                "user": "catchyash007",
            },
            {
                "tool": "shell",
                "cwd": "kraken",
                "script": """
                pgrep -f "python3 app.py" > /dev/null && { pid=$(pgrep -f "python3 app.py"); 
                echo "Process is running. PID: $pid"; kill $pid; echo "Process terminated."; } || 
                echo "Process is not running." 
                """,
                "user": "catchyash007",
            },
            {
                "tool": "shell",
                "cwd": "kraken",
                "cmd": "python3 app.py >> log.txt 2>&1 &",                
                "user": "catchyash007",
            },],
            "environments": [{
                "system": "any",
                "agents_group": "all",
                "config": "default"
            }]
        }]
    }
