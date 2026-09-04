from mod_rh import cadastrar_colaborador, exibir_colaboradores

lista_colaboradores = []

def menu ():
    while True:
        print("Menu:")
        print("1. Cadastrar colaborador")
        print("2. Listar colaboradorres")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            nome = input("Digite o nome do colaborador: ")
            cargo = str(input("Digite o cargo do colaborador: "))
            salario = float(input("Digite o salário do colaborador: "))
            colaborador = cadastrar_colaborador(nome, cargo, salario)
            lista_colaboradores.append(colaborador)
            print("Usuario cadastrado com sucesso!")
        elif escolha == "2":
            exibir_colaboradores(lista_colaboradores)
        elif escolha == "3":
            print("Saindo do menu.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()