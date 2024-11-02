import unittest
from src.main import Camelô


class TestCamelo(unittest.TestCase):

    def setUp(self):
        # Inicializa uma instância da classe Camelô antes de cada teste
        self.camelo = Camelô()
        self.camelo = Camelô(modo_teste=True)  # Inicia em modo de teste

    def test_inicializacao_camelo(self):
        """Verifica se a inicialização do Camelô está correta."""
        self.assertEqual(self.camelo.totalCompra, 0.0)
        self.assertEqual(self.camelo.carrinho, [])

    def test_adicionar_carrinho_valido(self):
        """Testa a adição de um produto válido ao carrinho."""
        self.camelo.adicionar_carrinho(
            1)  # Produto ID 1: 'Iphone 75 Pro Max' - 750.0
        self.assertEqual(len(self.camelo.carrinho), 1)
        self.assertEqual(self.camelo.carrinho[0]['nome'], 'Iphone 75 Pro Max')
        self.assertEqual(self.camelo.totalCompra, 750.0)

    def test_adicionar_carrinho_multiplos_produtos(self):
        """Testa a adição de vários produtos ao carrinho."""
        self.camelo.adicionar_carrinho(1)  # 'Iphone 75 Pro Max'
        self.camelo.adicionar_carrinho(4)  # 'Camisa Naique'
        self.camelo.adicionar_carrinho(7)  # 'Pai Pobre, Pai Pobre'
        self.assertEqual(len(self.camelo.carrinho), 3)
        self.assertEqual(self.camelo.totalCompra,
                         750.0 + 50.0 + 30.0)  # Soma dos preços

    def test_adicionar_carrinho_invalido(self):
        """Tenta adicionar um produto inexistente ao carrinho."""
        self.camelo.adicionar_carrinho(99)  # ID inexistente
        self.assertEqual(len(self.camelo.carrinho), 0)
        self.assertEqual(self.camelo.totalCompra, 0.0)

    def test_ver_carrinho_com_produtos(self):
        """Testa a visualização do carrinho com produtos."""
        self.camelo.adicionar_carrinho(
            5)  # 'Calça Angelical do Free Fire' - 5000.0
        self.camelo.adicionar_carrinho(6)  # 'Tênis Jordão' - 65.0
        self.assertEqual(len(self.camelo.carrinho), 2)
        self.assertEqual(self.camelo.carrinho[0]['nome'],
                         'Calça Angelical do Free Fire')
        self.assertEqual(self.camelo.carrinho[1]['nome'], 'Tênis Jordão')

    def test_ver_carrinho_vazio(self):
        """Verifica a saída quando o carrinho está vazio."""
        self.assertEqual(len(self.camelo.carrinho), 0)
        self.camelo.ver_carrinho()

    def test_finalizar_compra_com_produtos(self):
        """Testa a finalização da compra com produtos no carrinho."""
        self.camelo.adicionar_carrinho(3)  # 'BJL' - 80.0
        self.camelo.adicionar_carrinho(8)  # 'Quem Pensa Empobrece' - 230.0
        self.camelo.finalizar_compra()
        self.assertEqual(self.camelo.totalCompra, 80.0 + 230.0)

    def test_finalizar_compra_vazia(self):
        """Testa a finalização da compra com o carrinho vazio."""
        self.camelo.finalizar_compra()
        self.assertEqual(self.camelo.totalCompra, 0.0)

    def test_adicionar_produto_id_negativo(self):
        """Tenta adicionar um produto com ID negativo."""
        self.camelo.adicionar_carrinho(-1)
        self.assertEqual(len(self.camelo.carrinho), 0)
        self.assertEqual(self.camelo.totalCompra, 0.0)

    def test_adicionar_produto_id_nao_numerico(self):
        """Tenta adicionar um produto com ID não numérico."""
        with self.assertRaises(TypeError):
            self.camelo.adicionar_carrinho("um")  # Deve levantar um TypeError

    def test_adicionar_mesmo_produto_multiplas_vezes(self):
        """Adiciona o mesmo produto várias vezes."""
        self.camelo.adicionar_carrinho(2)  # PeraBook M1
        self.camelo.adicionar_carrinho(2)
        self.camelo.adicionar_carrinho(2)
        self.assertEqual(len(self.camelo.carrinho), 3)
        self.assertEqual(self.camelo.totalCompra, 1600.0 * 3)  # Preço somado

    def test_adicionar_produto_id_zero(self):
        """Tenta adicionar um produto com ID zero."""
        self.camelo.adicionar_carrinho(0)
        self.assertEqual(len(self.camelo.carrinho), 0)
        self.assertEqual(self.camelo.totalCompra, 0.0)

    def test_adicionar_produto_id_extremamente_grande(self):
        """Tenta adicionar um produto com um ID muito grande."""
        self.camelo.adicionar_carrinho(999999999999)
        self.assertEqual(len(self.camelo.carrinho), 0)
        self.assertEqual(self.camelo.totalCompra, 0.0)

    def test_adicionar_remover_e_adicionar_novamente(self):
        """Testa a adição, remoção e nova adição de produtos ao carrinho."""
        self.camelo.adicionar_carrinho(1)  #  (Iphone 75 Pro Max)
        self.camelo.adicionar_carrinho(2)  # (PeraBook M1)
        self.assertEqual(len(self.camelo.carrinho), 2)
        self.assertEqual(self.camelo.totalCompra, 2350.0)  # Total
        self.camelo.remover_carrinho(2)  # Remove (PeraBook M1)
        self.assertEqual(len(self.camelo.carrinho), 1)
        self.assertEqual(self.camelo.totalCompra,
                         750.0)  # Total deve ser igual ao Iphone
        self.camelo.adicionar_carrinho(3)  # Adiciona (BJL)
        self.assertEqual(len(self.camelo.carrinho), 2)
        self.assertEqual(self.camelo.totalCompra, 830.0)  # Total Iphone + BJL


if __name__ == "__main__":
    unittest.main()
