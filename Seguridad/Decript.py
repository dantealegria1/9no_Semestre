"""
 ===================================
 Miembros: Dante Alegria y Andrea Balandran
 Objetivo: Desarrollar un sistema que permita
           la desencriptación de un mensaje
           con un alfabeto proporcionado en
           un archivo .txt usando el método Atbash.
 ===================================
"""

import sys

# Constantes globales: ruta del archivo del alfabeto, texto cifrado con Atbash y César
FILE_PATH = "alphabet.txt"
TEXT = "SVOOL SLD ZIV F"   # Texto cifrado con Atbash
TEXT_CESAR = "KHOOR"       # Texto cifrado con César (HELLO con shift=3)


def read_alphabet(file_path: str) -> str:
    """
    Lee el alfabeto desde un archivo de texto.
    
    - Si el archivo existe: devuelve el contenido como string.
    - Si el archivo no existe: imprime un error y devuelve un alfabeto por defecto.
    
    Esto es útil si queremos usar alfabetos personalizados (por ejemplo, incluir Ñ).
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            alphabet = file.read().strip()
    except FileNotFoundError:
        print(f"[ERROR] El archivo '{file_path}' no fue encontrado.")
        # Alfabeto español por defecto
        alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    return alphabet


def atbash_decrypt(ciphertext: str, alphabet: str) -> str:
    """
    Descifra un mensaje usando el método Atbash.
    
    El método Atbash funciona invirtiendo el alfabeto:
    - A ↔ Z, B ↔ Y, C ↔ X, ...
    
    Pasos:
    1. Genera una versión invertida del alfabeto.
    2. Crea una tabla de traducción con `str.maketrans`.
    3. Reemplaza cada letra del mensaje con su equivalente.
    """
    reversed_alphabet = alphabet[::-1]                   # Alfabeto invertido
    translation_table = str.maketrans(alphabet, reversed_alphabet)  
    return ciphertext.translate(translation_table)       # Traducción carácter por carácter


def cesar_decrypt(text: str, shift: int) -> str:
    """
    Descifra un mensaje usando el método César.
    
    Funcionamiento:
    - El texto cifrado fue creado desplazando cada letra hacia adelante `shift` posiciones.
    - Para descifrar, retrocedemos `shift` posiciones en el alfabeto.
    
    Ejemplo (shift = 3):
    Texto original : HELLO
    Texto cifrado  : KHOOR
    
    Lógica:
    - Recorremos cada carácter:
      - Si es letra: convertimos a código ASCII con `ord(char)`,
        restamos la base (`A` o `a` según mayúscula/minúscula),
        aplicamos la fórmula `(posicion - shift) % 26`
        y volvemos a letra con `chr`.
      - Si no es letra (espacios, números, signos), lo dejamos igual.
    """
    result = ""
    for char in text:
        if char.isalpha():  
            # Determinar si es mayúscula o minúscula
            base = ord('A') if char.isupper() else ord('a')
            
            # Aplicar el corrimiento inverso (retroceder posiciones)
            new_char = chr((ord(char) - base - shift) % 26 + base)
            result += new_char
        else:
            # Mantener espacios, signos, etc.
            result += char
    return result


def main():
    """
    Función principal:
    - Lee el alfabeto desde archivo (o usa el por defecto).
    - Permite pasar textos cifrados desde argumentos o input.
    - Si no se pasa nada, usa los valores por defecto.
    """
    alphabet = read_alphabet(FILE_PATH)

    # Texto Atbash: desde argumento, input o default
    if len(sys.argv) > 1:
        ciphertext_atbash = sys.argv[1].upper()
    else:
        entrada = input("Introduce texto Atbash (Enter para usar default): ").strip()
        ciphertext_atbash = entrada.upper() if entrada else TEXT

    # Texto César: desde argumento, input o default
    if len(sys.argv) > 2:
        ciphertext_cesar = sys.argv[2].upper()
    else:
        entrada = input("Introduce texto César (Enter para usar default): ").strip()
        ciphertext_cesar = entrada.upper() if entrada else TEXT_CESAR

    # Descifrar ambos
    plaintext_atbash = atbash_decrypt(ciphertext_atbash, alphabet)
    plaintext_cesar = cesar_decrypt(ciphertext_cesar, 3)  # shift fijo de 3

    print("Mensaje desencriptado (Atbash):", plaintext_atbash)
    print("Mensaje desencriptado (César):", plaintext_cesar)


if __name__ == "__main__":
    main()

