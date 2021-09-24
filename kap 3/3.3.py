
betyg = float(input("Vad fick hen för poäng? "))

if betyg >= 51:
    print("50 är max, prova igen")
elif betyg >= 45:
    print("Hen fick A")
elif betyg >= 40:
    print("Hen fick B")
elif betyg >= 35:
    print("Hen fick C")
elif betyg >= 30:
    print("Hen fick D")
elif betyg >= 25:
    print("Hen fick E")
elif betyg <= 24:
    print("Hen fick F")
else:
    print("Ett fel inträffade prova igen")

