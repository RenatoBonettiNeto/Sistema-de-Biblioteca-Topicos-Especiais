from Livro import Livro, livros
from Usuario import Usuario, usuarios
from Emprestimo import Emprestimo, emprestimos
from datetime import datetime, timedelta


def buscar_livro_por_titulo(titulo):
    for i, livro in enumerate(livros):
        if livro.titulo.lower() == titulo.lower():
            return i, livro
    return -1, None


def buscar_usuario_por_matricula(matricula):
    for i, usuario in enumerate(usuarios):
        if usuario.matricula == matricula:
            return i, usuario
    return -1, None


def emprestimo_atual_do_livro(livro):
    for emp in emprestimos:
        if emp.livro == livro and not emp.devolvido:
            return emp
    return None

def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado.")
        return
    print("\n=== LIVROS CADASTRADOS ===")
    for i, livro in enumerate(livros, 1):
        print(f"{i}. {livro}")
    print()


def cadastrar_livro():
    print("\n--- Cadastrar Novo Livro ---")
    titulo = input("Título: ").strip()
    if not titulo:
        print("Título não pode ser vazio!")
        return
    autor = input("Autor: ").strip()
    while True:
        try:
            ano = int(input("Ano de publicação: "))
            break
        except ValueError:
            print("Digite um ano válido!")
    livro = Livro(titulo, autor, ano)
    livros.append(livro)
    print("Livro cadastrado com sucesso!")


def editar_livro():
    listar_livros()
    if not livros:
        return
    titulo = input("Digite o título do livro que deseja editar: ").strip()
    idx, livro = buscar_livro_por_titulo(titulo)
    if idx == -1:
        print("Livro não encontrado!")
        return

    print(f"Livro atual: {livro}")
    novo_titulo = input(f"Novo título (Enter para manter '{livro.titulo}'): ").strip()
    novo_autor = input(f"Novo autor (Enter para manter '{livro.autor}'): ").strip()
    novo_ano = input(f"Novo ano (Enter para manter {livro.ano}): ").strip()

    if novo_titulo:
        livro.titulo = novo_titulo
    if novo_autor:
        livro.autor = novo_autor
    if novo_ano:
        try:
            livro.ano = int(novo_ano)
        except ValueError:
            print("Ano inválido, mantido o anterior.")

    print("Livro atualizado com sucesso!")


def remover_livro():
    listar_livros()
    if not livros:
        return
    titulo = input("Digite o título do livro que deseja remover: ").strip()
    idx, livro = buscar_livro_por_titulo(titulo)
    if idx == -1:
        print("Livro não encontrado!")
        return

    if not livro.disponivel:
        print("Não é possível remover um livro emprestado!")
        return

    livros.pop(idx)
    print("Livro removido com sucesso!")


def cadastrar_usuario():
    print("\n--- Cadastrar Usuário ---")
    nome = input("Nome: ").strip()
    if not nome:
        print("Nome não pode ser vazio!")
        return
    matricula = input("Matrícula: ").strip()
    if not matricula:
        print("Matrícula não pode ser vazia!")
        return
    if buscar_usuario_por_matricula(matricula)[0] != -1:
        print("Já existe um usuário com essa matrícula!")
        return

    usuarios.append(Usuario(nome, matricula))
    print("Usuário cadastrado com sucesso!")


def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    print("\n=== USUÁRIOS CADASTRADOS ===")
    for i, usuario in enumerate(usuarios, 1):
        print(f"{i}. {usuario}")
    print()


def realizar_emprestimo():
    if not livros or not usuarios:
        print("Cadastre pelo menos um livro e um usuário primeiro!")
        return

    listar_livros()
    titulo = input("\nTítulo do livro a emprestar: ").strip()
    idx, livro = buscar_livro_por_titulo(titulo)
    if idx == -1:
        print("Livro não encontrado!")
        return
    if not livro.disponivel:
        print("Este livro já está emprestado!")
        return

    listar_usuarios()
    matricula = input("Matrícula do usuário: ").strip()
    idx_u, usuario = buscar_usuario_por_matricula(matricula)
    if idx_u == -1:
        print("Usuário não encontrado!")
        return

    emprestimo = Emprestimo(livro, usuario)
    emprestimos.append(emprestimo)
    livro.disponivel = False
    print("Empréstimo realizado com sucesso!")
    print(f"Prazo de devolução: {emprestimo.data_devolucao.strftime('%d/%m/%Y')}")


def devolver_livro():
    if not any(not e.devolvido for e in emprestimos):
        print("Não há empréstimos pendentes.")
        return

    print("\n=== EMPRÉSTIMOS ATIVOS ===")
    ativos = [e for e in emprestimos if not e.devolvido]
    for i, emp in enumerate(ativos, 1):
        print(f"{i}. {emp}")

    escolha = input("\nDigite o número do empréstimo a devolver (ou Enter para cancelar): ").strip()
    if not escolha.isdigit():
        return
    num = int(escolha) - 1
    if num < 0 or num >= len(ativos):
        print("Número inválido!")
        return

    emp = ativos[num]
    emp.devolvido = True
    emp.livro.disponivel = True
    print("Livro devolvido com sucesso!")


def listar_emprestimos_por_usuario():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    listar_usuarios()
    matricula = input("\nMatrícula do usuário: ").strip()
    idx, usuario = buscar_usuario_por_matricula(matricula)
    if idx == -1:
        print("Usuário não encontrado!")
        return

    print(f"\n=== LIVROS EMPRESTADOS ATUALMENTE POR {usuario.nome.upper()} ===")
    atuais = [e for e in emprestimos if e.usuario == usuario and not e.devolvido]
    if not atuais:
        print("Nenhum livro emprestado no momento.")
    else:
        for e in atuais:
            print(e)

    print(f"\n=== HISTÓRICO COMPLETO DE EMPRÉSTIMOS DE {usuario.nome.upper()} ===")
    historico = [e for e in emprestimos if e.usuario == usuario]
    if not historico:
        print("Nenhum empréstimo registrado.")
    else:
        for e in historico:
            print(e)
    print()


def menu():
    while True:
        print("=" * 50)
        print("     SISTEMA DE BIBLIOTECA")
        print("=" * 50)
        print("1. Listar livros")
        print("2. Cadastrar livro")
        print("3. Editar livro")
        print("4. Remover livro")
        print("5. Cadastrar usuário")
        print("6. Listar usuários")
        print("7. Realizar empréstimo")
        print("8. Devolver livro")
        print("9. Ver empréstimos de um usuário (com histórico)")
        print("0. Sair")
        print("-" * 50)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_livros()
        elif opcao == "2":
            cadastrar_livro()
        elif opcao == "3":
            editar_livro()
        elif opcao == "4":
            remover_livro()
        elif opcao == "5":
            cadastrar_usuario()
        elif opcao == "6":
            listar_usuarios()
        elif opcao == "7":
            realizar_emprestimo()
        elif opcao == "8":
            devolver_livro()
        elif opcao == "9":
            listar_emprestimos_por_usuario()
        elif opcao == "0":
            print("Até logo! Obrigado por usar o sistema da biblioteca.")
            break
        else:
            print("Opção inválida! Tente novamente.")

        input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    menu()