Warsztat: Gra w zgadywanie liczb.

Napisz prostą grę w zgadywanie liczb. Komputer musi wylosować liczbę w zakresie 1 – 100. 
Następnie:

Zadać pytanie: "Zgadnij liczbę" i pobrać liczbę z klawiatury.

Sprawdzić, czy wprowadzony napis, to rzeczywiście liczba i w razie błędu wyświetlić 
komunikat "To nie jest liczba", po czym wrócić do pkt. 1

Jeśli liczba podana przez użytkownika jest mniejsza niż wylosowana, wyświetlić 
komunikat "Za mało!", po czym wrócić do pkt. 1.

Jeśli liczba podana przez użytkownika jest większa niż wylosowana, wyświetlić 
komunikat "Za dużo!", po czym wrócić do pkt. 1.

Jeśli liczba podana przez użytkownika jest równa wylosowanej, wyświetlić komunikat 
"Zgadłeś!", po czym zakończyć działanie programu.

    Przykład:
    
    Zgadnij liczbę: cześć
    To nie jest liczba.
    Zgadnij liczbę: 50
    Za mało!
    Zgadnij liczbę: 75
    Za dużo!
    Zgadnij liczbę: 63
    Zgadłeś!


Warsztat: Kostka do gry

W grach planszowych i papierowych RPG używa się wielu rodzajów kostek do gry, nie tylko tych dobrze znanych, sześciennych. Jedną z popularniejszych kości jest np. kostka dziesięciościenna, a nawet stuścienna! Jako że w grach kośćmi rzuca się często, pisanie za każdym razem np. "rzuć dwiema kostkami dziesięciościennymi, a do wyniku dodaj 20" byłoby nudne, trudne i marnowałoby ogromne ilości papieru. W takich sytuacjach używa się kodu "rzuć 2D10+20".

Kod takiej kostki wygląda następująco:
xDy+z

gdzie:

    y – rodzaj kostek, których należy użyć (np. D6, D10),
    x – liczba rzutów kośćmi; jeśli rzucamy raz, ten parametr jest pomijalny,
    z – liczba, którą należy dodać (lub odjąć) do wyniku rzutów (opcjonalnie).

Przykłady:

    2D10+10: 2 rzuty D10, do wyniku dodaj 10,
    D6: zwykły rzut kostką sześcienną,
    2D3: rzut dwiema kostkami trójściennymi,
    D12-1: rzut kością D12, od wyniku odejmij 1.

Napisz funkcję, która:

    przyjmie w parametrze taki kod w postaci stringa,
    rozpozna wszystkie dane wejściowe:
        rodzaj kostki,
        liczbę rzutów,
        modyfikator,
    wykona symulację rzutów i zwróci wynik.

Typy kostek występujące w grach: D3, D4, D6, D8, D10, D12, D20, D100.
Wszystkie zadania rozwiązuj używając wersji 3 Pythona!

Repozytorium z ćwiczeniami zostanie usunięte 2 tygodnie po zakończeniu kursu. Spowoduje to też usunięcie wszystkich forków, które są zrobione z tego repozytorium.