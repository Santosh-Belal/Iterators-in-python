mytuple=("Hari","Shyam","Santosh")

myiter=iter(mytuple)

print(next(myiter))

print(next(myiter))

print(next(myiter))

for i in mytuple:

    print(i)

    

class person():

    def __iter__(Self):

        Self.Age=15

        return Self

    

    def __next__(Self):

        x=Self.Age

        Self.Age +=10

        return x

        

Myclass=person()

output =iter(Myclass)

#print(next(output))

#print(next(output))    

#print(next(output))

#print(next(output))

for x in output :

    print(x)

   # break

    
