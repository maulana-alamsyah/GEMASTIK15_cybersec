#!usr/bin/python3

#fungsi logika enkripsine
def encrypt(plaintext):
    plaintext = plaintext[::-1]   #sg kiye nggo membalikan inputan
    ciphertext = "" #kiye variabel kosong nggo nampung hasile
    for i in plaintext: #perulangan sesuai panjang plaintext
        copy = "X" * ((ord(i) ^ 0x50) + 9) #huruf diubah menjadi unicode kemudia di shift 0x50 trus ditambah 9 trush hasile dikali string X
        copy += "-" #ditambahi '-' ng akhir 
        ciphertext += copy #trus dimasukkan ke variabel ciphertext
        #print(ciphertext)
    return ciphertext

#fungsi logika decrypt membalik logika encrypt
def decrypt():
    f = open("encrypted.txt", "r") #baca isi file encrypted.txt
    encrypted = f.read() #isi dari file encrypted.txt ditampung ng variabel encrypted
    encrypted = encrypted.split("-") #berhubung mau pemisah - antar huruf, encrypted dipecah dadi array pemisahe - [xxxxxxxx, xxxxxxxx
    encrypted.reverse() #terus dibalik kesemula
    plaintext = ""
    for i in encrypted: #perulangan sesuai panjang array encrypted
         if(i != '' and i != 'None'): #kondisi misal isi array ora kosong
               copy = chr((i.count('X')-9) ^ 0x50) #hitung panjang X ana pira terus dikurangi 9 kemudian dishift 0x50 terus diubah ke bentuk character
               plaintext += copy #terus dimasukkan kevariabel plaintext
         print(plaintext)

print ("Jatim Encryptor")
print (decrypt())
