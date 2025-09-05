SZEKEK_SZAMA = 10
szekek = ["🟢"]*SZEKEK_SZAMA

loop = 0

while loop == 0:
    melyik_szekek = input(f"Melyik széket szeretnéd lefoglalni? (1-{SZEKEK_SZAMA}) Írd be hogy 'kilép' a kilépéshez.\n>")
    if melyik_szekek == "kilép":
        loop = 1
    try:
        int_szek = int(melyik_szekek)-1

        if not 0 <= int_szek < SZEKEK_SZAMA:
            raise Exception
        szekek[int_szek] = "🔴"
        print(szekek)
    except (ValueError, TypeError, Exception):
        print(f"Helytelen érték! Csak számok 1-{SZEKEK_SZAMA}ig")
