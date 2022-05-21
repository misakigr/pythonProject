import os
import re
import time


def Rezka(bb):
    dirC = 'resNEW/'  # Directory where blk*.dat files are stored
    dirF = 'res/'  # Directory where to save parsing results
    fLi = os.listdir(dirC)
    fLi = [x for x in fLi if (x.endswith('.dat') and x.startswith('blk'))]
    fLi.sort()
    # Проверяем на содержание файлов в папке res
    fLiFF = os.listdir(dirF)
    fLiFF = [x for x in fLiFF if (x.endswith('.dat') and x.startswith('blk'))]
    fLiFF.sort()


    try:
        if fLiFF == []:
            a = 0
            k = fLi[bb]
            #print(k)
            namRrc = k
            p = dirC + namRrc
            print('Start ' + p)
            with open(p) as file:
                for line in file:
                    ccc = str(line)
                    ccc = re.sub("['|[]", "", ccc)
                    ccc = ccc.replace('\n', '')  # Искомое слово без перевода строки
                    a += 1
                    file_name = (dirF + 'blk_{}.dat').format(str(ccc[16:]))
                    f = open(file_name, 'w')
                    f.write(ccc)
                    f.close()
            os.remove(p)
    except:
        pass
if __name__ == '__main__':
    pass



