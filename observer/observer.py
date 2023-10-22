from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

class Observer(ABC):
    @abstractmethod
    def update(self):
        ...

class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state > 5:
            print('ConcreteObserverA: Reacted to the event')

class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state >= 0 or subject._state <= 5:
            print('ConcreteObserverB: Reacted to the event')

class Subject(ABC):

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        ...

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        ...

    @abstractmethod
    def notify(self) -> None:
        ...

    def some_business_logic(self) -> None:
        self._state = randrange(0, 10)
        self.notify()


class ConcreteSubject(Subject):
    _state: int = None
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)
    
    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)
    
    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)


if __name__ == '__main__':
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
