import os
my_out_file = r'my_matrix_out.json'

if os.path.exists(my_out_file):
    print('File {} exists'.format(my_out_file))
else:
    print('File {} does not exists'.format(my_out_file))

from pathlib import Path
#home_folder = os.path.expanduser('~')
home_folder = Path.home()
print(home_folder)
#my_folder = r''
my_desktop = os.path.join(home_folder, 'Desktop')
print(os.listdir(my_desktop))

for f in os.listdir(my_desktop):
    desc = 'd' if os.path.isdir(f) else '-'
    print(f'{desc} {f}')