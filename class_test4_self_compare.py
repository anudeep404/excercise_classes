#All about constructor(init)

class Computer:
    
    def __init__(self):
        self.name = 'Anudeep'
        self.age = 32


    def update(self):
        self.age = 30

#Method to compare
    def compare(self,c2):
        if self.age == c2.age:
            return True
        else:
            return False

c1 = Computer()
c1.age = 30
c2 = Computer()

#calling UPDATE method for object c1, "self" is the pointer that is directing the method to specific object.

if c1.compare(c2):
    print("They are same")
else:
    print("They are different")

print(c1.name)
print(c2.name)
