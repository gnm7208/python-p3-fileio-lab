def write_file(file_name, file_content):
    file_name = file_name + ".txt"
    with open(file_name, 'w') as f:
        f.write(file_content)
        f.close()
    pass

def append_file(file_name, append_content):
    file_name = file_name + ".txt"
    with open(file_name, 'a') as f:
        f.write(append_content)
        f.close()
    pass

def read_file(file_name):
    file_name = file_name + ".txt"
    with open(file_name, 'r') as f:
        print(f.read())
        f.close()   
    pass
