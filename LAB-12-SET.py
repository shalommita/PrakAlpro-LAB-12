# Shalommita P.
# 71200640
# LAB 12 SET

# Input
lst=input("List pertama: ").lower()
lst2=input("List kedua: ").lower()

# Proses
print("1. Cek Gabungan dari kedua list\n2. Cek Irisan dari kedua list")
pilih=int(input("Pilihanmu: "))
if pilih==1:
    print("Cek Gabungan dari kedua list")
    set1=set(lst)
    set2=set(lst2)
    gab=set1.union(set2) 
    print(gab)
    print(type(gab))
elif pilih==2:
    print("Cek Irisan dari kedua list")
    sett1=set(lst)
    sett2=set(lst2)
    iris=sett1.intersection(sett2)
    print(iris)
    print(type(iris)) 
else:
    print("Pilihan tidak tersedia. Sialakn cek ulang pilihan Anda.")

# Output berupa tipe data set