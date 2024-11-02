class Camelô:

    def __init__(self, modo_teste=False):
        # totalCompra guarda os gastos das compras.
        # carrinho armazena os produtos que foram adicionados ao carrinho.
        self.totalCompra = 0.0
        self.carrinho = []
        self.modo_teste = modo_teste

    # Essa parte é muito estranha. Basicamente a gente criou um dicionário que dentro possui um dicionário e que dentro possui outros dicionários.
    # Tudo isso foi feito pra armazenar os produtos do Camelô do Mendes.
    # A gente não sabia que tinha como fazer isso e nós só descobrimos por causa do chat gpt.
    produtos = {
        'Eletronicos': {
            1: {
                'nome': 'Iphone 75 Pro Max',
                'preco': 750.0
            },
            2: {
                'nome': 'PeraBook M1 ',
                'preco': 1600.0
            },
            3: {
                'nome': 'BJL',
                'preco': 80.0
            },
        },
        'Roupas': {
            4: {
                'nome': 'Camisa Naique',
                'preco': 50.0
            },
            5: {
                'nome': 'Calça Angelical do Free Fire',
                'preco': 5000.0
            },
            6: {
                'nome': 'Tênis Jordão',
                'preco': 65.0
            },
        },
        'Livros': {
            7: {
                'nome': 'Pai Pobre, Pai Pobre',
                'preco': 30.0
            },
            8: {
                'nome': 'Quem Pensa Empobrece',
                'preco': 230.0
            },
            9: {
                'nome': 'As 48 Leis do Fracasso',
                'preco': 115.0
            },
        }
    }

    # Esse método serve pra mostrar os produtos da loja.
    # Por conta do dicionário que a gente fez nós tivemos que fazer 2 loops para mostrar os produtos.
    def mostrar_produtos(self):
        print("""
      Produtos Disponíveis:
      """)
        # Esse loop acha as categorias 'Eletrônicos', 'Roupas' e 'Livros' e os dicionários dentro deles.
        for categoria, itens in self.produtos.items():
            print(categoria + ":")
            # Esse loop aqui encontra os produtos dentro dos dicionários que possuem os produtos. O índice é a chave e o item é um dicionário que possui as informações dos produtos.
            for indice, item in itens.items():
                print(f"{indice} - {item['nome']} - R$ {item['preco']:}")
            print()  # Isso é só pra dar um espaço.

# Esse método serve para armazenar os produtos na lista carrinho e somar os preços dos produtos no atributo totalCompra.

    def adicionar_carrinho(self, numero=None):
        if numero is None:
            numero = int(
                input(
                    "Qual o número do produto que deseja adicionar ao carrinho? : "
                ))
        if numero < 0:
            return "ID inválido"

        for categoria, itens in self.produtos.items():
            if numero in itens:
                produto = itens[numero]
                self.totalCompra += produto['preco']
                self.carrinho.append(produto)
                print(f"Produto adicionado: {produto['nome']}")
                return
        print("Produto não encontrado.")

# Esse método serve para mostrar os itens escolhidos no carrinho.

    def ver_carrinho(self):
        print("""
      Carrinho de Compras:
      """)

        # Se o carrinho de compras tiver algum item ele vai iniciar o loop para mostrar os produtos dentro da lista carrinho.
        if len(self.carrinho) > 0:
            for item in self.carrinho:
                print(f"{item['nome']} - R$ {item['preco']:}")
        else:
            print("O carrinho está vazio.")

# Essa função mostra os custos das compras.

    def finalizar_compra(self):
        print("""
      Finalizando Compra:
      """)

        # Se o carrinho estiver com algo ocorre um loop pra mostrar os prdoutos comprados e mostra o total de gastos.
        if len(self.carrinho) > 0:
            for item in self.carrinho:
                print(f"{item['nome']} - R$ {item['preco']:}")

            print(f"""
          Total da Compra: R$ {self.totalCompra:}
          """)
        else:
            print("Comprou nada? Não volta mais seu pobre miserável!")

# COLOCAR REMOVER PRODUTOS AQUI!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# é uma caixinha pra armazenar a classe Camelô. Serve para o programa principal acionar os métodos da classe.
a = Camelô()

print("""
Bem Vindo ao Camelô do Mendes!
Aqui você encontra os melhores produtos da internet!
Vendemos apenas produtos 'oliginais' importados do Paraguai (Obs: Somos vendedores autorizados).
""")

# Esse é o programa principal. Não tem muito o que dizer a não ser que ele é um loop que irá se repetir toda vez que um método da classe finalizar e só irá parar quando acionar o break.
while True:
    print("""
  Escolha uma opção:

  1- Mostrar produtos disponíveis.
  2- Adicionar produto ao carrinho.
  3- Ver carrinho de compras.
  4- Finalizar compra.
  """)
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        a.mostrar_produtos()
    elif opcao == 2:
        a.adicionar_carrinho()
    elif opcao == 3:
        a.ver_carrinho()
    elif opcao == 4:
        a.finalizar_compra()
        break
    elif opcao == 5:
        a.remover_carrinho(opcao)
    else:
        print("Opção inválida. Por favor, escolha novamente.")
