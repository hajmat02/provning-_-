# smamma som 2.7 fast med kommentarer

import math   #importerar en modul

#program som räknar ut Omkrets och area av en cirkel genom att veta radien

radie = float(input("Vad är cirkelns radie: "))

r = radie #gör det personen har skrivit in till r

o = (r * 2) * math.pi #räknar ut omkretsen

a = (r **2) * math.pi #räknar ut arean

print(f"Omkretsen = {o:.3f} Arean = {a:.3f}") #skriver ut svaren