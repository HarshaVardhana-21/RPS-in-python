with open("03_Append.txt", 'r') as f:
    content = f.read()
    for line in content.splitlines():
        print(line)