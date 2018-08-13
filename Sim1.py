import random
day= 0
chickennumber = 1
eggnumber = 0
while (eggnumber < 500):

    birth = random.randint(0,1)
    chickennumber = chickennumber + birth
    eggnumber = eggnumber + chickennumber
    day = day + 1
    print("it is now day " + str(day))
    print("you have " + str(chickennumber) + " chickens")
    print("they have laid eggs. you now have " + str(eggnumber) + " eggs")


print("congratulations. it is now day " + str(day))
print("you have successfully acquired " + str(eggnumber) + " in " + str(day) + " days! nicely done by your " + str(chickennumber) + " chickens!")



