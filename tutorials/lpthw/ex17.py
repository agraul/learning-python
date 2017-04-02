from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")


indata = open(from_file).read()

input(f'''
The input file is {len(indata)} bytes long
Does the output file exist? {exists(to_file)}
Ready, hit RETURN to continue, CTRL-C to abort.
''')

out_file = open(to_file, 'w').write(indata)


print("Alright, all done.")
