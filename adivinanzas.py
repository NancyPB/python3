ns=6
num=int(input("introduce un numero entre 0 y 10, te dire si adivinaste o te asecaste al numero secreto:"))
if num>ns:
    print("el numero secreto es menor a este, intentalo nuevamente")
elif num==ns:
    print("adivinaste, el numero secreto es",ns)
    