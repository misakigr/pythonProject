import os
import re

def Rezka(bb):
    dirC = 'D:/misak/Разное/blockchain/'  # Directory where blk*.dat files are stored
    dirF = 'res/'  # Directory where to save parsing results
    fLi = os.listdir(dirC)
    fLi = [x for x in fLi if (x.endswith('.dat') and x.startswith('blk'))]
    fLi.sort()
    try:
        a = 0
        k = fLi[bb]
        print(k)
        # for k in fLi:
        namRrc = k
        p = dirC + namRrc
        print('Start ' + p)
        with open(p) as file:
            for line in file:
                ccc = str(line)
                ccc = re.sub("['|[]", "", ccc)
                ccc = ccc.replace('\n', '')  # Искомое слово без перевода строки
                a += 1
                file_name = (dirF + 'blk00{}.dat').format(a)
                f = open(file_name, 'w')
                f.write(ccc)
                f.close()
        #os.remove(p)
    except:
        pass
if __name__ == '__main__':
    Rezka()



