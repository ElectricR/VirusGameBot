import os
import time

with open("curr_f", 'w') as f:
    for i in range(10):
        f.write('0' * 10 + '\n')
    f.write('1')

curr_p = '1'

for i in range(60):
    os.system("python3 virus/virus.py < curr_f > temp")
    os.system("cat temp")
    print()
    curr_p = {'1': '2', '2': '1'}[curr_p]
    with open("curr_f", 'w') as f, open("temp") as g:
        f.write(g.read())
        f.write(curr_p)
    time.sleep(0.1)

os.system("rm curr_f temp")


