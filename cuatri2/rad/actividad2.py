from time import sleep
data = []
with open("./data.txt") as openfile:
	for i in openfile:
		j = i.split(" ")
		j.pop()
		for k in range(len(j)):
			j[k] = float(j[k])
		data.append(tuple(j))


"""data es una lista de tuplas de len = 2
donde el primer lugar(0) es la energía
y el segundo(1) es el poder de frenado
asociado."""

"""Material: Boron
"""


E = 0.7
dx = 0.001
dn = 2.37
log = open('./plotdata.dat', 'w+')
log.write('#x	E	dE \n')
x = 0
while E>0:
	for i in data:
		if i[0] > E:
			SE = i[1]
			break
	dE = SE * dx * dn
	log.write(str(x) + ", " + str(E) + ", " + str(dE) + "\n")
	x += dx
	E -= dE
log.write('#x 	E	dE')
log.close()
