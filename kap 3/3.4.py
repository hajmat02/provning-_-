t = float(input("Yttertemperatur? "))

if t < 18:
    print("Det är lite kallare än sommar")
    print("Ta med en vindjacka")
elif t < 10:
    print("Nu äre kallt")
    print("Ta på en flecejacka under vindjackan")
elif t < 1:
    print("Nu äre satans kallt")
    print("FRAM MED VINDTERKLÄDER!")

else:
    if t > 30:
        print("Satan va varmt")
        print("Ta me isbitar och lev i vattnet under skuggan så du inte dör!!")
    elif t > 25:
        print("Nu äre badväder")
        print("Ta med badkläder")
    elif t > 18:
        print("Nu äre sommar")
        print("Ta med en kofta just in case")