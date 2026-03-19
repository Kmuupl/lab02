print("Podaj oceny. Aby zakończyć, wpisz 'q'.\n")

punkty_list = []

while True:
    type = input("Podaj punkty: ")
    if type.lower() == "q":
        break
    try:
        punkty = int(type)
        if 0 <= punkty <= 100:
            punkty_list.append(punkty)
        else:
            print("Punkty muszą być w zakresie 0-100 :)")
    except ValueError:
        print("Hej, to nie jest liczbą! :O")

if not punkty_list:
    print("Nie podano ocen.")
else:
    def grade(p):
        if p >= 90:
            return 5
        elif p >= 80:
            return 4
        elif p >= 70:
            return 3
        elif p >= 65:
            return 2
        else:
            return 1


    oceny = []
    for p in punkty_list:
        oceny.append(grade(p))

    srednia = sum(oceny) / len(oceny)

    miimum = oceny[0]
    maximum = oceny[0]
    for o in oceny:
        if o < minimum:
            minimum = o
        if o > maximum:
            maximum = o

        posortowane = sorted(oceny)
        n = len(posortowane)
        if n % 2 == 1:
            mediana = posortowane[n // 2]
        else:
            mediana = (posortowane[n // 2 - 1] + posortowane[n // 2]) / 2

        powyzej_sredniej = 0
        for o in oceny:
            if o > srednia:
                powyzej_sredniej += 1

            wyniki = {
                "liczba_ocen": len(oceny),
                "oceny": oceny,
                "srednia": round(srednia, 2),
                "mediana": mediana,
                "min": minimum,
                "max": maximum,
                "powyżej średniej": powyzej_sredniej

            }

            print("\n==== WYNIKI ====")
            for klucz, wartosc in wyniki.items():
                print(f"{klucz}: {wartosc}")

                print("\n-=== BONUS ===-")
                oceny_comp = [grade(p) for p in punkty_list]
                powyzej_comp = len([o for o in oceny_comp if o > srednia])
                slownik = {p: grade(p) for p in punkty_list}

                wyniki_comp = {
                    "liczba ocen": len(oceny_comp),
                    "oceny": oceny_comp,
                    "średnia": round(sum(oceny_comp) / len(oceny_comp), 2),
                    "mediana": mediana,
                    "min": min(oceny_comp),
                    "max": max(oceny_comp),
                    "powyżej średniej": powyzej_sredniej,
                    "słownik": slownik,
                }

                print("Słownik wyników: ")
                for klucz, wartosc in wyniki_comp.items():
                    print(f"{klucz}: {wartosc}")
