spam = ['hello', 'hi' , 'howdy', 'heyas']
test = spam.index('hi')
print test
spam.append('Hey')
print spam
spam.insert(1, 'Yoo')
print spam
spam.sort(key=str.lower)
print spam
print(list('Hello'))

name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:len(name)]
print(name)
print(newName)


def eggs(someParameter):
    someParameter.append('Hello')

spam = [1,2,3]
eggs(spam)
print(spam)
