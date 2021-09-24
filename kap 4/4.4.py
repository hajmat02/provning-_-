
height = float(input("Höjd? "))

# hh = height * 0.3
# studs = height - hh

stopp = 1
studs = 1

while height > stopp:
    height = height * 0.7
    studs = studs + 1
print(f"Det tar {studs} studs innan bollen stannar")
