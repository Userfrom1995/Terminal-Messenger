import subprocess

# Run the first file
process1 = subprocess.Popen(['python', 'Client.py'])

# Run the second file
process2 = subprocess.Popen(['python', 'Server.py'])

# Wait for both processes to complete (optional)
process1.wait()
process2.wait()