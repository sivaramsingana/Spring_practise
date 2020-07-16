first = "it's me"
First = 'it"s" changed'
FIRST = '"c\'ap"sed'
fruit = "Apple"
fruit1 = "ORANGE"
happy = "super excellent"
checks = first;
sampleinput = input("please provide some input for python")
version =3
print (First)
print (FIRST)
print (fruit.upper() + fruit1.lower()+checks)

print (len(first))

print (happy *3)

print ('I want to learn python {}'.format(version))
print ('{2}{0} {1} '.format('I',"like",'this'))
print ('{0:18} | {1:5}'.format('fruits','quantity'))
print ('{0:8} | {1:<8.2f}'.format('mango',10))


def welcome_learner(sampleinput):
    print ('Hello Welcome to python learning'+sampleinput)

animals = ['man','bear','dog']
print(animals[0:2])
animals.extend(['cow'])
moreanimals = ['cat','tiger']
animals.extend(moreanimals)
print(animals)
animals.insert(2,'horse')
index =0
sorted(animals)
while index<len(animals):
    print(animals[index])
    index += 1

for category in animals:
    print(animals)

try:  
    print (animals.index('rat'))
except:
    print ("No Exception or element not found in the list")

welcome_learner(sampleinput)

contacts = {'jason':'2233','mark':'3344'}

print (contacts['jason'])

contacts['john'] = '4455'
contacts['dan'] = '5566'

print (contacts)
del contacts['dan']
print (contacts)

if ('jason' in contacts.keys()):
    print(contacts['jason'])
    print('3344' in contacts.values())


print ('Hello Sivaram'+first)
print ('Welcome to new world of possibilites')
