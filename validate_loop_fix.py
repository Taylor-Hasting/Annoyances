import re
import os



#I'll admit i'm not a good coder and used ChatGPT to convert my workflow into a python path. 
#Someone smarter than me can probably improve this. 
# Function to read log text from a file
def read_log_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Path to the log file
log_file_path = os.path.expanduser("~/.local/share/Steam/logs/content_log.txt")

# Read log text from the file
log_text = read_log_from_file(log_file_path)

# Extract lines containing 'Failed' and the associated file path
failed_lines = re.findall(r'\[.*?\] AppID \d+ update canceled : Failed.*?\"(.*?)\"', log_text)

# Iterate through failed lines and attempt to delete the associated .ucas file
for file_path in failed_lines:
    try:
        if file_path.endswith('.ucas'):
            os.remove(file_path)
            print(f"Deleted {file_path}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except PermissionError:
        print(f"No permission to delete: {file_path}")

