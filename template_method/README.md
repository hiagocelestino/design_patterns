# Design Patterns Template Method

Esse design pattern é bem simples, uma classe abstrata descreve um metódo que irá usar outros 
outros métodos, esse outros metódos deveram ser implementados pelas classes que herdarem dessa
classe abstrata.

![UML do Template Method](uml.png "UML Template Method")


# [Design Patterns Hooks](example/hooks.py)

Esse design pattern tem uma pequena alteração em comparação com o template method, ele permite
que existam métodos opcionais na chamada do método implementado na classe abstrata.
