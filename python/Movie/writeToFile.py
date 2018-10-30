with open('my_file.txt', 'w') as f:
    f.write("Hello World!")

with open('my_file.txt', 'r') as f:
    print(f.readline())
