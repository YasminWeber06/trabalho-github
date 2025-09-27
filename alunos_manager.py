def adicionar_aluno(alunos, nome, idade, nota):
    novo_id = len(alunos) + 1
    alunos.append({"id": novo_id, "nome": nome, "idade": idade, "nota": nota})


def listar_alunos(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for a in alunos:
            print(f"ID: {a['id']}, Nome: {a['nome']}, Idade: {a['idade']}, Nota: {a['nota']}")


def menu():
    alunos = []
    while True:
        print("\n1) Listar alunos")
        print("2) Adicionar aluno")
        print("0) Sair")
        opcao = input("Escolha: ")
        if opcao == "1":
            listar_alunos(alunos)
        elif opcao == "2":
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            nota = float(input("Nota: "))
            adicionar_aluno(alunos, nome, idade, nota)
            print("Aluno adicionado.")
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()