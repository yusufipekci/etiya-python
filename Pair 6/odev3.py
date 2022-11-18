lessonCount = int(input("Kaç adet ders notu gireceksiniz?"))

geçilenders=0
kalinanDers= 0
basariliders = []
basarisizders = []

passedExams = 0
failedExams = 0
for i in range(lessonCount):
    lessonExam1 = float(input(f"{i+1}. ders için vize notunuzu giriniz."))
    lessonExam2 = float(input(f"{i+1}. ders için final notunu giriniz."))
    totalExamNote = (lessonExam1 * 0.4) + (lessonExam2 * 0.6)
    if totalExamNote >= 50:
        passedExams += 1
    else:
        failedExams += 1


    if totalExamNote >= 50:
        geçilenders+=1
        basariliders.append(totalExamNote)

    else:
        kalinanDers+=1
        basarisizders.append(totalExamNote)


print(f"Başarılı ders sayısı: {geçilenders} ")
print(f"Kalınan ders sayısı: {lessonCount-geçilenders} ")
print(f"Kalınan derslerin notu :{basarisizders} geçilen derslerin notu: {basariliders}")
