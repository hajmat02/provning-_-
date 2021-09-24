
års = float(input("Hur mycket kostar ett årskort? "))
bilj = float(input("Hur mycket kostar en biljett? "))
ggr = float(input("Hur många gånget hade du tänkt gå? "))

summa = bilj * ggr

if summa >= års:
    print("Välj ett årskort")
else:
    print("Ta biljettvis")