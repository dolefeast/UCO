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


E=7.0e-1
dx=10**-3
energias=[]
perdidas=[]
distancias=[]
while E>0:
	for i in data:
		if i[0]>E:
			SE=i[1]
			break
	energias.append(E)
	perdidas.append(SE)
	distancias.append(dx)
	dx=dx+10**-3
	E=E-SE*dx
print(energias,perdidas,distancias,sep='\n')
