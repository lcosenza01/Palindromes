"""
teste si la chaine p passé en paramètre est un palindrome
"""

def ispalindrome(p):
    """
    méthode principale
    """
    trad=str.maketrans(str.maketrans({
    'à': 'a', 'â': 'a', 'ä': 'a', 'á': 'a', 'ã': 'a', 'å': 'a',
    'è': 'e', 'ê': 'e', 'ë': 'e', 'é': 'e',
    'ì': 'i', 'î': 'i', 'ï': 'i', 'í': 'i',
    'ò': 'o', 'ô': 'o', 'ö': 'o', 'ó': 'o', 'õ': 'o',
    'ù': 'u', 'û': 'u', 'ü': 'u', 'ú': 'u',
    'ç': 'c', 'ñ': 'n',
    'À': 'A', 'Â': 'A', 'Ä': 'A', 'Á': 'A', 'Ã': 'A', 'Å': 'A',
    'È': 'E', 'Ê': 'E', 'Ë': 'E', 'É': 'E',
    'Ì': 'I', 'Î': 'I', 'Ï': 'I', 'Í': 'I',
    'Ò': 'O', 'Ô': 'O', 'Ö': 'O', 'Ó': 'O', 'Õ': 'O',
    'Ù': 'U', 'Û': 'U', 'Ü': 'U', 'Ú': 'U',
    'Ç': 'C', 'Ñ': 'N'})) 
    simple=p.translate(trad)
    simple_ans_espace=""
    for c in simple:
        if (c.isalpha() or c.isnumeric()) :
            simple_ans_espace+=c
    simple_sans_espacemj = simple_ans_espace.lower()
    if len(simple_sans_espacemj)<2:
        return True
    if simple_sans_espacemj[0]==simple_sans_espacemj[-1]:
        return ispalindrome(simple_sans_espacemj[1:-1])
    return False

#### Fonction principale


def main():
    """
    methode principale
    """
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
