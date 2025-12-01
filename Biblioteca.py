import csv
import os

ARQUIVO = "biblioteca.csv"


def carregar_livros():
    """Lê o arquivo CSV e carrega os dados em uma lista de dicionários."""
    livros = []
    if not os.path.exists(ARQUIVO):
        print(f"Arquivo {ARQUIVO} não encontrado. Criando um novo...")
        with open(ARQUIVO, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["titulo", "autor", "ano", "genero", "disponibilidade"])

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for linha in reader:
            livros.append(linha)

    return livros


def salvar_livros(livros):
    """Salva a lista de livros no arquivo CSV."""
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as f:
        campos = ["titulo", "autor", "ano", "genero", "disponibilidade"]
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(livros)


def listar_livros(livros):
    print("\n===== LISTA DE LIVROS =====")
    for i, livro in enumerate(livros, 1):
        print(f"{i}. {livro['titulo']} | {livro['autor']} | {livro['ano']} | {livro['genero']} | {'Disponível' if livro['disponibilidade']=='sim' else 'Emprestado'}")


def buscar_livros(livros):
    termo = input("Digite o termo de busca (título/autor/gênero): ").lower()
    resultados = [
        livro for livro in livros
        if termo in livro["titulo"].lower()
        or termo in livro["autor"].lower()
        or termo in livro["genero"].lower()
    ]

    if resultados:
        print("\n===== RESULTADOS DA BUSCA =====")
        for livro in resultados:
            print(f"{livro['titulo']} - {livro['autor']} ({livro['ano']}) - {livro['genero']} - {livro['disponibilidade']}")
    else:
        print("Nenhum livro encontrado.")


def registrar_emprestimo(livros):
    listar_livros(livros)
    indice = int(input("\nSelecione o número do livro para emprestar: ")) - 1

    if livros[indice]["disponibilidade"] == "não":
        print("O livro já está emprestado!")
    else:
        livros[indice]["disponibilidade"] = "não"
        print("Empréstimo registrado com sucesso!")


def registrar_devolucao(livros):
    listar_livros(livros)
    indice = int(input("\nSelecione o número do livro para devolver: ")) - 1

    if livros[indice]["disponibilidade"] == "sim":
        print("O livro já está disponível!")
    else:
        livros[indice]["disponibilidade"] = "sim"
        print("Devolução registrada com sucesso!")


def adicionar_livro(livros):
    print("\n===== ADICIONAR NOVO LIVRO =====")
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = input("Ano: ")
    genero = input("Gênero: ")

    novo = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "genero": genero,
        "disponibilidade": "sim"
    }

    livros.append(novo)
    print("Livro adicionado com sucesso!")


def menu():
    livros = carregar_livros()

    while True:
        print("""
===== MENU BIBLIOTECA =====
1 - Listar todos os livros
2 - Buscar livros
3 - Registrar empréstimo
4 - Registrar devolução
5 - Adicionar livro
6 - Salvar alterações
0 - Sair
""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_livros(livros)
        elif opcao == "2":
            buscar_livros(livros)
        elif opcao == "3":
            registrar_emprestimo(livros)
        elif opcao == "4":
            registrar_devolucao(livros)
        elif opcao == "5":
            adicionar_livro(livros)
        elif opcao == "6":
            salvar_livros(livros)
            print("Alterações salvas!")
        elif opcao == "0":
            salvar_livros(livros)
            print("Saindo e salvando alterações...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
