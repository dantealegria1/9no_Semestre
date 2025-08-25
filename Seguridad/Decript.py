"""
 ===================================
 Miembros: Dante Alegria y Andrea Balandran
 Objetivo: Desarrollar un sistema que permita
           la desencriptación de un mensaje
           con un alfabeto proporcionado en
          un archivo .txt usando el método Atbash.
===================================
"""
"""
Constantes globales
"""
FILE_PATH = "alphabet.txt"
TEXT = "SVOOL SLD ZIV F"

"""
Lee el alfabeto desde un archivo de texto.
Si no existe, devuelve un alfabeto por defecto.
"""
def read_alphabet(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            alphabet = file.read().strip()
    except FileNotFoundError:
        print(f"[ERROR] El archivo '{file_path}' no fue encontrado.")
        alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    return alphabet

"""
Descifra un mensaje usando el método Atbash.
Invierte el alfabeto y traduce carácter por carácter.
"""
def atbash_decrypt(ciphertext: str, alphabet: str) -> str:
    reversed_alphabet = alphabet[::-1]
    translation_table = str.maketrans(alphabet, reversed_alphabet)
    return ciphertext.translate(translation_table)

"""
Función principal del programa:
- Lee el alfabeto
- Descifra el texto con Atbash
- Imprime el mensaje en claro
"""
def main():
    alphabet = read_alphabet(FILE_PATH)
    ciphertext = TEXT
    plaintext = atbash_decrypt(ciphertext, alphabet)
    print("Decrypted message:", plaintext)


if __name__ == "__main__":
    main()
