# KrakenCI-WorkflowSchema


A Kraken CI workflow Schema to: 

1. Clone the python calculator web app repository into the container run by the
agent on the server.
2. Update the server repositories to install necessary python packages and tools.
3. Check if pip3 and flask are already installed, if not, installs them.
4. Kill the process python3 if it is already running to vacate the port 8443.
5. Run the app.py file in background.
6. Executes the 2 test cases and stores the artifacts on the kraken artifact center, Using Robot Framework.
