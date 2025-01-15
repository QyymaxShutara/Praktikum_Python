#length - menghitung panjang list 
panjanglist = [1, 2, 3, 4]
print("lenght:", len(panjanglist))

#Concanenation - menggabungkan dua list 
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2 
print("contatination:", combined_list )

#reperation = mengulang elemen list 
reperetionlist = ['halo!'] * 4 
print("reperetion:", reperetionlist)

#membership - memeriksa apakah elemen ada di dalam list
member = 2 in [1, 2, 3]
print("membership:", member)

#iteration - melakukan iterasi pada list
for x in [1, 2, 3]:
    print(x, end= ' ')

#indexing - mengakses elemen berdasarkan indeksnya
L = ['C++', 'java', 'python']
print(L[2])
print(L[-2])

#slicing - mengambil bagian dari index tertentu
list = ['charger', 'ponsel', 'headphone']
print(list[1:])