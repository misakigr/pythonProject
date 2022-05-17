# autor: Misac Igor
# licese: GPL3
"""This is the "example" module.
"""

import os
import re
import RazborDef
import TabelDef
import WebOpen

k = 0
j = 0
c = ''
word = 'raw-tx'
dirA = 'res/'  # Directory where blk*.dat files are stored
dirB = 'wal_adr/'  # Directory where to save parsing results

fList = os.listdir(dirA)
fList = [x for x in fList if (x.endswith('.dat') and x.startswith('blk'))]
fList.sort()

for i in fList:
    nameSrc = i
    nameRes = nameSrc.replace('.dat', '.txt')
    resList = []
    SortList = []
    a = 0
    t = dirA + nameSrc
    print('Start ' + t)
    with open(t) as file:
        for line in file:
            c = str(line)
            c = re.sub("^\s+|\n|\r|\s+$", '', c)
            # print(c)
            match = WebOpen.Match(c)
            resList = RazborDef.Razb(match)

            wallet = TabelDef.Tab(resList)
            print(wallet)

            j += 1
            file_name = 'raz_tranz/list00{}.txt'.format(j)
            f = open(file_name, 'w')
            for z in resList:
                f.write(z + '\n')
            f.close()


            resList = []