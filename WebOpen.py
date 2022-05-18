# autor: Misac Igor
# licese: GPL3
"""This is the "example" module.
"""

from urllib.request import urlopen
import re
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time


def Match(c):
    htmlfile = urlopen("https://btc.bitaps.com/raw/transaction/%s?format=json" % c, timeout=10)
    htmltext = htmlfile.read().decode('utf-8')
    b = htmltext.partition('raw-tx')[2]
    match = re.search(r'(?:\w+\d+\w+)+', b)
    match = match[0]

    return match


def Razb(match):
    resList = []
    word = '022100'
    # С начала
    text = str(match)
    if text.isprintable() == False:
        text = text[:(len(text) - 1)]
    c = (text[:8])  # 1
    b = (text[8:])
    b_end = c
    resList.append(c)
    c = (b[:2])  # 2
    b = (b[2:])
    resList.append(c)
    c = (b[:64])  # 3
    b = (b[64:])
    resList.append(c)
    c = (b[:8])  # 4
    b = (b[8:])
    resList.append(c)
    # 5
    if '0220' in b[:20]:
        resList.append(b.partition('0220')[0] + '0220')
        b = b.partition('0220')[2]
    else:
        resList.append(b.partition('022100')[0] + word)
        b = b.partition('022100')[2]
    # 6
    c = (b[:64])
    b = (b[64:])
    resList.append(c)
    # 7
    if '022100' in b[:20]:
        resList.append('022100')
        b = b.partition('022100')[2]
    else:
        resList.append('0220')
        b = b.partition('0220')[2]
    # 8
    c = (b[:64])
    b = (b[64:])
    resList.append(c)
    b = (b[:-86])
    # 9
    if '01000000' in b:
        kk = (b.partition('01000000')[0])
        c1 = kk[:-72]
        resList.append(c1)
        # 10
        resList.append('ffffffff')
        # 11
        c = kk[-64:]
        resList.append(c)
        # 12
        resList.append('01000000')
        b = (b.partition(kk)[2])
        b = (b.partition('01000000')[2])
    elif '00000001' in b:
        kk = (b.partition('00000001')[0])
        c1 = kk[:-72]
        resList.append(c1)
        # 10
        resList.append('ffffffff')
        # 11
        c = kk[-64:]
        resList.append(c)
        # 12
        resList.append('00000001')
        b = (b.partition(kk)[2])
        b = (b.partition('00000001')[2])
    elif '00000000' in b:
        kk = (b.partition('00000000')[0])
        c1 = kk[:-72]
        resList.append(c1)
        # 10
        resList.append('ffffffff')
        # 11
        c = kk[-64:]
        resList.append(c)
        # 12
        resList.append('00000000')
        b = (b.partition(kk)[2])
        b = (b.partition('00000000')[2])
    # 13
    if '0220' in b[:20]:
        resList.append(b.partition('0220')[0] + '0220')
        b = b.partition('0220')[2]
    else:
        resList.append(b.partition('022100')[0] + word)
        b = b.partition('022100')[2]
    # 14
    c = (b[:64])
    b = (b[64:])
    resList.append(c)
    # 15
    if '0220' in b[:20]:
        resList.append(b.partition('0220')[0] + '0220')
        b = b.partition('0220')[2]
    else:
        resList.append(b.partition('022100')[0] + word)
        b = b.partition('022100')[2]
    # 16
    c = (b[:64])
    b = (b[64:])
    resList.append(c)
    # 17
    resList.append(b)
    # С конца
    # 18
    c = (text[-86:-78])
    resList.append(c)
    # 19
    c = (text[-78:-76])
    resList.append(c)
    # 20
    c = (text[-76:-60])
    resList.append(c)
    # 21
    c = (text[-60:-58])
    resList.append(c)
    # 22
    c = (text[-58:-8])
    resList.append(c)
    # 23
    c = (text[-8:])
    resList.append(c)

    resList.append(b_end)

    return resList


def Tab(c):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://sagecell.sagemath.org/")
    phn = driver.find_element_by_xpath('//*[@id="cell"]/div[1]/div[1]/div/div[1]/textarea').send_keys(c)
    # time.sleep(2)
    driver.find_element_by_xpath('//*[@id="cell"]/div[1]/button').click()
    time.sleep(5)
    result = driver.find_element_by_xpath('// *[ @ id = "cell"] / div[3] / div[1] / div / div[2]').text
    driver.close()
    header = result
    import codecs  # If not installed: "pip3 install codecs"
    import hashlib
    bits_hex = hex(int(header))
    # 0x66d891b5ed7f51e5044be6a7ebe4e2eae32b960f5aa0883f7cc0ce4fd6921e31
    private_key = bits_hex[2:]
    PK0 = private_key
    PK1 = '80' + PK0
    PK2 = hashlib.sha256(codecs.decode(PK1, 'hex'))
    PK3 = hashlib.sha256(PK2.digest())
    checksum = codecs.encode(PK3.digest(), 'hex')[0:8]
    PK4 = PK1 + str(checksum)[2:10]  # I know it looks wierd

    # Define base58
    def base58(address_hex):
        alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
        b58_string = ''
        # Get the number of leading zeros
        leading_zeros = len(address_hex) - len(address_hex.lstrip('0'))
        # Convert hex to decimal
        address_int = int(address_hex, 16)
        # Append digits to the start of string
        while address_int > 0:
            digit = address_int % 58
            digit_char = alphabet[digit]
            b58_string = digit_char + b58_string
            address_int //= 58
        # Add ‘1’ for each 2 leading zeros
        ones = leading_zeros // 2
        for one in range(ones):
            b58_string = '1' + b58_string
        return b58_string

    WIF = base58(PK4)
    # print(WIF)
    from bitcoinaddress import Wallet
    wallet = Wallet(WIF)

    return wallet


if __name__ == '__main__':
    print(Match('5439C37C4C6DAD4AD93B1D5598D57F1AACE9D0F68B892236DA903B3F136451A1'))
