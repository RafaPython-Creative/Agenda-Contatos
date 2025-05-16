# Lista principal de contatos
contatos = []

# Função 1: Adicionar contato
def adicionar_contato(contatos, nome, telefone, email, favorito=False):
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": favorito
    }
    contatos.append(contato)
    print(f"Contato '{nome}' adicionado com sucesso.")

# Função 2: Listar contatos
def listar_contatos(contatos):
    if not contatos:
        print("Nenhum contato cadastrado.")
    else:
        for i, contato in enumerate(contatos):
            fav = "★" if contato["favorito"] else " "
            print(f"{i+1}. {fav} {contato['nome']} - {contato['telefone']} - {contato['email']}")

# Função 3: Editar contato
def editar_contato(contatos):
    listar_contatos(contatos)
    try:
        indice = int(input("Digite o número do contato que deseja editar: ")) - 1
        if 0 <= indice < len(contatos):
            contatos[indice]["nome"] = input("Novo nome: ")
            contatos[indice]["telefone"] = input("Novo telefone: ")
            contatos[indice]["email"] = input("Novo email: ")
            print("Contato atualizado com sucesso.")
        else:
            print("Contato não encontrado.")
    except ValueError:
        print("Entrada inválida.")

# Função 4: Marcar/Desmarcar como favorito
def marcar_favorito(contatos):
    listar_contatos(contatos)
    try:
        indice = int(input("Digite o número do contato para (des)marcar como favorito: ")) - 1
        if 0 <= indice < len(contatos):
            contatos[indice]["favorito"] = not contatos[indice]["favorito"]
            status = "favorito" if contatos[indice]["favorito"] else "não favorito"
            print(f"Contato marcado como {status}.")
        else:
            print("Contato não encontrado.")
    except ValueError:
        print("Entrada inválida.")

# Função 5: Listar contatos favoritos
def listar_favoritos(contatos):
    favoritos = [c for c in contatos if c["favorito"]]
    if not favoritos:
        print("Nenhum contato favorito.")
    else:
        for i, contato in enumerate(favoritos):
            print(f"{i+1}. ★ {contato['nome']} - {contato['telefone']} - {contato['email']}")

# Função 6: Deletar contato
def deletar_contato(contatos):
    listar_contatos(contatos)
    try:
        indice = int(input("Digite o número do contato que deseja deletar: ")) - 1
        if 0 <= indice < len(contatos):
            nome = contatos[indice]['nome']
            del contatos[indice]
            print(f"Contato '{nome}' deletado com sucesso.")
        else:
            print("Contato não encontrado.")
    except ValueError:
        print("Entrada inválida.")

# Loop principal
while True:
    print("\nAgenda Automática 1.0")
    print("1 - Criar contato")
    print("2 - Listar contatos")
    print("3 - Editar contato")
    print("4 - Marcar/Desmarcar como favorito")
    print("5 - Listar contatos favoritos")
    print("6 - Deletar contato")
    print("7 - Sair")

    escolha = input("Escolha uma opção: ")

#    # Verifica a escolha do usuário
    if escolha == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        adicionar_contato(contatos, nome, telefone, email)
    elif escolha == "2":
        listar_contatos(contatos)
    elif escolha == "3":
        editar_contato(contatos)
    elif escolha == "4":
        marcar_favorito(contatos)
    elif escolha == "5":
        listar_favoritos(contatos)
    elif escolha == "6":
        deletar_contato(contatos)
    elif escolha == "7":
        print("Saindo da agenda...")
        break
    else:
        print("Opção inválida. Tente novamente.")
