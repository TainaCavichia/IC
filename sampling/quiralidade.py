import math
arm = []
zig = []
qui = []
darm = []
dzig = []
dqui = []

for i in range(1,81):
    arm.append([i,i])
    zig.append([i,0])
    

def calcula_d(n,m,lista_d):
    termo1 = (math.sqrt(3))/math.pi
    a = 1.418 #ligação C-C em ang
    termo2 = math.sqrt(n**2 + m**2 + n*m)
    d = termo1*a*termo2
    lista_d.append(d)

for i in range(0,80):
    #arm
    n = arm[i][0]
    m = arm[i][1]
    calcula_d(n,m,darm)
    #zig
    n = zig[i][0]
    m = zig[i][1]
    calcula_d(n,m,dzig)
    
def le_lista(lista):
    for i in range(0, len(lista)):
        print(lista[i])

print("CNTs armchair:")
le_lista(arm)
print("Diâmetros armchair:")
le_lista(darm)
print("CNTs zigzag:")
le_lista(zig)
print("Diâmetros zigzag:")
le_lista(dzig)
