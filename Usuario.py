from datetime import datetime, timedelta

usuarios = []

class Usuario:
    def __init__(self, nome, matricula):
        self.nome = nome.strip()
        self.matricula = matricula.strip()

    def __str__(self):
        return f"{self.nome} ({self.matricula})"
    