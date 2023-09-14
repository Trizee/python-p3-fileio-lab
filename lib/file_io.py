def write_file(file_name, file_content):
   with open(f'{file_name}.txt', 'w',encoding='utf-8') as f:
       f.write(file_content)

def append_file(file_name, append_content, encoding='utf-8'):
    with open(f'{file_name}.txt', 'a') as f:
        f.write(append_content)

def read_file(file_name, encoding='utf-8'):
    with open(f'{file_name}.txt') as f:
        return f.read()
