from random import randint


start = input("Välkommen till Häst Quizet, tryck enter för att fortsätta")

info = input('''Du kommer nu får frågor och med de frågorna kommer du ha tre alternativ,
 A B & C. I slutet kommer du att få veta hur många rätt du fick och hur mycket du kan om hästar,
 lycka till!''')

svar = 0

fråga1 = input('''Vad heter färgen på hästen om den är vit?
a: Månstoft
b: Skimmel
c: Vit
 ''')

if fråga1 == "b":
    svar += 1
else:
    svar = svar

fråga2 = input('''Vad heter det man har under sadeln?
a: Shabrak
b: Sadelskydd
c: Sadelmatta
 ''')

if fråga2 == "a":
    svar += 1
else:
    svar = svar

fråga3 = input('''Vad heter en tjej häst?
a: Tik
b: Sto
c: Tacka
 ''')

if fråga3 == "b":
    svar += 1
else:
    svar = svar

fråga4 = input('''Vad heter en kastrerad kill häst?
a: Valack
b: Hingst
c: Hane
 ''')

if fråga4 == "a":
    svar += 1
else:
    svar = svar

fråga5 = input('''Hur gammal blir vanligt vis en häst?
a: 15-20
b: 30-45
c: 20-35
 ''')

if fråga5 == "c":
    svar += 1
else:
    svar = svar



print(f"Nu är quizet slut och du fick {svar} av 5")