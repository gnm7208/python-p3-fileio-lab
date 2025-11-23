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

# use write_file function. 
write_file(file_name="logfile", file_content="Log 1: 5 bananas added" )
append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted")

read_file(file_name="logfile")
# Log 1: 5 bananas added
# Log 2: 3 bananas subtracted