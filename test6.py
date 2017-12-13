test = '''a1
a2 '''
bla = '  blabla'
print (test)

dl=len(test)
print(test.rjust(dl*3,'*'))
bla = bla.strip()
print(bla.center(dl*3, "-"))


a1 = 'Jan'
a2 = 'Kowalski'
a3 = 'M'

dlStr = 'Name %s Surname %s Sex %s' % (a1, a2, a3)
print(dlStr)
