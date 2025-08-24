# ===================================
# Miembros: Dante Alegria y Andrea Balandran
# Objetivo: Desarrollar un sistema que permita
#           la desencriptación de un mensaje
#           con un alfabeto proporcionado en
#           un archivo .txt usando el método Atbash.
# ===================================

FILE_PATH = "alphabet.txt"
TEXT = "SVOOL SLD ZIV F"


def read_alphabet(file_path: str) -> str:
    """
    Lee el alfabeto desde un archivo de texto.
    Si no existe, devuelve un alfabeto por defecto.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            alphabet = file.read().strip()
    except FileNotFoundError:
        print(f"[ERROR] El archivo '{file_path}' no fue encontrado.")
        alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    return alphabet


def atbash_decrypt(ciphertext: str, alphabet: str) -> str:
    """
    Descifra un mensaje usando el método Atbash.
    Invierte el alfabeto y traduce carácter por carácter.
    """
    reversed_alphabet = alphabet[::-1]
    translation_table = str.maketrans(alphabet, reversed_alphabet)
    return ciphertext.translate(translation_table)


def main():
    """
    Función principal del programa:
    - Lee el alfabeto
    - Descifra el texto con Atbash
    - Imprime el mensaje en claro
    """
    alphabet = read_alphabet(FILE_PATH)
    ciphertext = TEXT
    plaintext = atbash_decrypt(ciphertext, alphabet)
    print("Decrypted message:", plaintext)


if __name__ == "__main__":
    main()
