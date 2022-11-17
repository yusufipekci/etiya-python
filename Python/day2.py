#! kullanıcıdan girdi almak
#! karar blokları
#! döngüler
print("2. gün başlangıç")

userInput = input()
print(f"Girilen değer: {userInput}")

#! type conversion
numberStr = "10"
print(type(numberStr))
number = int(numberStr)
print(number + 10)
print(type(number))

userInput = input()
lessonNote = float(userInput)
print(f"Ders notunuz: {lessonNote}")


#indent
# n adet conditiona bağlı karar bloğlu
if lessonNote>50:
    print("Geçtiniz")
elif lessonNote ==50:
    print("Sınırda geçtiniz")
elif lessonNote == 49:
    print("Sınırda kaldınız")
else:
    print("Kaldınız")







# vize = input("Vize:")
# final = input("Final:")
 
# sonuc = int(vize)(0.4) + int(final)(0.6)
# if sonuc>80 and sonuc<100:
#     print("Harf Notu: AA")
# elif sonuc>=70 and sonuc<80:
#     print("Harf Notu: BB")
# elif sonuc>=60 and sonuc<70:
#     print("Harf Notu: CC")
# elif sonuc>=50 and sonuc<60:
#     print("Harf Notu: DD")
# elif sonuc>=0 and sonuc<50:
#     print("Harf Notu: FF")
# print ("Ortalama") 
# print (float(sonuc))

