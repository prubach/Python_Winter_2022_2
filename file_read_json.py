import json

my_out_file = 'my_matrix_out.json'
with open(my_out_file, 'r') as f:
    m = json.load(f)
    print(m)
    print(type(m[0][2]))