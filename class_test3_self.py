#All about constructor(init)

class Computer:
    
    def __init__(self):
        self.name = 'Anudeep'
        self.age = 32

c1 = Computer()
c2 = Computer()


print(c2.name)
c1.name = 'Sravani'
print(c1.name)
