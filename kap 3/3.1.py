
minuter = float(input("Hur många minuter ringer du per månad? "))

kostnad = float(input("Hur mycket kostar varje minut? "))

tot = minuter * kostnad

if tot >= 300:
    pris = tot * 0.9

else:
    pris = tot

print(f"Din totala kostnad blir {pris:.2f}")