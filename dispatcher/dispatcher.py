from functools import singledispatch

class Amarelo:
    ...

class Verde:
    ...

class Roxo:
    ...

@singledispatch
def paul(evento):
    ...

@paul.register(Roxo)
def mandar_para_centauro(evento):
    print('Centauro recebeu a cor roxa')

@paul.register(Amarelo)
def mandar_para_fausto(evento):
    print('Fausto recebeu a cor amarela')

# Uma situação na qual o type do python faz algo
@paul.register
def mandar_para_unicornio(evento: Verde):
    print('Unicornio recebeu a cor verde')


paul(Verde())