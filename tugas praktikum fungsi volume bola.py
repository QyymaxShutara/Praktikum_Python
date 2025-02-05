def bola(r):
    return 4/3 * 3.14 * r**3

r = float(input("masukkan nilai jari jari: "))
volume = bola(r)
print(f"volume bola dengan jari jari {r} adalah {volume}")