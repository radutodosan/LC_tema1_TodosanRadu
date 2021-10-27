"""
    sau = "∨"
    si = "∧"
    not = "¬"
    implica = "⇒"
    echivalent = "⇔"
"""


def verificare_propozitie():
    # pdeschisa va tine cont de numarul parantezelor deschise din sintaxa introdusa
    pdeschisa = 0
    # pinchisa va tine cont de numarul parantezelor inchise din sintaxa introdusa
    pinchisa = 0

    # verificam daca primul caracter din sintaxa introdusa este paranteza deschisa
    if sintaxa_introdusa[0] == "(":
        pdeschisa += 1

    # sterg spatiile din sintaxa introdusa pentru a fi mai usor de lucrat
    sintaxa = sintaxa_introdusa.replace(" ", "")

    # parcurg sintaxa caracter cu caracter folosindu-ma de i
    for i in range(1, len(sintaxa)):

        """
            in urmatoarele conditii verific pentru fiecare caracter din sintaxa, daca
            caracterul precedent este asezat conform definitiei propozitiilor
        """
        if sintaxa[i] == "(":
            if sintaxa[i-1] == "(" or sintaxa[i-1] in simboluri or sintaxa[i-1] in negatie:
                pdeschisa += 1
            else:
                return False
        elif sintaxa[i] == ")":
            if sintaxa[i-1] == ")" or sintaxa[i-1].isalpha():
                pinchisa += 1
            else:
                return False
        elif sintaxa[i].isalpha() and not (sintaxa[i-1] == "(" or sintaxa[i-1] in simboluri or sintaxa[i-1] in negatie):
            return False
        elif sintaxa[i] in simboluri and not (sintaxa[i-1] == ")" or sintaxa[i-1].isalpha()):
            return False
        elif sintaxa[i] in negatie and sintaxa[i-1] != "(":
            return False

    # daca numarul parantezelor deschise este diferit de numarul parantezelor inchise sintaxa nu e propozitie
    if pdeschisa != pinchisa:
        return False
    # daca s-a ajuns pana aici inseamna ca sintaxa este propozitie asa ca returnez true
    else:
        return True


# variabila simboluri tine minte multimea simbolurilor mai putin cel al negatiei
simboluri = "∨∧⇒⇔"

# variabila negatie tine minte negatia
negatie = '¬'

# input-ul utilizatorului (introducerea sintaxei)
sintaxa_introdusa = input("Introduceti sintaxa: ")

# afisarea rezultatului
if verificare_propozitie() is True:
    print("Sintaxa introdusa este o formula propozitionala.")
else:
    print('Sintaxa introdusa NU este o formula propozitionala.')
