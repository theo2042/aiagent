from functions.get_files_info import get_files_info

try:
    get_files_info("calculator", ".")
    get_files_info("calculator", "/bin")
    get_files_info("calculator", "../")
    get_files_info("calculator", "main.py")
    

except Exception as e:
    print(f'Error: {e}')