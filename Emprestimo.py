from datetime import datetime, timedelta

emprestimos = []

class Emprestimo:
    def __init__(self, livro, usuario):
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = datetime.now()
        self.data_devolucao = self.data_emprestimo + timedelta(days=14)
        self.devolvido = False

    def __str__(self):
        devolucao = self.data_devolucao.strftime("%d/%m/%Y")
        status = "Devolvido" if self.devolvido else f"Devolver até {devolucao}"
        return f"{self.livro.titulo} → {self.usuario.nome} ({status})"
