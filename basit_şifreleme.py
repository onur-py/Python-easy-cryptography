import os




y=[]
llst=[]
all0=["VYZlm5ğWXıin7oöSŞkp)rs{6];şü4vyzq \_$%wU9Üdx1tu23c>?0,çĞHIİJ(KabhL*<MNT8efgABC|}[ÇDEFGQ+-jOÖPR!@#=./^&"]


for i in all0:
    for m in i:
        llst.append(m)


def encrypt():
    os.system("cls")

    enter=input("Şifrelenmek istenen bilgi: ")

    for i in range(len(enter)):
        if enter[i] in llst:
            for s in range(1,6):
                fd=llst.index(enter[i])+s
                y.append(llst[fd])
        
    listToStr=''.join(map(str,y))
    return print("\nBilgileriniz başarıyla şifrelendi!\n\nencrypt: "+listToStr)







def decrypt():
    enter=input("Şifrelenmiş bilgiyi giriniz: ")
    
    for i in range(len(enter)):
        if enter[i] in llst:
            fd=llst.index(enter[i])-1
            for kk in range(0,len(enter),5):
                if i==kk:
                    y.append(llst[fd])
    listToStr=''.join(map(str,y))
    return print("\ndecrypt işlemi başarılı!\n\ndecrypt: "+listToStr)



os.system("cls")
slct=input("1)Encrypt\n\n2)Decrypt\n\n3)Çıkış\n\n\t\tSelect: ")




 
while True:
    if slct=="1":
        encrypt()
        break
    elif slct=="2":
        decrypt()
        break
    elif slct=="3":
        break
    else:
        break
        







