import os
import re

dirA = 'resNEW/'  # Directory where blk*.dat files are stored
dirB = 'res/'  # Directory where to save parsing results

fList = os.listdir(dirA)
fList = [x for x in fList if (x.endswith('.dat') and x.startswith('blk'))]
fList.sort()

j = 0
for i in fList:
    nameSrc = i
    t = dirA + nameSrc
    print('Start ' + t)
    with open(t) as file:
        for line in file:
            c = str(line)
            c = re.sub("['|[]", "", c)
            c = c.replace('\n', '')  # Искомое слово без перевода строки
            j += 1
            file_name = (dirB+'blk00{}.dat').format(j)
            f = open(file_name, 'w')
            f.write(c)
            f.close()