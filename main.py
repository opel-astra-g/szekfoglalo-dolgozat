szekek = [1, 2, 3, 4, 5, 6, 7, 8]

melyik_szek = int(input("Melyik széket szeretnéd lefoglalni? (1-8): "))
while not (melyik_szek == 1 or melyik_szek == 2 or melyik_szek == 3 or melyik_szek == 4 or melyik_szek == 5 or melyik_szek == 6 or melyik_szek == 7 or melyik_szek == 8):
    melyik_szek = int(input("Melyik széket szeretnéd lefoglalni? (1-8): "))

foglaltak  = []

i = 0

while 

szekek.pop(melyik_szek-1)

print("🔴 ha szék foglalt, 🟢 ha nem foglalt")
print(szekek)
print(f"{}")