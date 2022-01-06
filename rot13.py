from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename


def choose_file():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    return filename

def welcome():
    komunikat="Witaj w koderze ROT-13"
    spaces=0
    for chars in range(len(komunikat)):
        if komunikat[chars]==' ':
            spaces+=1
    print("="*(len(komunikat)+spaces+1))
    print("=",komunikat,"=")
    print("="*(len(komunikat)+spaces+1))


def menu():
    print("Wybierz plik, który chcesz zakodować! ")
    file_path=choose_file()
    f = open (file_path, "r")
    f_content=(f.read())
    

    decision=int(input(' Aby zakodować tekst wpisz 1\n Aby odkodować tekst wpisz 2 \n'))
    if (decision==1):
        textInputEncrypt=f_content
        print('Tekst wejściowy: ', textInputEncrypt)
        print('Tekst zaszyfrowany: ', Encrypt(textInputEncrypt),'\n')
    elif (decision==2):
        textInputDecrypt=f_content
        print('Tekst wejściowy: ', textInputDecrypt)
        print('Odszyfrowany tekst: ', Decrypt(textInputDecrypt),'\n')
    else:
        print('Wybierz 1 lub 2!')
    f.close()
    return 0

def Encrypt(textInputEncrypt):
    textEncrypted=''
    for i in range(len(textInputEncrypt)):
        if  123 > (ord(textInputEncrypt[i])) > 122-13:    #szyfrowanie malych liter x y z
            newSign=chr(ord(textInputEncrypt[i])+13-26)
            textEncrypted+=newSign
        elif 96 < (ord(textInputEncrypt[i])) < 123-13:    #szyfrowanie wszystkich malych liter                                   
            newSign=chr(ord(textInputEncrypt[i])+13)
            textEncrypted+=newSign
        elif  91 > (ord(textInputEncrypt[i])) > 90-13:    #szyfrowanie duzych liter XYZ
            newSign=chr(ord(textInputEncrypt[i])+13-26)
            textEncrypted+=newSign
        elif 64 < (ord(textInputEncrypt[i])) < 91-13:     #szyfrowanie wszystkich duzych liter                                   
            newSign=chr(ord(textInputEncrypt[i])+13)
            textEncrypted+=newSign
        elif (ord(textInputEncrypt[i])) == 32:            #szyfrowanie spacji                                 
            newSign=chr(ord(textInputEncrypt[i]))
            textEncrypted+=newSign
    f_encrypted=open(r"./encrypted_file.txt", "w")
    f_encrypted.write(textEncrypted)
    f_encrypted.close()
    return textEncrypted

def Decrypt(textInputDecrypt):
    textDecrypted=''
    for i in range(len(textInputDecrypt)):
        if 96 < (ord(textInputDecrypt[i])) < (97+13):         #deszyfrowanie malych liter a b c
            newSign=chr(ord(textInputDecrypt[i])+26-13)
            textDecrypted+=newSign
        elif 96+13 < (ord(textInputDecrypt[i])) < 123:        #deszyfrowanie wszystkich malych liter
            newSign=chr(ord(textInputDecrypt[i])-13)
            textDecrypted+=newSign
        elif 64 < (ord(textInputDecrypt[i])) < (65+13):       #deszyfrowanie duzych liter A B C
            newSign=chr(ord(textInputDecrypt[i])+26-13)
            textDecrypted+=newSign
        elif 64+13 < (ord(textInputDecrypt[i])) < 91:         #deszyfrowanie wszystkich duzych liter
            newSign=chr(ord(textInputDecrypt[i])-13)
            textDecrypted+=newSign
        elif (ord(textInputDecrypt[i])) == 32:                #deszyfrowanie spacji                                 
            newSign=chr(ord(textInputDecrypt[i]))
            textDecrypted+=newSign
    f_dencrypted=open(r"./decrypted_file.txt", "w")
    f_dencrypted.write(textDecrypted)
    f_dencrypted.close()
    return textDecrypted
welcome()
menu()

end=input("Aby zakonczyc wcisnij enter")