# fungsi enkripsi pesan
def encryptMessage(key, message):
    # list kosong untuk menampung pesan yang telah dienkripsi
    cipher = ''
    # melakukan iterasi pada setiap karakter dalam pesan
    for char in message:
        # mengenkripsi karakter
        if char.isalpha():
            # mengubah karakter menjadi huruf besar
            char = char.upper()
            # hitung indeks karakter setelah dienkripsi
            charIndex = ord(char) - ord('A')
            charIndex = (charIndex + key) % 26
            # menambahkan karakter yang telah dienkripsi ke dalam cipher
            cipher += chr(charIndex + ord('A'))
        else:
            # menambahkan karakter yang tidak perlu dienkripsi ke dalam cipher
            cipher += char
    # mengembalikan pesan yang telah dienkripsi
    return cipher

# fungsi dekripsi pesan
def decryptMessage(key, message):
    # list kosong untuk menampung pesan yang telah didekripsi
    plain = ''
    # melakukan iterasi pada setiap karakter
    for char in message:
        # mendekripsi karakter
        if char.isalpha():
            # mengubah karakter menjadi huruf besar
            char = char.upper()
            # hitung indeks karakter setelah didekripsi
            charIndex = ord(char) - ord('A')
            charIndex = (charIndex - key) % 26
            # menambahkan karakter yang telah didekripsi ke dalam plain
            plain += chr(charIndex + ord('A'))
        else:
            # menambahkan karakter yang tidak perlu didekripsi ke dalam plain
            plain += char
    # mengembalikan pesan yang telah didekripsi
    return plain

def main():
    while True:
        # key untuk mengenkripsi dan mendekripsi pesan
        key = int(input("Masukkan key untuk mengenkripsi dan mendekripsi pesan: "))
        # Pesan yang akan dienkripsi
        message = input("Masukkan pesan yang akan dienkripsi: ")
        # enkripsi pesan
        cipherText = encryptMessage(key, message)
        print("Enkripsi: ", cipherText)
        # dekripsi pesan
        plainText = decryptMessage(key, cipherText)
        print("Dekripsi: ", plainText)
        # menanyakan untuk melanjutkan program atau tidak
        choice = input("Lanjutkan program? (y/n): ")
        if choice.lower() == 'n':
            break

if __name__ == '__main__':
    main()