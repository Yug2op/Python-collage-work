def readFile(fileName):
    try:
        with open(fileName,'r') as file:
            for line in file:
                 print(line,end=' ')
    except FileNotFoundError:
        print(f"File {fileName} not found.")
readFile('Hello.txt')