# autor: Misac Igor
# licese: GPL3
"""This is the "example" module.
"""


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


if __name__ == "__main__":
    print(Razb('0100000002f522914c0ed9d6877d8c964be934b7c4555b4d2c6867d2fb6761fa965511e62b0000000049483045022100fe250c2ae048800d5fb268ca1f46fca65016c08ffd6bc64ad1d6f2a54500331f02202955e4cd17fa21f864009a7eb4606132fb938225ec8663b491d2fd464824b24301ffffffff31787113df29141747d61e26319ab5e168ee0272deea08ad23803bb2a6ef1f87000000004847304402203baab2ff57ea4a7148ff8ceb0a6cfa35cfc9a7316dc4e801c42a8456315cf3e60220327ae1b781fc21b7ab5f84e76b73b286acbd1a204cecf5576815fd789bf4a03201ffffffff0100e40b54020000001976a91428b4a69ff958801b1289f6888671eba670dcf51d88ac00000000'))
