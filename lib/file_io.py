from pathlib import Path
import subprocess

def write_file(file_name, file_content):
    file_path = Path(file_name).with_suffix('.txt')
    with open(file_path, 'w') as f:
        f.write(file_content)

def append_file(file_name, append_content):
    file_path = Path(file_name).with_suffix('.txt')
    with open(file_path, 'a') as f:
        f.write(append_content)

def read_file(file_name):
    file_path = Path(file_name).with_suffix('.txt')
    with open(file_path, 'r') as f:
        content = f.read()
    return content

def commit_code(commit_msg="Save changes"):
    """
    Executes git add and git commit with the given commit message.
    """
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        print(f"Committed changes with message: '{commit_msg}'")
    except subprocess.CalledProcessError as e:
        print("An error occurred while trying to commit changes:", e)


# use write_file function. 
write_file(file_name="logfile", file_content="Log 1: 5 bananas added\n" )
append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted\n")

content = read_file(file_name="logfile")
print(content)

commit_code("Implemented file IO functions: write_file, append_file, read_file")
