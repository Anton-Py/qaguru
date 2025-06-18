import os.path

CURRENT_FILE = os.path.abspath(__file__)
# print(CURRENT_FILE)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
# print(CURRENT_DIR)
DATA_DIR = os.path.join(CURRENT_DIR, 'data')
# print(DATA_DIR)