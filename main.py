# autor: Misac Igor
# licese: GPL3
"""This is the "example" module.
"""

import os
import re
import SelectAdress
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
            resList = WebOpen.Razb(match)
            f = open('file_name.txt', 'w')
            for i in resList:
                f.write(i + '\n')
            f.close()
            t = 'file_name.txt'
            i = 1
            with open(t) as file:
                while i <= 24:
                    exec("x{} = {}".format(i, 'str(file.readline())'))
                    i += 1
                x0 = '00'
                x00 = ''
                res1 = x1 + x2 + x3 + x4 + x21 + x22 + x10 + x11 + x12 + x0 + x00 + x18 + x19 + x20 + x21 + x22 + x23 + x24
                res1 = res1.replace("\r", "")
                res1 = res1.replace("\n", "")
                from binascii import unhexlify
                from hashlib import sha256

                res1 = unhexlify(res1)
                res1 = sha256(sha256(res1).digest()).hexdigest()
                res = x1 + x2 + x3 + x4 + x0 + x00 + x10 + x11 + x12 + x21 + x22 + x18 + x19 + x20 + x21 + x22 + x23 + x24
                res = res.replace("\r", "")
                res = res.replace("\n", "")
                res = unhexlify(res)
                res = sha256(sha256(res).digest()).hexdigest()
                c = ""
                c1 = 'p  = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141'
                c = c + c1 + '\n'
                c2 = 'r  = 0x' + x6
                c = c + c2
                c3 = 's1 = 0x' + x8
                c = c + c3
                c4 = 's2 = 0x' + x16
                c = c + c4
                c5 = 'z1 = 0x' + res1 + '\n'
                c = c + c5
                c6 = 'z2 = 0x' + res
                c = c + c6 + '\n'
                c7 = 'K = GF(p)'
                c = c + c7 + '\n'
                c8 = 'K((z1*s2 - z2*s1)/(r*(s1-s2)))'
                c = c + c8
                wallet = WebOpen.Tab(c)

                f = open('file_wall.txt', 'w')
                f.write(str(wallet))
                f.close()

                List = SelectAdress.Sel()


                f = open('Lists.txt', 'a')
                for L in List:
                    f.write(L)
                f.close()
                List = []

                # Удаление дубликатов строк
                file = 'Lists.txt'
                uniqlines = set(open(file, 'r', encoding='utf-8').readlines())
                gotovo = open(file, 'w', encoding='utf-8').writelines(set(uniqlines))

            j += 1
            file_name = 'raz_tranz/list00{}.txt'.format(j)
            f = open(file_name, 'w')
            for z in resList:
                f.write(z + '\n')
            f.close()
            resList = []

            file_name = 'wal_adr/wall00{}.dat'.format(j)
            f = open(file_name, 'w')
            f.write(str(wallet))
            f.close()
