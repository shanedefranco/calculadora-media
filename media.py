def calcular_media(numeros):
    total = sum(numeros)
    media = total / len(numeros)
    return media

def main():
    numeros = []
    n = int(input("Quantos números você deseja inserir? "))
    
    for i in range(n):
        numero = float(input(f"Digite o {i+1}º número: "))
        numeros.append(numero)
    
    media = calcular_media(numeros)
    print("A média dos números inseridos é:", media)

if __name__ == "__main__":
    main()
