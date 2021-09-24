bredd = float(input("Brevets bredd i mm: "))
längd = float(input("Btevets längd i mm: "))
tjock = float(input("Brevets tjocklek i mm: "))

brev = bredd + längd + tjock

if brev > 900:
    print("FÖR STORT!")
elif brev <= 900:
    print("PERFEKT!")
elif brev < 230:
    print("FÖR LITET!")
