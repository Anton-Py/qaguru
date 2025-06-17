import os.path

CURRENT_FILE = os.path.abspath(__file__)

print(CURRENT_FILE)

CURRENT_DIR = os.path.dirname(CURRENT_FILE)

print(CURRENT_DIR)

TMP_DIR = os.path.join(CURRENT_DIR, 'tmp')

print(TMP_DIR)






# with open("my_file.txt", "w") as my_file:
#     my_file.write("Hello World")