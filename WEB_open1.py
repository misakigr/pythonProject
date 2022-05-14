import os
from urllib.request import urlopen
import re

c = ''
word = 'raw-tx'
dirA = 'res/'  # Directory where blk*.dat files are stored
# dirA = sys.argv[1]
dirB = 'res/'  # Directory where to save parsing results
# dirA = sys.argv[2]

fList = os.listdir(dirA)
fList = [x for x in fList if (x.endswith('.dat') and x.startswith('blk'))]
fList.sort()
# Источник: https://pythonim.ru/list/metod-sort-python)

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

            htmlfile = urlopen("https://btc.bitaps.com/raw/transaction/%s?format=json" % c, timeout=10)
            htmltext = htmlfile.read().decode('utf-8')
            b = htmltext.partition('raw-tx')[2]
            match = re.search(r'(?:\w+\d+\w+)+', b)
            # print(match[0] if match else 'Not found')

            file = open('trans.txt', 'a')
            file.write(match[0] + '\n')
            file.close()
