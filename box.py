box=[]
while True:
    print("1-Colocar item")
    print("2-Retirar item")
    print("3-Listar itens")
    print("4- Sair")
    opc=int(input("Digite uma opção: "))

    if opc == 1:
        item= input("Digite o item: ")
        box.append(item)
    elif opc == 2:
        item = input("Digite o item: ")
        if item in box:
         box.remove(item)
        else:
           print("não presente na caixa")
    elif opc == 3:
       print(box)
    elif opc == 4:
       print("Encerrando sistema...")

    else:
       print("Opção invalida")
