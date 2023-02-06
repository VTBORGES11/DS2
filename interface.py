from repository import codigos

while True:
    codigo_ddd = int(input("Digite o DDD:"))
    found = False
    for ddd in codigos:
        if ddd["codigo"] == codigo_ddd:
            print("A cidade cujo DDD é", codigo_ddd, "é", ddd["cidade"])
            found = True
            break

    if not found:
        print("DDD nao cadastrado")
