# x = {"name" : "Jeferson"}
# x['nome'] = 'Marcos'
# y = x.copy()
import zero as zero

x = {1,1,2,3,4,5,6,7,8}
y= {10,11,12}
print (x)

z = x.union(y)
x = x.difference(y)

z = x.symmetric_difference(y)
print(z)