employees = open("sample.txt", "a")

try:
   employeesCount = int(input("çalışan sayısı giriniz: "))

   for i in range(employeesCount):
        employeesInfo = input("çalışan adı-soyadı giriniz:")
        employeesSalary = float(input("çalışan maaş bilgisini giriniz:"))
        employees.write(f"{employeesInfo}, {employeesSalary} \n")
        total = (f"{employeesInfo} {employeesSalary}")
        print(total)

except ValueError:
    print("Ad-Soyad bilgisinde rakam olamaz")
    print("Maaş bilgisinde string ifade olamaz")
finally:
    print("başarılı")

employees.close()

file1 = open("sample.txt","r")
lines = file1.readlines() 
for line in lines:
    print(line)
file1.close()
