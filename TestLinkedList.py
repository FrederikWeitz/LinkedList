from MyLinkedList import *

lili = LinkedList()
lili.add({'m0': 'gehts?'})

m1 = Member()
m1.setMember({'m1': 17})
lili.add(m1)

lili.printAll()

m2 = Member()
m2.setMember({'m2': 'was zum Spielen'})
lili.add(m2)

lili.add({'m3': 'hurra'})

lili.add_many([{'m4':5},{'m5':6},{'m6':10,'ma':3,'mb':17}])

m3 = Member()
m3.setMember({'m8': 'uff', 'mb': 'hallo', 'mc': 'wie auch immer', 'd': 2018})

lili.add_many([m3,{'m9': 15, 'zwei': -34}])

print()
print('\nAddBehind:')
lili.add_after(pointer={'a': 'Alles frisch?', 'b': 'Oder wie oder was?'}, member=lili.has_at_index(3))
lili.add_after(pointer=m1, member=lili.has_at_index(3))
lili.add_after(pointer=m1, index=0)
lili.add_after(pointer=m1, index=8)
lili.add_after(pointer=m1, index=11)
lili.add({'hallo': 'gehts?'})
lili.printAll()

lili.add_before({'erster':2018},index=0)
lili.add_before(pointer={'a': 'Alles frisch?', 'b': 'Oder wie oder was?'}, member=lili.has_at_index(3))
print()
print('--------------------------------------------------------')
lili.printAll()
