import os

y = []
llst = []
all0 = ["VYZlm5WXin7oSkp)rs{6];þ4vyzq \_$%wU9dx1tu23c>?0,HIJ(KabhL*<MNT8efgABC|}[DEFGQ+-jOPR!@#=./^&"]

for i in all0:
    for m in i:
        llst.append(m)


def encrypt():
    os.system("cls")

    enter = input(">>>Encrypt: ")

    for i in range(len(enter)):
        if enter[i] in llst:
            for s in range(1, 6):
                fd = llst.index(enter[i]) + s
                y.append(llst[fd])

    listToStr = ''.join(map(str, y))
    return print("\nEncryption successful!\n\nencrypt: " + listToStr)


def decrypt():
    os.system("cls")
    enter = input(">>>Decrypt: ")

    for i in range(len(enter)):
        if enter[i] in llst:
            fd = llst.index(enter[i]) - 1
            for kk in range(0, len(enter), 5):
                if i == kk:
                    y.append(llst[fd])
    listToStr = ''.join(map(str, y))
    return print("\nDecryption successful!\n\ndecrypt: " + listToStr)


os.system("cls")
slct = input("1)Encrypt\n\n2)Decrypt\n\n3)Exit\n\n>>>Select: ")

while True:
    if slct == "1":
        encrypt()
        break
    elif slct == "2":
        decrypt()
        break
    elif slct == "3":
        break
    else:
        break

