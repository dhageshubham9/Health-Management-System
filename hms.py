import datetime


def gettime():
    return datetime.datetime.now()


fun1 = int(input("enter 1 for get and 2 for insert data : "))
print("enter client name id : ")
cn = int(input("1 for Rajesh, 2 for Vivek and 3 for Shyam : "))
fun2 = int(input("select function 1 for diet 2 for exercise : "))
if fun1 == 1:
    if cn == 1:
        if fun2 == 1:
            with open("Rajesh_diet.txt") as rd:
                a = rd.read()
                print(a)
        elif fun2 == 2:
            with open("Rajesh_exercise.txt") as re:
                a = re.read()
                print(a)
    elif cn == 2:
        if fun2 == 1:
            with open("Vivek_diet .txt") as vd:
                a = vd.read()
                print(a)
        elif fun2 == 2:
            with open("Vivek_diet .txt") as ve:
                a = ve.read()
                print(a)
    elif cn == 3:
        if fun2 == 1:
            with open("Shyam_diet.txt") as sd:
                a = sd.read()
                print(a)
        elif fun2 == 2:
            with open("Shyam_exercise.txt") as se:
                a = se.read()
                print(a)
elif fun1 == 2:
    if cn == 1:
        if fun2 == 1:
            value = input()
            with open("Rajesh_diet.txt", "a") as rd:
                rd.write(str([str(gettime())]) + ": " + value)
        elif fun2 == 2:
            value = input()
            with open("Rajesh_exercise.txt", "a") as re:
                re.write(str([str(gettime())]) + ": " + value)
    elif cn == 2:
        if fun2 == 1:
            value = input()
            with open("Vivek_diet .txt", "a") as vd:
                vd.write(str([str(gettime())]) + ": " + value)
        elif fun2 == 2:
            value = input()
            with open("Vivek_exercise.txt", "a") as ve:
                ve.write(str([str(gettime())]) + ": " + value)
    elif cn == 3:
        if fun2 == 1:
            with open("Shyam_diet.txt", "a") as sd:
                sd.write(str([str(gettime())]) + ": " + input())
        elif fun2 == 2:
            with open("Shyam_exercise.txt", "a") as se:
                se.write(str([str(gettime())]) + ": " + input())
    print("update is recorded successfully")
