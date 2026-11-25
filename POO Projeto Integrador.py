class Livro:
    def __init__(self, titulo, autor, isbn, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = disponivel

    def emprestar(self):
        if self.disponivel == True:
           self.disponivel = False
           print(f"livro emprestado")
        else:
            print("Livro indisponivel")

    def devolver(self):
        self.indisponivel = True
        print("Produto devolvido")