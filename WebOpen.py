# autor: Misac Igor
# licese: GPL3
"""This is the "example" module.
"""

from urllib.request import urlopen
import re

k = 0
j = 0
c = ''
def Match(c):
    htmlfile = urlopen("https://btc.bitaps.com/raw/transaction/%s?format=json" % c, timeout=10)
    htmltext = htmlfile.read().decode('utf-8')
    b = htmltext.partition('raw-tx')[2]
    match = re.search(r'(?:\w+\d+\w+)+', b)

    match = match[0]

    return match

if __name__ == '__main__':
    print(Match('5439C37C4C6DAD4AD93B1D5598D57F1AACE9D0F68B892236DA903B3F136451A1'))