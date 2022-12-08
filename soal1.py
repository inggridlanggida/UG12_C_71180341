def temukan(kata_terbalik) :
    misal = " "
    for i in kata_terbalik:
        misal = i+ misal
    return misal

kata_terbalik = (input ('Masukkan Kata atau Angka : '))
print(temukan(kata_terbalik))