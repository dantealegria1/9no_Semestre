#===================================
# Miembros: Dante Alegria y Andrea Balandran
# Objetivo: Desarrollar un sistema que permita la desencriptacion de un mensaje
# Con un alfabeto proporcionados en un archivo txt. Usando el metodo Atbash
#===================================

#Valores Globales
FILE_PATH = 'alphabet.txt'
TEXT = "SVOOL SLD ZIV F"

#Leemos el archivo deseado, en caso de que no exista usamos un alfabeto por defecto
def Read_Alphabet(file_path):
    try:
        with open(file_path, 'r') as file:
            alphabet = file.read().strip()
    except FileNotFoundError:
        print(f"[ERROR] El archivo '{file_path}' no fue encontrado.")
        alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    return alphabet

#Desencriptamos el texto usando el alfabeto proporcionado
#Como sabemos el metodo Atbash invierte el alfabeto
def Atbash_Decrypt(ciphertext, alphabet):
    reversed_alphabet = alphabet[::-1]
    translation_table = str.maketrans(alphabet, reversed_alphabet)
    return ciphertext.translate(translation_table)

def main():
    alphabet = Read_Alphabet(FILE_PATH)
    ciphertext = TEXT
    plaintext = Atbash_Decrypt(ciphertext, alphabet)
    print("Decrypted message:", plaintext)

if __name__ == "__main__":
    main()