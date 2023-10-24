from abc import ABC, abstractmethod

class AbstractClass(ABC):

    def template_method(self):
        self.step1()
        self.step2()
        self.step3()

    @abstractmethod
    def step1(self):
        ...

    @abstractmethod
    def step2(self):
        ...

    @abstractmethod
    def step3(self):
        ...


class ConcreteClass1(AbstractClass):

    def step1(self):
        print('Do something somehow...1')
    
    def step2(self):
        print('Do something somehow...2')
    
    def step3(self):
        print('Do something somehow...3')


class ConcreteClass2(AbstractClass):

    def step1(self):
        print('Do something another way...1')
    
    def step2(self):
        print('Do something another way...2')
    
    def step3(self):
        print('Do something another way...3')

