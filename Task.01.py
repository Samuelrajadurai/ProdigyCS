
letters = 'abcdefghijklmnopqrstuvwxyz'
num = len(letters)

def encrypt(plaintext, key ):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if not letter == '':
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = index + key
                if new_index >= num:
                    new_index -= num
                ciphertext += letters[new_index]
    return ciphertext 

def decrypt(ciphertext, key ):
    plaintext = ' '
    for letter in ciphertext:
        letter = letter.lower()
        if not letter == '':
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = index - key
                if new_index < 0:
                    new_index += num
                plaintext += letters[new_index]
    return plaintext

print()
print(" Caesar Cipher Program")
print("Encrypt or Decrypt")
code = input().lower()
print()

if code == 'e':
    key = int(input("Enter Key: "))
    text = input("Enter text to be Encrypted: ")
    ciphertext = encrypt(text,key)
    print(f'CIPERTEXT: {ciphertext}')

elif code == 'd':
    key = int(input("Enter the Key: "))
    text = input("Enter the text to be Decrypted: ")
    plaintext = decrypt(text,key)
    print(f'PLAINTEXT: {plaintext}')

