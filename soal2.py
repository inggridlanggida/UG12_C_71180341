test = input("Masukkan Angka: ")
coba = input("Masukkan Angka yang dihitung: ")

jika=0
for b in list (test):
    if b == coba:
        jika = jika+1
print("Angka", coba , "Muncul Sebanyak", jika , "kali")