filename = input("Enter the name of the file to read: ")

try:
    # Use the filename input by the user
    with open(filename, "r") as file:
        content = file.read()
    
    # Modify the content (example: convert to uppercase)
    modified_content = content.upper()

    # Write modified content to a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)

    print(f"Modified content written to {new_filename} successfully!")

except FileNotFoundError:
    # This will catch if the original file doesn't exist
    print(f"Error: The file '{filename}' does not exist. Please check the name and try again.")

except IOError:
    print("Error: There was a problem reading or writing the file.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
