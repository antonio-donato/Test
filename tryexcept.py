# x = "ciao"

try:
    print(x)
except NameError:
    print("x non definita")
except:
    print("non è NameError")
finally: #a prescindere dal risultato del try
    print("finally")

print("ciao")
