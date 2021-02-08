class Aninal(object):
    def __init__(self):
        print('Aninaml')
    def eat1(self,name):
        self.name=name
    def cute1(self):
        print('cute1')

class Mammal(Aninal):
    def cute1(self,name):
        print('cute2')

class Bird(Aninal):
    def cute1(self):
        print('cute3')

class Runnable(Aninal):
    def run(self):
        print('we can run')
class Dog(Mammal,Runnable):
    def cute1(self,name):
        print('dog cute')

class Parrot(Bird):
    pass

dog=Dog()
dog.run()
dog.cute1('mike')
dog.eat1('shit')