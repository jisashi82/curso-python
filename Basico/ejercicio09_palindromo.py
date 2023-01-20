def palindromo(palabra: str):
    # luzazul
    palabra = palabra.replace(" ", "")
    palabra= palabra.lower()
    palabra_invertida = palabra[::-1]

    if palabra == palabra_invertida:
        return True
    else:
        return False


# funcion principal
def main():
    palabra = input("ingrese una palabra: ")
    es_palindromo = palindromo(palabra)

    if es_palindromo == True:
        print(f"la palabra {palabra} es palindromo")
    else:
        print(f"la palabra {palabra} no es palindromo")


# punto de entrada de la aplicacion
if __name__ == "__main__":
    main()
