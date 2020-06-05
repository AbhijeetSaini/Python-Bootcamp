def add(n1, n2):
    return (n1 + n2)


result = add(400, 30)
print(result)


def dog_check(mystring):
    if 'dog' in mystring.lower():
        return 'Yes'
    else:
        return 'No'


re = dog_check('Are you a Dog?')

print(re)

def pig_latin(word):

    first_letter = word[0]

    # check if vowel

    if first_letter in 'aeiou':
        return word + 'ay'
    else:
        return word[1:] + first_letter + "ay"


re = pig_latin('ashiva')
print(re)

def myfunc(*abhi):
    #return 10%of the sum
    return sum(abhi)*0.1
summo = myfunc(24,48, 34, 5, 2, 5, 45, 56)
print(summo)

def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    elif 'veggie' in kwargs:
        print('My veggie of choice is {}'.format(kwargs['veggie']))
    else:
        print('No choice')


myfunc(fruit='apple')
myfunc(veggie='pear')
myfunc(Fruit = 'abs')

def myfunc(*args):
    for num in args:
        if num % 2 == 0:
            return num

myfunc(2, 3, 4, 5)

def myfunc(*args):
    enum = []
    for n in args:
        if n % 2 == 0:
            enum.append(n)
    return enum

summo = myfunc(1, 2, 4, 56)
print(summo)


def myfunc(**kwargs):
    for word in kwarg:
        if count(word) % 2 == 0:
            return word
        else:
            return word

myfunc('abhijeet')

def paper_doll(text):
    b = len(text)
    for i in range(b):
        c = 3*text[0:b]
        return c
re = paper_doll('Hello')
print(re)

x = 25

def printer():
    x = 50
    return x

print(x)

print(printer())

un_list = []
for a in un_list:
    if a not in un_list:
            un_list.append(a)
for a in un_list:
        print(a)

mylist = [1, 2, 4, 6]
myset = set()
print(type(myset))
print(type(mylist))

class Sample():
    pass

mysample = Sample()
print(type(mysample))


class Dog():
    def __init__(self, breed, name, spot):
        self.breed = breed
        self.name = name
        self.spot = spot  #expect boolean
    def bark(self, number):
        print('WOOF! My name is {} and the number is {}'.format(self.name, number))

mydog = Dog(breed = 'Husky', name = 'Brook', spot = 'no-spots')

print(type(mydog))
print(mydog.name + ' is of ' + mydog.breed + ' and have ' + mydog.spot)
print(mydog.bark(4))

class Animal:
    def _init_(self):
        print('Animal Created')

    def _who_am_I(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')


myanimal = Animal()
result1 = myanimal._who_am_I()
result2 = myanimal.eat()

class Dog(Animal):
    def _init_(self):
        Animal._init_(self)
        print("Dog Created")

    def eat(self):
        print('I am a dog and eating')

    def bark(self):
        print('Woof!!')

mydog = Dog()
print(mydog)

result3 = mydog.eat()
result4 = mydog._who_am_I()
result5 = mydog.bark()


##POLYMORPHISM

class Dog():
     def _init_(self, name):
         self.name = name
     def speak(self):
         return self.name + "says WOOF!"

class Dog():
         def _init_(self, name):
             self.name = name

def speak(self):
             return self.name + "says WOOF!"

