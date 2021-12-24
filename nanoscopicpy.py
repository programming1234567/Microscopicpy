def Builder(code):
    line1 = code[0:7]
    line2 = code[7:14]
    line3 = code[14:21]
    line4 = code[21:28]
    line1log = line1.count("log")
    line2log = line2.count("log")
    line3log = line3.count("log")
    line4log = line4.count("log")
    line1inp = line1.count("inp")
    line2inp = line2.count("inp")
    line3inp = line3.count("inp")
    line4inp = line4.count("inp")
    line1var = line1.count(" = ")
    line2var = line2.count(" = ")
    line3var = line3.count(" = ")
    line4var = line4.count(" = ")
    if line1log == 1:
        print(line1[5:7])
    if line2log == 1:
        print(line2[5:7])
    if line3log == 1:
        print(line3[5:7])
    if line4log == 1:
        print(line4[5:7])
    if line1inp == 1:
        input(line1[5:7])
    if line2inp == 1:
        input(line2[5:7])
    if line3inp == 1:
        input(line3[5:7])
    if line4inp == 1:
        input(line4[5:7])
    if line1var == 1:
        a = line1[5:7]
        print(a)
k = """
x = 9735345345
"""
Builder(k)