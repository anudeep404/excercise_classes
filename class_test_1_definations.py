#Defining a class
class Computer:

#Defining a Method
#Attributes ---> Variables
#Behaviour ----> Methods (Function)

    def config(self):
        print("i5, 16gb, 1TB")

com1 = Computer()
com2 = Computer()


#since the Method is within a class, we have to call the Method by prefixing it with the class name.
#You also have to pass objects to it, like com1

Computer.config(com1)
#Hey Computer, show me your configuration for com2
Computer.config(com2)

#Universally used syntax
#We are using object itself to call the object.
#It works because, com1 belongs to class Computer and config belongs to it as well.

com1.config()
com2.config()