import subprocess

def get_service_name(port):
    try:
        # Execute the lsof command to get the service name occupying the port
        result = subprocess.run(["lsof", "-i", "tcp:{}".format(port)], capture_output=True, text=True, check=True)
        # Filter the output to extract the service name
        service_name = result.stdout.split("\n")[1].split()[0]
        return service_name
    except subprocess.CalledProcessError as e:
        print("Error executing lsof command:", e)
        print("Command output (stderr):", e.stderr)
        return None

def execute_curl(port):
    # Get the service name
    service_name = get_service_name(port)
    if service_name:
        print("Service occupying port {}:".format(port), service_name)
    else:
        print("No service found occupying port", port)

    # Construct the curl command
    curl_command = ["curl", "http://localhost:{}/".format(port)]
    
    try:
        # Execute the curl command
        result = subprocess.run(curl_command, capture_output=True, text=True, check=True)
        # Print the output
        print("Curl output:", result.stdout)
    except subprocess.CalledProcessError as e:
        # Print error if curl command fails
        print("Error executing curl command:", e)
        print("Curl output (stderr):", e.stderr)

# Define the port number
port_number = 8080  # Change this to the port of your choice

# Execute curl command
execute_curl(port_number)
