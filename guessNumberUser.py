import random
import time
import os
import sys

time.sleep(1)

intervall = int(input("\nSkriv in hur stort intervall du vill gissa i från 0:"))

time.sleep(1)

print(f"Datorn tänker på ett tal mellan 0 och {intervall} du ska ta reda på vilket, du har 5 försök på dig")

time.sleep(3)

dator_tal = random.randint(0, intervall)

gissningsförsök = 5

while True:
    gissning = int(input(f"Gissa ett tal mellan 0 och {intervall}: "))
    if gissningsförsök == 0:
        print("Du har inga försök kvar, du förlorade!")
        break

    if gissning == dator_tal and gissningsförsök > 0:
        print("Rätt gissat!")
        time.sleep(1)
        print("Du klarade spelet!")
        break

    elif gissning < dator_tal:
        print("För lågt gissat!")
        gissningsförsök -= 1
        continue

    elif gissning > dator_tal:
        print("För högt gissat!")
        gissningsförsök -= 1
        continue

    else:
        print(f"Är du dum? Gissa mellan 0 och {intervall}")
        gissningsförsök -= 1
        continue

time.sleep(3)

print("Spela igen? (1/2)")
print("1. Ja")
print("2. Nej")
val = int(input("Skriv in ditt val:"))

if val == 1:
    os.execl(sys.executable, sys.executable, *sys.argv)
    pass

elif val == 2:
    print("Tack för att du spelade!")
    time.sleep(2)
    exit()
