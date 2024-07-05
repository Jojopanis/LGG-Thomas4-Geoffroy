import os

def read_file(filename : str) -> list:
    words = []
    path = file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), filename)
    with open(path, 'r') as file:
        while line := file.readline():
            words.append(line.strip())
    return words