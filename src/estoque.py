class ErroEstoque(Exception):
    """Exceção personalizada para erros de negócio no Estoque."""
    pass

class Estoque:
    def __init__(self):
        # Dicionário para armazenar o estoque: {'nome_produto': quantidade}
        self.produtos = {}

    def _validar_quantidade(self, quantidade):
        """
        Função interna (prefixo _) para validar se a quantidade é um inteiro positivo.
        Perfeita para teste unitário isolado.
        """
        if not isinstance(quantidade, int) or quantidade <= 0:
            raise ErroEstoque("A quantidade deve ser um número inteiro positivo.")
        return True

    def adicionar_produto(self, nome, quantidade):
        """Adiciona uma quantidade especificada a um produto no estoque."""
        try:
            # 1. Valida a entrada antes de qualquer operação
            self._validar_quantidade(quantidade)
            nome = nome.strip().lower()

            # 2. Adiciona ou atualiza o estoque
            if nome in self.produtos:
                self.produtos[nome] += quantidade
            else:
                self.produtos[nome] = quantidade

            return f"Adicionadas {quantidade} unidades de {nome}."
        except ErroEstoque as e:
            return str(e)

    def remover_produto(self, nome, quantidade):
        """Remove uma quantidade especificada de um produto no estoque."""
        try:
            self._validar_quantidade(quantidade)
            nome = nome.strip().lower()

            if nome not in self.produtos:
                raise ErroEstoque(f"O produto '{nome}' não está cadastrado no estoque.")

            estoque_atual = self.produtos[nome]
            if quantidade > estoque_atual:
                raise ErroEstoque(f"Não há estoque suficiente de '{nome}'. Estoque atual: {estoque_atual}.")

            # 3. Remove do estoque
            self.produtos[nome] -= quantidade
            return f"Removidas {quantidade} unidades de {nome}."
        except ErroEstoque as e:
            return str(e)

    def verificar_estoque(self, nome):
        """Retorna a quantidade em estoque de um produto ou zero se não existir."""
        nome = nome.strip().lower()
        return self.produtos.get(nome, 0)