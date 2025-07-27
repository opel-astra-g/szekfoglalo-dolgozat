szekek = []
szekek_szama = 8

for i in range(szekek_szama):
    szekek.append("🟢")

print(szekek)

while True:

    melyik_szekek = input(f"Melyik széket szeretnéd lefoglalni? (1-{szekek_szama}) Írd be hogy 'kilép' a kilépéshez.\n>")
    if melyik_szekek == "kilép":
        break
    try:
        int_szek = int(melyik_szekek)-1

        if not 0 <= int_szek < szekek_szama:
            raise ValueError
        szekek.pop(int_szek)
        szekek.insert(int_szek, "🔴")
    except (ValueError, TypeError):
        print(f"Helytelen érték! Csak számok 1-{szekek_szama}ig")
        continue
    print(szekek)