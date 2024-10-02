import time
import os

def shell_sort(arr, file):
    n = len(arr)
    gap = n // 2 # Inicializa o "gap", metade do tamanho da lista

    # Diminui o gap até que ele seja 0
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            # Faz a ordenação por inserção modificada
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        frase = f"O valor do incremento eh  {gap} e  o estado atual da sequencia eh:  {arr} \n"
        file.write(frase)
        gap //= 2



path = "entrada1.txt"

try:
    with open (path, ) as file:
        out_file =  open("saida1.txt", "w")
        sequencia = file.readline()
        while sequencia:
            sequencia = sequencia.split()
            shell_sort(sequencia,out_file)
            out_file.write("\n")
            sequencia = file.readline()
        
        out_file.close()
        
except FileNotFoundError:
    print("Não achamos o file")



