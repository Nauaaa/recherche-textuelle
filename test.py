def recherche_naive(texte, mot):
    # Vérifie que les arguments sont des chaînes de caractères
    assert type(texte) == str, "Le texte doit être un 'str' !"
    assert type(mot) == str, "Le mot recherché doit être un 'str' !"
    assert texte != "", "Il n'y a pas de texte dans lequel chercher."
    assert mot != "", "Il n'y a pas de mot à chercher."
    # Initialisation du compteur de résultats et du tableau des emplacements
    result = 0
    reresult = []

    # Parcourt chaque position dans le texte
    for a in range(len(texte)):
        # Vérifie si le caractère actuel dans le texte correspond au premier caractère du motif
        if texte[a] == mot[0]:
            var = 0
            # Parcourt chaque caractère du motif
            for b in range(len(mot)):
                # Compare les caractères du texte et du motif
                if (a + b) < len(texte) and texte[a + b] != mot[b]:
                    var += 1
            # Si toutes les correspondances sont trouvées, incrémente le compteur de résultats et marque la position du motif dans "reresult"
            if var == 0:
                result += 1
                reresult.append(a)
    # Renvoie le nombre total d'occurrences du motif et leurs emplacement dans le texte
    print("il y a", result ,"occurence du mot recherché aux emplacements:")
    print(reresult)

long_alpha = 256
def alphabet(texte):
    alphab = [-1]*long_alpha
    for i in range(len(texte)):
        alphab[ord(texte[i])] = i
    return alphab

def recherche(texte, paterne):
    assert type(texte) == str,"Le texte doit être un 'str' !"
    assert type(paterne) == str,"Le paterne doit être un 'str' !"
    assert texte != "", "Il n'y a pas de texte dans lequel chercher."
    assert paterne != "", "Il n'y a pas de paterne à chercher."
    t = len(texte)
    p = len(paterne)
    alphab = alphabet(paterne)
    result=[]
    s = 0
    while s <= t-p:
        j = p-1
        while j >= 0  and paterne[j] == texte[s+j]:
            j = j-1
        if j<0:
            result.append(s)
            s = s + (p-alphab[ord(texte[s+p])] if s+p<t else 1)
        else:
            s = s + max(1, j - alphab[ord(texte[s+j])])
    if result == []:
        return "Le paterne n'est pas présent"
    if len(result) == 1 :
        print ("Le paterne a été détécté",len(result),"fois a l'emplacement :")
        return result
    else:
        print ("Le paterne a été détécté",len(result),"fois aux emplacements :")
        return result


if __name__ == "__main__":
    """TEST RECHERCHE NAIVE"""
#     Tests de recherche :
    # print(recherche_naive("baac", "a"))
    # print(recherche_naive("0000000001000", "00"))

#      Tests d'assertion :
    # print(recherche_naive("baac", 0))
    # print(recherche_naive(000, "a"))
    # print(recherche_naive("", "a"))
    # print(recherche_naive("abc", ""))

#     Tests d'erreurs : (vérifier si la fonction ne s'éxécute pas meme avec des valeurs manquante)
    # print(recherche_naive(, "a"))
    # print(recherche_naive("abc", ))

    """TEST RECHERCHE BOYER-MOORE-HORSPOOL"""

#     Tests de recherche :
# print(recherche("aaaaab","a"))
# print(recherche("aaaaab","aa"))
# print(recherche("aaaaab","ab"))
# print(recherche("lorem ipsum dolor sit amet"," "))

#     Tests d'assertion :
# print(recherche("aaaab","c"))
# print(recherche("aaaab",""))
# print(recherche("","aaaaaaab"))

# La table "alphab" se basant sur la table ascii, tout caractère d'un autre alphabet comme un caractère chinois provoquera une erreur "index i out of range".
# print(recherche("異 ","異"))