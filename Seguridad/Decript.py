"""
 ===================================
 Miembros: Dante Alegria y Andrea Balandran
 Objetivo: Desarrollar un sistema que permita
           la desencriptación de un mensaje
           con un alfabeto proporcionado en
           un archivo .txt usando el método Atbash.
 ===================================
"""

""" Constantes globales: ruta del archivo del alfabeto, texto cifrado con Atbash y texto cifrado con César """
FILE_PATH = "alphabet.txt"
TEXT = "SVOOL SLD ZIV F"
CIFRADO = "KHOOR"


def read_alphabet(file_path: str) -> str:
    """
    Lee el alfabeto desde un archivo de texto.
    - Si el archivo existe: devuelve el contenido como string.
    - Si el archivo no existe: imprime un error y devuelve un alfabeto por defecto.
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
    Descifra un mensaje usando el método Atbash:
    - Invierte el alfabeto original.
    - Construye una tabla de traducción entre alfabeto normal y alfabeto invertido.
    - Traduce cada carácter del mensaje cifrado.
    """
    reversed_alphabet = alphabet[::-1]
    translation_table = str.maketrans(alphabet, reversed_alphabet)
    return ciphertext.translate(translation_table)


def cesar_decrypt(text: str, shift: int) -> str:
    """
    Descifra un mensaje usando el método César:
    - Recorre cada carácter del texto.
    - Si es letra, aplica la fórmula inversa del cifrado César (retrocede posiciones según shift).
    - Si no es letra (espacios, signos), se conserva igual.
    - Devuelve el texto en claro.
    """
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result


def main():
    """
    Función principal del programa:
    1. Carga el alfabeto desde el archivo (o usa el por defecto).
    2. Descifra el texto definido en TEXT con el método Atbash.
    3. Descifra el texto definido en CIFRADO con el método César (desplazamiento = 3).
    4. Imprime ambos resultados en pantalla.
    """
    alphabet = read_alphabet(FILE_PATH)

    ciphertext_atbash = TEXT
    plaintext_atbash = atbash_decrypt(ciphertext_atbash, alphabet)

    ciphertext_cesar = CIFRADO
    plaintext_cesar = cesar_decrypt(ciphertext_cesar, 3)

    print("Mensaje desencriptado (Atbash):", plaintext_atbash)
    print("Mensaje desencriptado (César):", plaintext_cesar)


if __name__ == "__main__":
    main()
