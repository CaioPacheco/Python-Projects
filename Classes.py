class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return "Nome: %s, Idade: %s" % (self.nome, self.idade)


class Incel(Pessoa):
    def __init__(self, nome, idade, misogenia, virgem = True):
        super().__init__(nome, idade)
        self.misogenia = misogenia
        self.virgem = virgem

    def __str__(self):
        return "Nome: %s, Idade: %s, Misogenia: %s" % (self.nome, self.idade, self.misogenia) + '%' + ', Virgem: %s' % self.virgem


class Lacradora(Pessoa):
    def __init__(self, nome: str, idade: int = 0, lacre: int = 50):
        super().__init__(nome, idade)
        self.lacracao = lacre

    def __str__(self):
        return "Nome: %s, Idade: %s, Lacre: %s" % (self.nome, self.idade, self.lacracao) + '%'


def printcheck_instancia(objeto: object, classe: classmethod):
    if isinstance(objeto, classe):
        return "{} é um {}".format(objeto.nome, str(classe).split("'")[1].split('.')[1])
    else:
        return "{} não é um {}".format(objeto.nome, str(classe).split("'")[1].split('.')[1])


def print_all():
    print('')
    for y in range(len(pessoas)):
            print(pessoas[y])
            print('')

    for x in range(len(classes)):
        for y in range(len(pessoas)):
            print(printcheck_instancia(pessoas[y], classes[x]))
        print('')


Ygona = Lacradora("Ygona", 25, 97)
Bolsonaro = Incel("Bolsonaro", 22, 99)
Caio = Pessoa("Caio", 19)

classes = [Pessoa, Incel, Lacradora]
pessoas = [Ygona, Bolsonaro, Caio]


print_all()

