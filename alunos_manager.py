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
        print("Bem-vindo ao gerenciador de alunos!")
        print("\n1) Listar alunos")
        print("2) Adicionar aluno")
        print("3) Calcular média das notas")
        print("4) Buscar aluno por nome")
        print("5) Editar aluno")
        print("6) Remover aluno")
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
        elif opcao == "3":
          print(f"Média das notas: {calcular_media(alunos):.2f}")
        elif opcao == "4":
            termo = input("Termo de busca: ")
            encontrados = buscar_por_nome(alunos, termo)
            listar_alunos(encontrados)

        elif opcao == "5":
            aluno_id = int(input("ID do aluno a editar: "))
            nome = input("Novo nome (ou Enter para manter): ")
            idade = input("Nova idade (ou Enter para manter): ")
            nota = input("Nova nota (ou Enter para manter): ")
            editar_aluno(alunos, aluno_id,
                 nome if nome else None,
                 int(idade) if idade else None,
                 float(nota) if nota else None)

        elif opcao == "6":
            aluno_id = int(input("ID do aluno a remover: "))
            if remover_aluno(alunos, aluno_id):
                print("Aluno removido.")
            else:
                print("Aluno não encontrado.")


        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()

def calcular_media(alunos):
    if not alunos:
        return 0.0
    return sum(a["nota"] for a in alunos) / len(alunos)
    
def buscar_por_nome(alunos, termo):
    termo = termo.lower()
    return [a for a in alunos if termo in a["nome"].lower()]

def editar_aluno(alunos, aluno_id, nome=None, idade=None, nota=None):
    for a in alunos:
        if a["id"] == aluno_id:
            if nome: a["nome"] = nome
            if idade: a["idade"] = idade
            if nota: a["nota"] = nota
            return True
    return False

def remover_aluno(alunos, aluno_id):
    for i, a in enumerate(alunos):
        if a["id"] == aluno_id:
            del alunos[i]
            return True
    return False

def listar_alunos_aprovados(self):
    """Método adicionado no branch feature/melhorias"""
    aprovados = [aluno for aluno in self.alunos if aluno['media'] >= 7]
    print(f"Total aprovados: {len(aprovados)}")
    return aprovados