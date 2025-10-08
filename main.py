SZEKEK_SZAMA = 10
szekek = ["🟢"]*SZEKEK_SZAMA

loop = True

while loop:
    melyik_szekek = input(f"Melyik széket szeretnéd lefoglalni? (1-{SZEKEK_SZAMA}) Írd be hogy 'kilép' a kilépéshez.\n>")
    if melyik_szekek == "kilép":
        loop = False
    else:
        try:
            int_szek = int(melyik_szekek)-1

            if not 0 <= int_szek < SZEKEK_SZAMA:
                raise 
            szekek[int_szek] = "🔴"
            print(szekek)
        except:
            print(f"Helytelen érték! Csak számok 1-{SZEKEK_SZAMA}ig")
