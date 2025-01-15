#length - menghitung panjang tuple 
panjangtuple = (1, 2, 3, 4)
print("lenght:", len(panjangtuple))

#Concanenation - menggabungkan dua tuple
tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
combined_tup = tup1 + tup2 
print("contatination:", combined_tup )

#reperation = mengulang elemen tuple 
reperetiontup = ('halo!') * 4 
print("reperetion:", reperetiontup)

#membership - memeriksa apakah elemen ada di dalam list
member = 2 in (1, 2, 3)
print("membership:", member)

#iteration - melakukan iterasi pada list
for x in (1, 2, 3):
    print(x, end= ' ')

#indexing - mengakses elemen berdasarkan indeksnya
L = ('C++', 'java', 'python')
print(L[2])
print(L[-2])

#slicing - mengambil bagian dari index tertentu
list = ('charger', 'ponsel', 'headphone')
print(list[1:])