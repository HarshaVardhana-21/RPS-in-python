from pathlib import Path

a = "Lorem ipsum dolor sit amet * 2 \n"

if Path("Append.txt").exists():
    file = open("Append.txt", 'a')
    file.write(a)
else:
    file = open("Append.txt", 'w')
    file.write(a)
    
file.close()