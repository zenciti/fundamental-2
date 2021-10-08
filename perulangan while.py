"""
program perulangan baca buku dengan while
"""


jumlah_buku = 100
print( "ibu berkata, baca semua bukumu")

jumlah_buku_yg_sudah_dibaca = 0

print(f"jumlah buku yg dibaca = {jumlah_buku_yg_sudah_dibaca}")
while jumlah_buku_yg_sudah_dibaca < jumlah_buku :
    jumlah_buku_yg_sudah_dibaca = jumlah_buku_yg_sudah_dibaca + 1
    print(f"buku ke- {jumlah_buku_yg_sudah_dibaca} sudah dibaca")

print(f"jumlah buku yang dibaca {jumlah_buku_yg_sudah_dibaca}")
