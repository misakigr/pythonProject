
def Sel():
    word = 'Public Address 1: '  # Искомое слово
    dorw = 'Public Address 1 compressed: '  # Искомое слово 2
    List = []
    f = open('file_wall.txt', 'r')
    for line in f:
        if word in line:
            text = str(line)
            List.append(text.partition(word)[2])
            # print(kb)
        if dorw in line:
            text = str(line)
            List.append(text.partition(dorw)[2])
    return List

