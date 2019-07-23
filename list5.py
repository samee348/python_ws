c = ["PKM","ALN","GLN","NVR","PVR","KM","VP","CS","MCS"]
f = ["PKM","ALN","RMZ","CS","MCS"]
b = ["PKM","ALN","NV","KM","RMV"]

players=[]
players.extend(c)
players.extend(f)
players.extend(b)
u_name=[]
for name in players:
    if name in u_name:
        pass
    else:
        u_name.append(name)
print(u_name) 




