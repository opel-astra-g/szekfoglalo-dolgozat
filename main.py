melyik_szek = int(input("Melyik széket szeretnéd lefoglalni? (1-8): "))
while not (1 <= melyik_szek <= 8):
    melyik_szek = int(input("Melyik széket szeretnéd lefoglalni? (1-8): "))

foglaltak = []
i = 0

while i < 8:
    foglaltak.append("🟢")
    i += 1

foglaltak.pop(melyik_szek)
foglaltak.insert(melyik_szek-1, "🔴")

print("🔴 ha szék foglalt, 🟢 ha nem foglalt")
print(foglaltak)

# szünet