import math
def kuadrat(x):
    return x**2
hasil= kuadrat(4)
print(hasil)

print("="*10)
print("Lambda")
kuad = lambda x: x**2
hasil = kuad(4)
print(hasil)
print("="*10)

def tambah(x,y):
    return math.sqrt (x**2 + y**2)
hasil= tambah(4,2)
print(hasil)

print("="*10)
print("Lambda")
tamb = lambda x,y: math.sqrt(x**2 + y**2)
hasil = tamb(4,2)
print(hasil)
print("="*10)

def c(*args):
    return sum(args)/len(args)
hasil= c(100,50,30)
print(hasil)

print("="*10)
print("Lambda")
c = lambda *args : sum(args)/len(args)
hasil = c(100,50,30)
print(hasil)

def d(s):
    return "12".join(set(s))
print(d("12"))

print("Lambda")
d = lambda s : "12".join(set(s))
hasil= d(12)
print(hasil)
