#student marks,percentage and grade
name = input ("enter student name:")
n=int(input("enter the number of subject "))
total=0
for i in range (1,n+1):
  mark=int(input(f"enter the subject mark{i}:"))
  total+=mark
percentage=total/n
if percentage>=90:
    grade="A+"
    perfomance="outstanding"
elif percentage>=80:
    grade="A"
    perfomance="excellent"
elif percentage>=70:
    grade="B"
    perfomance="very good"
elif percentage>=60:
    grade="C"
    perfomance="good"
elif percentage>=50:
    grede="D"
    perfomance="average"
else:
    grade="E"
    perfomance="need improvement"

print("\n-----academic perfomance------")
print("student name",name)
print("total mark:",total)
print("percentage:",round(percentage,2),"%")
print("grade:",grade)
print("perfomance:",perfomance)


  
