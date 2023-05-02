import os

input_file_extension = ".sub"
output_file_extension = ".c16"
intermediate_freq = "//"  # example value, replace with your desired value
amplitude_percentage = "100"  # example value, replace with your desired value
sampling_rate = "500000"  # example value, replace with your desired value

# Traverse through all the directories and subdirectories in the current working directory
for root, dirs, files in os.walk("."):
    # Check each file in the current directory for the specified input file extension
    for file in files:
        if file.endswith(input_file_extension):
            # Generate the full file path for the input file
            input_file_path = os.path.join(root, file)
            # Generate the output file name by replacing the input file extension with the output file extension
            output_file_name = os.path.splitext(file)[0] + output_file_extension
            # Generate the full file path for the output file
            output_file_path = os.path.join(root, output_file_name)
            # Construct the npm start command with the input and output file paths, and other specified arguments
            command = f"npm start -- -f \"{input_file_path}\" -a {amplitude_percentage} -sr {sampling_rate} -o \"{output_file_path}\""
            # Print the command to the console (optional)
            print(command)
            # Execute the command (optional)
            os.system(command)