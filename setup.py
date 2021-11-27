import random
import os
import shutil

# How to randomly partition a list into n nearly equal parts?
def partition(lst, n): 
    random.shuffle(lst)
    division = len(lst) / float(n) 
    ans = [ lst[int(round(division * i)): int(round(division * (i + 1)))] for i in range(n) ]
    random.shuffle(ans)
    return ans



li = ['A', 'B', 'C']
def create_folder():
    for c in li:
        if os.path.exists(os.path.join(os.getcwd(), 'AT&T_{}'.format(c))):
            shutil.rmtree(os.path.join(os.getcwd(), 'AT&T_{}'.format(c)))

        os.mkdir(os.path.join(os.getcwd(), 'AT&T_{}'.format(c)))
        for i in range(1, 41):
            os.mkdir(os.path.join(os.getcwd(), 'AT&T_{}\\s{}'.format(c,i)))

def copy_files():
    for i in range(1, 41):
        par_list = partition([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
        for j in range(3):
            for k in range(len(par_list[j])):
                shutil.copy('AT&T/s{}/{}.pgm'.format(i,par_list[j][k]), 'AT&T_{}/s{}/{}.pgm'.format(li[j],i,par_list[j][k]))


create_folder()
copy_files()