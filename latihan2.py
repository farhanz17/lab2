#membuat program nilai akhir

nama = input("Masukan Nama : ")
uts = input("Masukan UTS : ")
uas = input("Masukan UAS : ")
tugas = input("Masukan TUGAS : ")

hasil = (int(tugas)*.2) + (int(uts)*.4) + (int(uas)*.4)
keterangan = ("TIDAK LULUS" , "LULUS") [hasil > 60]
if hasil > 80:
    huruf = "A"
elif hasil > 70:
    huruf = "B"
elif hasil > 50:
    huruf = "C"
elif hasil > 40:
    huruf = "D"
else :
    huruf = "E"

print("\nNama", nama)
print("UTS", uts)
print("UAS", uas)
print("Tugas", tugas)
print("HASIL", hasil)
print("HURUF", huruf)
print("UTS", uts)
print("keterangan" , keterangan)




