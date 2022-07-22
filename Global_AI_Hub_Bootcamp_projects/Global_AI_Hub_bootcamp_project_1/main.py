import pandas as pd
n = int(input("Enter total no of students:"))
lesson=['Math']
Rollno = []
Name = []
midtermex = []
finalex = []
mean = []
for i in range(n):
    with open("math_exam_results.xls", "a") as ogr:
        rn = input("Enter roll no:")
        nm = input("Enter the student name:")
        mex = int(input("Enter the midterm exam grade:"))
        finex = int(input("Enter the final exam grade:"))
        meanx = round(mex*0.4+finex*0.4)

        Rollno.append(rn)
        Name.append(nm)
        midtermex.append(mex)
        finalex.append(finex)
        mean.append(meanx)

        if (meanx >= 90):
            print("Harf Notu: AA")
        elif (meanx >= 85):
            print("Harf Notu: AB")
        elif (meanx >= 75):
            print("Harf Notu: BA")
        elif (meanx >= 70):
            print("Harf Notu: BB")
        elif (meanx >= 65):
            print("Harf Notu: CB")
        elif (meanx >= 55):
            print("Harf Notu: CC")
        elif (meanx >= 50):
            print("Harf Notu: DC")
        elif (meanx >= 45):
            print("Harf Notu: DD")
        elif (meanx < 45):
            print("Harf Notu: FF")

        print("Ortalama:", +meanx)
        if (meanx < 45):
            sonuc = ("Kaldınız")
        else:
            sonuc = ("Geçtiniz")

        ogr.write(str(rn)+"\t"+str(nm)+"\t"+str(mex)+"\t"+str(finex)+"\t"+str(meanx)+"\t"+str(sonuc)+"\t"+str(lesson)+"\n")
y={"Student_admno":Rollno, "Student_Name":Name, "Midterm":midtermex, "Final":finalex, "Mean":mean, "Result":sonuc, "Lesson":lesson}
z=pd.DataFrame(y)
print(z)


