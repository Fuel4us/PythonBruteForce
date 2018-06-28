# coding=utf-8
#Isto é python, é nojento claro. Mas não tinha nada para fazer e ja nao pegava em python aos tempos e basiei me numa cena do reddit xDDD
import random
import time

#criação do array "objectivo"
target_array = list("Boa Viagem suas borregas!")
#tamanho do array para fins de nao repetir código
size_array = len(target_array)
#array a preencher
string_array = [""] * size_array

#se tiver de explicar a incialização de variaveis, nem sei que te faça
i = 0

#Para printar algo para nao achares estupido nao correr logo
print("Demora 5 segundinhos da lhe tempo <3\n")
#dou te a conhecer a classe Time é porreirita
time.sleep(3)

#basicamente um ciclo que corre todos os caracters random até corresponder ao array objectivo
while i < size_array:
    string_array[i] = chr(random.randint(32,126))
    if string_array[i] == target_array[i]:
        i += 1
    print("".join(string_array))
    #experimenta comentar a linha de baixo, YUP os processadores sao rapidos
    time.sleep(.006)

print("\n")
time.sleep(1.5)
print("PS: Diz a tua irma que até a curto\n")
time.sleep(2)
print("Done MUAHAHAHHAHHA\n")
