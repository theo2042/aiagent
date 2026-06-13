import os
import config

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_dir_abs= os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
        # Will be True or False
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir:
            return (f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        if not os.path.isfile(target_dir):
            return (f'Error: File not found or is not a regular file: "{file_path}"')
        

        with open("example.txt", "r") as f:
            content = f.read(config.FILE_LIMIT)
        
        
    




    except Exception as e:
        return (f"Error: {e}")
