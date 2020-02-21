class Dog:
    def __init__(self):
        print('dog needs to be taken out for a walk')

    def hungary(self):
        print('dog needs to be be fed')


class Husky(Dog):
    def __init__(self):
        super().__init__()
        print('Husky needs to be taken out for a walk')

    def hungary(self):
        print('husky need to be fed')

    def bath(self):
        print('husky needs to be bathe')


dog = Husky()
dog.hungary()
dog.bath()
'This is an example of inheritance, the class Husky inherits the function of the parent class Dog'
