import random

names = ['Jon', 'Aaron', 'Kat', 'Kahlah', 'Zach', 'Eric']
f = open("forJon.txt", "w")
name = random.choice(names)
while name == 'Jon':
    name = random.choice(names)
names.remove(name)
f.write(name)
f.close()

f = open("forAaron.txt", "w")
name = random.choice(names)
while name == 'Aaron':
    name = random.choice(names)
names.remove(name)
f.write(name)
f.close()

f = open("forKat.txt", "w")
name = random.choice(names)
while name == 'Kat':
    name = random.choice(names)
names.remove(name)
f.write(name)
f.close()

f = open("forKahlah.txt", "w")
name = random.choice(names)
while name == 'Kahlah':
    name = random.choice(names)
names.remove(name)
f.write(name)
f.close()

f = open("forZach.txt", "w")
name = random.choice(names)
while name == 'Zach':
    name = random.choice(names)
names.remove(name)
f.write(name)
f.close()

f = open("forEric.txt", "w")
name = random.choice(names)
while name == 'Eric':
    name = random.choice(names)
names.remove(name)
f.write(name)
f.close()
