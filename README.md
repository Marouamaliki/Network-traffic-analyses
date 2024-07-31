# Network-traffic-analyses
This code captures network packets on a specified interface for a determined duration, then analyzes and displays relevant information for each captured packet. 
This can be useful for monitoring and diagnosing network traffic, as well as for detecting potential security threats. 
This project uses Python and the Pyshark library to capture and analyze network packets.

# Step 1: Set Up Your Environment
  - Install Python on your system.
  - Install necessary libraries such as Pyshark using `pip install pyshark`.
  - Ensure you have the necessary permissions to capture network traffic (may require administrator or root access).

# Step 2: Capture Network Traffic
  - Use Pyshark's `LiveCapture` to initiate packet capture on the chosen interface.
  - Define the duration for which the capture should run.

# Step 3: Analyze Captured Packets
  - Iterate through the captured packets.
  - Extract and print details such as packet number, timestamp, source IP, destination IP, protocol, and length.
  - Handle packets that may not have certain expected attributes gracefully.

# Step 4: Main Function to Run the Capture and Analysis
  - Define the main function that sets up the capture and calls the analysis function.
  - Start the packet capture for the defined duration.
  - Pass the captured packets to the analysis function for processing and output.

# Notes
-> Ensure you have the necessary permissions to capture network traffic. You might need to run the script as an administrator.
-> Adjust the interface parameter in capture_traffic to match the network interface you want to capture traffic on (e.g., 'Ethernet' for a wired connection).
