class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, nome, preco, quantidade=1):
        if preco < 0 or quantidade <= 0:
            raise ValueError("Preço e quantidade devem ser positivos.")
        for item in self.itens:
            if item["nome"] == nome:
                item["quantidade"] += quantidade
                return
        self.itens.append({"nome": nome, "preco": preco, "quantidade": quantidade})

    def remover_item(self, nome):
        for item in self.itens:
            if item["nome"] == nome:
                self.itens.remove(item)
                return
        raise ValueError("Item não encontrado no carrinho.")

    def show(self):
        return self.itens

    def total(self):
        subtotal = sum(item["preco"] * item["quantidade"] for item in self.itens)
        
        frete = 20.00 if subtotal < 150.00 and subtotal > 0 else 0.00
        return round(subtotal + frete, 2)