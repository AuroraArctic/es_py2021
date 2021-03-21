import seaborn as sns
import matplotlib.pyplot as plt
import json
with open("new_lista.json", "r") as n:
        new_lista = json.loads(n.read()) # trasforma le tuple in lista
nw = new_lista[:20]
xs = [c[0] for c in nw]
ys = [c[1] for c in nw]

# sns.histplot(x=xs, y=ys)
sns.set_style(style = "whitegrid")
sns.barplot(x=ys, y = xs)#, color = "#414141") #senza colore diversi
plt.xticks(rotation = 90)
# sns.histplot(nw, x=xs, y=ys)
plt.show()