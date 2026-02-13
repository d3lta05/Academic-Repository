import sys
import os

def deleteFile(filename):
    try:
        os.remove(filename)
        print(f"Deleted file: {filename}")
    except Exception as e:
        sys.stderr.write(f"Error deleting file: {e}\n")
        sys.exit(1)
        
def directoryDelete(directory):
    try:
        
        for root, dirs, files in os.walk(directory, topdown=False):
            for name in files:
                file_path = os.path.join(root, name)
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
            for name in dirs:
                dir_path = os.path.join(root, name)
                os.rmdir(dir_path)
                print(f"Deleted directory: {dir_path}")
        os.rmdir(directory)
        print(f"Deleted directory: {directory}")
        
    except Exception as e:
        sys.stderr.write(f"Error deleting directory: {e}\n")
        sys.exit(1)
    
    
def recursiveCheck():
    recursiveDelete = sys.argv[1] if len(sys.argv) > 1 else None
    if recursiveDelete == "-R":
        return True
    return False

def main():
    
    recursive = recursiveCheck()
    
    if not recursive:
        print("Give the path of a file to delete")
        filename = input()
        deleteFile(filename)
    
    elif recursive:
        
        print("Caught recursive flag")
        print("Give the path of a directory to RECURSIVELY delete")
        
        directory = input()
        
        directoryDelete(directory)
        
    
    else:
        print("Unknown Fatal Error, exiting...")
        sys.exit(1)
        
    print("Run program again? (y/n)")
    response = input().strip().lower()
    
    if response == 'y':
        main()
    else:
        print("Goodbye!")
        sys.exit(0)
                
if __name__ == "__main__":
    main()
