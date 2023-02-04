from repository import codigos

codigo_ddd = int(input("Digite o DDD:"))

for ddd in codigos:
    if ddd.codigo == codigo_ddd:
        print("a cidade cujo DDD é", codigo_ddd,"é", ddd.cidade)
        break
else:
    print("DDD nao cadastrado")