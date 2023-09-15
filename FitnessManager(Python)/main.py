from datetime import datetime

def getTime():
    return datetime.now()

do=input("Enter 1 to Log data or 2 to Retrieve data: ")
forWhom=input("Enter 1 for Ani or 2 for AD: ")
forWhat=input("Enter 1 for Exercise or 2 for Diet: ")

if(do=="1"):   #ie. to write/log
    if(forWhom=="1"):
        if(forWhat=="1"):
            filAniExer=open("Ex5filAniExer.txt",mode="a") #append mode because we want to preserve previous data as well 
            AniExer=input("Specify exercise: ") 
            filAniExer.write(str(getTime())+"    ")
            filAniExer.write(AniExer)
            filAniExer.write("\n")
            filAniExer.close()
        else:
            filAniDiet=open("Ex5filAniDiet.txt",mode="a") #append mode because we want to preserve previous data as well 
            AniDiet=input("Specify Diet: ")
            filAniDiet.write(str(getTime())+"    ")
            filAniDiet.write(AniDiet)
            filAniDiet.write("\n")
            filAniDiet.close()
    else:
        if(forWhat=="1"):
            filADExer=open("Ex5filADExer.txt",mode="a") #append mode because we want to preserve previous data as well 
            ADExer=input("Specify exercise: ") 
            filADExer.write(str(getTime())+"    ")
            filADExer.write(ADExer)
            filADExer.write("\n")
            filADExer.close()
        else:
            filADDiet=open("Ex5filADDiet.txt",mode="a") #append mode because we want to preserve previous data as well 
            ADDiet=input("Specify Diet: ") 
            filADDiet.write(str(getTime())+"    ")
            filADDiet.write(ADDiet)
            filADDiet.write("\n")
            filADDiet.close()

#To retrieve data
else:
    if(forWhom=="1"):
        if(forWhat=="1"):
            filAniExer=open("Ex5filAniExer.txt",mode="r")#if we don't specify read that's okay because by default file is open read mode only 
            print(filAniExer.read())
            filAniExer.close()
        else:
            filAniDiet=open("Ex5filAniDiet.txt",mode="r")#if we don't specify read that's okay because by default file is open read mode only 
            print(filAniDiet.read())
            filAniDiet.close()
    else:
        if(forWhat=="1"):
            filADExer=open("Ex5filADExer.txt",mode="r")#if we don't specify read that's okay because by default file is open read mode only 
            print(filADExer.read())
            filADExer.close()
        else:
            filADDiet=open("Ex5filADDiet.txt",mode="r")#if we don't specify read that's okay because by default file is open read mode only 
            print(filADDiet.read())
            filADDiet.close()

