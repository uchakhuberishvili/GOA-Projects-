#algorithm code
import os
def calculate_directory_size(directory):
    total_size = 0
    for entry in os.scandir(directory):
        if entry.is_file():
            total_size += entry.stat().st_size
            print(f"File: {entry.name}, Size: {total_size/1024:.2f} KB")
            continue
        total_size += calculate_directory_size(entry.path)
        print(f"Directory: {entry.name}, Size: {total_size/1024:.2f} KB")
        continue
    return total_size

directory = input("Enter directory path: ")

if not os.path.isdir(directory):
    print(f"Error: {directory} is not a valid directory.")
    exit(1)

directory_size = calculate_directory_size(directory)

print(f"Total size of {directory}: {directory_size/1024:.2f} KB")

