from dataclasses import dataclass

@dataclass
class User:
    nome : str
    idade : int
    
    
User.nome = str(input("Digite o seu nome: "))
User.idade = int(input("Digiite a idade: "))


print(f"{User.nome} tem {User.idade} anos.")
    