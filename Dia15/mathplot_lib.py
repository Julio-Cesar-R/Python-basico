# Importamos el módulo de Matplotlib como plt
import matplotlib.pyplot as plt
x=list(range(101))
y=[]
for n in x:
    y.append(n**2)
print(y)
print(x)
fig,ax=plt.subplots()
print(ax.plot(x,y))





