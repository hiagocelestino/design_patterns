from typing import Text

class Pipeline:
    def __init__(self, *filters):
        self.filters = filters
    
    def __call__(self, value):
        final_value = value
        for filter in self.filters:
            final_value = filter(final_value)
        
        return final_value

def limpa_texto(texto: Text):
    return texto.replace('\n', '')

def achar_nome(texto: Text):
    nomes = ('Hiago', 'Matheus')
    final_value = texto
    for nome in nomes:
        final_value = final_value.replace(nome, f'NOME({nome})')
    
    return final_value

texto = "\n\n\n Hiago é um desenvolvedor \n\n\n"

pipe = Pipeline(limpa_texto, achar_nome)

print(pipe(texto))
