from dataclasses import dataclass

@dataclass
class Usuario:
    nome: str
    cpf: str
    email: str
    senha: str
    saldo: float = 0.0

usuarios: list[Usuario] = []

def menu_cadastro():
    while True:
        print("\n===== MENU =====")
        print("1 - Cadastrar cliente")
        print("2 - Login")
        print("0 - Sair")
 
        opcao = input("Escolha uma opção: ").strip()
 
        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            login_cliente()
        elif opcao == "0":
            print("\nEncerrando o sistema...")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

def cadastrar_cliente():
    print("\n--- CADASTRO DE CLIENTE ---")
    nome = input("Nome: ").strip()
    cpf = input("CPF: ").strip()
    email = input("E-mail: ").strip()
    senha = input("Senha: ").strip()
 
    # Validações básicas
    if not nome or not cpf or not email or not senha:
        print("\nErro: todos os campos são obrigatórios.")
        return
 
   
 
    usuario = Usuario(nome=nome, cpf=cpf, email=email, senha=senha)
    usuarios.append(usuario)
    print(f"\nUsuario '{nome}' cadastrado com sucesso!")

def login_cliente():
    print("\n--- LOGIN ---")
    email = input("E-mail: ").strip()
    senha = input("Senha: ").strip()

    for usuario in usuarios:
        if usuario.email == email and usuario.senha == senha:
            print(f"\nLogin bem-sucedido! Bem-vindo, {usuario.nome}.")
            from main import iniciar_banco

            iniciar_banco()
            return True

    print("\nErro: e-mail ou senha incorretos.")
    return False

