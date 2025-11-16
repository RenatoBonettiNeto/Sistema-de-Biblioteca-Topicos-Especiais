from datetime import datetime
class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True
    
    def __str__(self):
        return f"{self.titulo} ({self.ano}) - {self.autor} | Disponivel: {self.disponivel}"
    
class Usuario:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - Matricula: {self.matricula}"

class Emprestimo:
    def __init__(self, livro, usuario):
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = datelime.now().date()
        self.data_devolucao = None

    def devolver(self):
        self.data_devolucao = datetime.now().date()
        self.livro.disponivel = True

    def __str__(self):
        return (
            f"Livro: {self.livro.titulo} | Usuário: {self.usuario.nome} | "
            f"Empréstimo: {self.data_emprestimo} | Devolução: {self.data_devolucao}"
        )