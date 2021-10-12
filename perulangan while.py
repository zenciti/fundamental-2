"""
program perulangan baca buku dengan while
"""


jumlah_buku = 10
jumlah_baca = 0

print( "ibu berkata, baca semua bukumu")

jumlah_paham = 0

print(f"jumlah buku yg dibaca dan dipahami = {jumlah_paham}")
while jumlah_baca < jumlah_buku * 2 :
    jumlah_baca = jumlah_baca + 1
    if jumlah_paham == 9:
        print(f"buku ke- {jumlah_paham + 1} belum dipahami")
    else:
        jumlah_paham = jumlah_paham + 1
        print(f"buku ke- {jumlah_paham} sudah dibaca dan dipahami")

print(f"jumlah buku yang dibaca dan dipahami {jumlah_paham}")
if jumlah_paham == jumlah_buku:
    print('"BU, semua buku sudah dibaca dan dipahami"')
else:
    print(f'"Bu, tidak semua buku bisa dipahami, '
          f'saya hanya bisa memahami {jumlah_paham} buku"')

