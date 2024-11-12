#1
# import os
# import sys

# def list_files_in_directory(directory_path, file_extension):
#     try:
#         if not os.path.isdir(directory_path):
#             raise ValueError("Invalid directory path")
        
#         if not file_extension.startswith("."):
#             raise ValueError("File extension should start with a dot (e.g., .txt)")

#         for root, _, files in os.walk(directory_path):
#             for file_name in files:
#                 if file_name.endswith(file_extension):
#                     file_path = os.path.join(root, file_name)
#                     try:
#                         with open(file_path, 'r') as file:
#                             content = file.read()
#                             print(f"Contents of {file_name}:\n{content}\n")
#                     except (IOError, OSError) as file_error:
#                         print(f"Could not read {file_name}: {file_error}")
#     except ValueError as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     if len(sys.argv) != 3:
#         print("invalid") #python homework6.py folder .txt
#     else:
#         directory = sys.argv[1]
#         extension = sys.argv[2]
#         list_files_in_directory(directory, extension)

#2
# import os
# import sys

# def rename_files_with_prefix(directory_path):
#     try:
#         if not os.path.isdir(directory_path):
#             raise ValueError("Invalid directory path")
        
#         files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
#         files.sort()

#         for idx, file_name in enumerate(files, start=1):
#             original_path = os.path.join(directory_path, file_name)
#             new_name = f"file{idx}{os.path.splitext(file_name)[1]}"
#             new_path = os.path.join(directory_path, new_name)
            
#             try:
#                 os.rename(original_path, new_path)
#                 print(f"Renamed {file_name} to {new_name}")
#             except (IOError, OSError) as rename_error:
#                 print(f"Could not rename {file_name}: {rename_error}")
                
#     except ValueError as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("invalid") #python homework6.py folder
#     else:
#         directory = sys.argv[1]
#         rename_files_with_prefix(directory)

#3
# import os
# import sys

# def calculate_total_size(directory_path):
#     total_size = 0
#     try:
#         if not os.path.isdir(directory_path):
#             raise ValueError("Invalid directory path")
        
#         for root, _, files in os.walk(directory_path):
#             for file_name in files:
#                 file_path = os.path.join(root, file_name)
#                 try:
#                     total_size += os.path.getsize(file_path)
#                 except (IOError, OSError) as file_error:
#                     print(f"Could not access {file_name}: {file_error}")

#         print(f"Total size: {total_size} bytes")

#     except ValueError as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("invalid") #python homework6.py folder
#     else:
#         directory = sys.argv[1]
#         calculate_total_size(directory)

#4
import os
import sys
from collections import defaultdict

def count_files_by_extension(directory_path):
    extension_count = defaultdict(int)

    try:
        if not os.path.isdir(directory_path):
            raise ValueError("invalid path")

        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        
        if not files:
            print("empty folder")
            return

        for file_name in files:
            _, extension = os.path.splitext(file_name)
            extension_count[extension] += 1

        for ext, count in extension_count.items():
            print(f"{ext or 'No extension'}: {count} files")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("invalid") #python homework6.py folder
    else:
        directory = sys.argv[1]
        count_files_by_extension(directory)
