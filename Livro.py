from datetime import datetime, timedelta

livros = []

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo.strip()
        self.autor = autor.strip()
        self.ano = ano
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' - {self.autor} ({self.ano}) [{status}]"
    
