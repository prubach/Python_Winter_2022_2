import json
import os

print('Current Working dir: {}'.format(os.getcwd()))
print('My script: {}'.format(__file__))
print('My Python folder: {}'.format(os.path.dirname(__file__)))
#my_out_file = r'c:\users\prubac\Desktop\my_matrix_out.json'
#my_out_file = 'c:/users/prubac/Desktop/my_matrix_out.json'
my_out_file = 'my_matrix_out.json'

my_file = os.path.join(os.path.dirname(__file__), my_out_file)

with open(my_file, 'r') as f:
    m = json.load(f)
    print(m)
    print(type(m[0][2]))