import os

def search_file(file_name, search_path=None):
    """
    Searches for a file with a specific name in the given directory and its subdirectories.
    If no directory is specified, the current working directory is used.
    
    :param file_name: Name of the file to search for
    :param search_path: Directory path to start searching from (optional)
    :return: List of paths where the file was found
    """
    if search_path is None:
        search_path = os.getcwd()  # Use the current working directory if no path is provided

    result = []
    for root, dirs, files in os.walk(search_path):
        if file_name in files:
            result.append(os.path.join(root, file_name))
    
    return result

if __name__ == "__main__":
    # Example usage
    file_name = input("Enter the file name to search for (e.g., 'myfile.txt'): ")
    search_path = None #input("Enter the directory path to search (optional, leave blank to search in current directory): ")
    
    # If no search path is provided, search in the current working directory
    search_path = search_path if search_path else None

    found_files = search_file(file_name, search_path)

    if found_files:
        print("File found at the following locations:")
        for file_path in found_files:
            print(file_path)
    else:
        print("File not found.")
