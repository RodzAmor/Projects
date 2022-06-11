import os

f = open('text', 'r') # Reading a file
# 'r' represents reading mode
print(f.read())

f = open('text', 'a')
f.write("new line") # Adds a more text to file
f.close()

# f = open('text', 'x') # Creates a file. Makes an error if file exists
f = open('temp', 'x') # Creates file
os.remove('temp') # deletes file
if os.path.exists('temp'):
    os.remove('temp')
else:
    print('The file does not exist')