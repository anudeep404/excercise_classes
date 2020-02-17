#Defining a class
class Computer:
#If we need to define multiple variables, we can use the special Method.
#Init gets called automatically, unlike 'config'
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram



#Defining a Method
#Attributes ---> Variables
#Behaviour ----> Methods (Function)

    def config(self):
        print("Config is ", self.cpu, self.ram)

#objects below, these are instantiating class.

com1 = Computer('i5',16)
com2 = Computer('Rayzen 3', 8)


#Universally used syntax
#We are using object itself to call the object.
#It works because, com1 belongs to class Computer and config belongs to it as well.

com1.config()
com2.config()