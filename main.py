import os
import csv
import time
from sample_generator import sample_generator
from execute import execute
from config import *


if __name__ == '__main__':
    start = time.time()
    if not os.path.exists('./output'): 
        os.mkdir('output')
    equal = open("./output/equal.csv", "w")
    inequal = open("./output/inequal.csv", "w")
    e_writer = csv.writer(equal)
    i_writer = csv.writer(inequal)
    e_writer.writerow(["file1", "file2"])
    i_writer.writerow(["file1", "file2"])
    for dir in os.listdir('input'):
        if not os.path.isdir('input/' + dir):
            continue
        sample_list = sample_generator('input/' + dir + '/stdin_format.txt' , sample_num)
        result_table  = []
        print("Working on " + 'input/' + dir)
        for f in os.listdir('input/' + dir):
            if (f.endswith('.cpp')):
                result_table.append(execute('input/' + dir + '/' + f, sample_list))

        for i in range(len(result_table)):
            for j in range(i + 1, len(result_table)):
                if (result_table[i]["output"] == result_table[j]["output"]):
                    e_writer.writerow([result_table[i]["name"], result_table[j]["name"],])
                else: 
                    i_writer.writerow([result_table[i]["name"], result_table[j]["name"],])
    equal.close()
    inequal.close()
    if (os.name == 'nt'):
        if (os.path.exists("./a.exe")):
            os.remove("./a.exe")
    else:
        if (os.path.exists("./a.out")):
            os.remove("./a.out")   
    end = time.time()
    print("Done, it takes: ", round(end - start, 2), "s")
        
