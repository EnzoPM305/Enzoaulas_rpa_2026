def cadastrar_colaborador(nome: str, cargo: str, salario: float) -> dict:
    colaborador = {
        "nome": nome,
        "cargo": cargo,
        "salario": salario
    }

    return colaborador


def exibir_colaboradores(lista_colaboradores: list) -> None:
    if not lista_colaboradores:
        print("\nNenhum colaborador cadastrado.")
        return

    print("\n===== LISTA DE COLABORADORES =====")

    for i, colaborador in enumerate(lista_colaboradores, start=1):
        print(f"\nColaborador {i}")
        print(f"Nome: {colaborador['nome']}")
        print(f"Cargo: {colaborador['cargo']}")
        print(f"Salário: R$ {colaborador['salario']:.2f}")