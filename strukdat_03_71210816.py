kalimat = input("Masukkan Kalimat: ")
kata = input("Kata yang ingin dicari: ")

break_kalimat = kalimat.split(' ')
dict_kalimat = {}

for i in break_kalimat:
    x = i.lower()
    if x not in dict_kalimat:
        dict_kalimat[x] = 1
    else:
        dict_kalimat[x] = dict_kalimat[x] + 1

print(dict_kalimat[kata.lower()])
