def is_palindrom(element):
    """
    Functia verifica daca elementul este palindrom
    :param element: numar intreg
    :return: True/False
    """
    if element < 0:
        element = element * -1

    copie = element
    element2 = 0
    while element:
        element2 = element2 * 10 + element % 10
        element = element // 10
    if element2 == copie:
        return True
    else:
        return False


def get_longest_all_palindromes(lista):
    """
    Functia determina cea mai lunga subsecventa formata din elemente palindrom
    :param lista: lista de elemente
    :return: cea mai lunga subsecventa
    """

    subsecventa_maxima = []
    len_subsecventa_curenta = 0
    len_subsecventa_maxima = 0
    verificare = 0

    for i in range(len(lista)):
        if is_palindrom(lista[i]):
            verificare = 1
            len_subsecventa_curenta = len_subsecventa_curenta + 1

        elif len_subsecventa_maxima < len_subsecventa_curenta:
            indice_final = i - 1
            indice_inceput = i - len_subsecventa_curenta
            len_subsecventa_maxima = len_subsecventa_curenta
            len_subsecventa_curenta = 0

    if len_subsecventa_maxima < len_subsecventa_curenta:
        indice_final = i
        indice_inceput = i - len_subsecventa_curenta + 1

    if verificare == 1:
        for i in range(indice_inceput, indice_final + 1):
            subsecventa_maxima.append(lista[i])
    else:
        return "Nu exista o asemenea subsecventa "
    return subsecventa_maxima


def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([22, 41, 66, 88]) == [66, 88]
    assert get_longest_all_palindromes([]) == "Nu exista o asemenea subsecventa "
    assert get_longest_all_palindromes([22, 44, 66, 81]) == [22, 44, 66]
    assert get_longest_all_palindromes([21, 44, 66, 81]) == [44, 66]


def nr_de_forma_x_la_k(element, k):
    """
    Functia verifica daca elementul poate fi scris sub forma x^k,k citit
    :param element: numar intreg
    :param k: numar natural
    :return: True/False
    """
    factor_prim = 2
    numarare = 0

    if element <= 0 :
        return False

    if element == 1:
        if k == 1 or k == 0:
            return True
        else :
            return False

    while element != 1:
        if element % factor_prim == 0:
            while element % factor_prim == 0:
                element = element / factor_prim
                numarare = numarare + 1
            if element == 1 and numarare % k == 0:
                return True
            else:
                return False
        factor_prim = factor_prim + 1


def get_longest_powers_of_k(lista, k):
    """
    Functia determina cea mai lunga subsecventa formata din elemente care se pot scrie sub forma x^k,k citit
    :param lista: lista de elmente
    :param k: numar natural
    :return: cea mai lunga subsecventa
    """

    subsecventa_maxima = []
    len_subsecventa_curenta = 0
    len_subsecventa_maxima = 0
    verificare = 0

    for i in range(len(lista)):
        if nr_de_forma_x_la_k(lista[i], k):
            verificare = 1
            len_subsecventa_curenta = len_subsecventa_curenta + 1

        elif len_subsecventa_maxima < len_subsecventa_curenta:
            indice_final = i - 1
            indice_inceput = i - len_subsecventa_curenta
            len_subsecventa_maxima = len_subsecventa_curenta
            len_subsecventa_curenta = 0

    if len_subsecventa_maxima < len_subsecventa_curenta:
        indice_final = i
        indice_inceput = i - len_subsecventa_curenta + 1

    if verificare == 1:
        for i in range(indice_inceput, indice_final + 1):
            subsecventa_maxima.append(lista[i])
    else:
        return "Nu exista o asemenea subsecventa "
    return subsecventa_maxima


def test_get_longest_powers_of_k():
    assert get_longest_powers_of_k([4, 16, 9, 1, 4, 9], 2) == [4, 16, 9]
    assert get_longest_powers_of_k([1, 1, 2, 3], 1) == [1, 1, 2, 3]
    assert get_longest_powers_of_k([], 3) == "Nu exista o asemenea subsecventa "
    assert get_longest_powers_of_k([4, 9, 1, 4, 16, 9], 2) == [4, 16, 9]


def teste():
    """
    Se executa testele de baza
    :return: None
    """
    test_get_longest_all_palindromes()
    test_get_longest_powers_of_k()
    print("De mentionat : Functiile responsabile de verificarea prop. au trecut testele de baza")


def citire_date(optiune1):
    """
    Functia citeste numarul si elementele listei ; apelaza una dintre functiile de calcul
    :param: optiune1: numar natural
    :return: subsecventa cautata
    """

    teste()

    lista = []
    lista_afisata = []

    numar = int(input("Dati numarul elementelor "))
    for i in range(numar):
        lista.append(int(input("Dati elementul cu numarul " + str(i+1) + " ")))

    if optiune1 == 2:
        lista_afisata = get_longest_all_palindromes(lista)
        print("Cea mai mare subsecventa cu prop. ca toate nr. sunt palindrom este " + str(lista_afisata) + " ")
        print("Programul s-a intors la meniu principal unde puteti citi alte date,sau iesi din program ")

    elif optiune1 == 3:
        k = int(input("Dati valoarea k "))
        lista_afisata = get_longest_powers_of_k(lista, k)
        print("Cea mai mare subsecventa cu prop. ca toate nr. se pot scrie sub forma x^k este " + str(lista_afisata) + " ")
        print("Programul s-a intors la meniu principal unde puteti citi alte date,sau iesi din program ")

    else:
        while True:
            print("Alegeti ce proprietate sa aiba subsecventa,sau intoarceti-va la meniul principal (puteti citi alte date) ")
            print("Alegeti o optiune: ")
            print("1. Determinare cea mai lungă subsecvență cu toate numerele palindrom")
            print("2. Determinare cea mai lungă subsecvență cu numere ce pot fi scrise sub forma x^k ")
            print("3. Meniu principal ")
            optiune2 = int(input("Alegeti optiunea "))

            if optiune2 == 1:
                lista_afisata = get_longest_all_palindromes(lista)
                print("Cea mai mare subsecventa cu prop. " + str(optiune2) + " este " + str(lista_afisata) + " ")

            elif optiune2 == 2:
                k = int(input("Dati valoarea k "))
                lista_afisata = get_longest_powers_of_k(lista, k)
                print("Cea mai mare subsecventa cu prop. " + str(optiune2) + " este " + str(lista_afisata) + " ")

            elif optiune2 == 3:
                break

            else:
                print("Optiune gresita, alegeti din nou ")
            print("Programul s-a intors la meniu principal unde puteti citi alte date,sau iesi din program ")
            break


def main():
    print("Meniu principal ")
    print("Alegeti o optiune: ")
    while True:
        print("1. Citeste datele ")
        print("2. Determinare cea mai lungă subsecvență cu numere palindrom ")
        print("3. Determinare cea mai lungă subsecvență cu numere ce pot fi scrise sub forma x^k ")
        print("4. Iesire ")
        optiune1 = int(input("Introduceti numarul optiunnii "))
        if optiune1 == 1:
            citire_date(1)
        elif optiune1 == 2:
            print("Prima data va trebui sa cititi datele,se selecteaza automat optiunea 1 ")
            citire_date(optiune1)
        elif optiune1 == 3:
            print("Prima data va trebui sa cititi datele,se selecteaza automat optiunea 1 ")
            citire_date(optiune1)
        elif optiune1 == 4:
            print("La revedere! ")
            break
        else:
            print("Optiune gresita,alegeti din nou ")


if __name__ == '__main__':
    main()
