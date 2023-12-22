long_alpha = 256
def alphabet(texte):
    # cette première fonction sert a créer une table de 256 elements représentant la table ASCII , nous nous arretons a 256 elements car au dela cela reviendrais a rajouter des caractères presque jamais utilisé, les éléments de la table seront tous [-1] sauf au emplacements sur la table ASCII d'un caractere de texte, aux emplacements d'un caractere de texte on renvoie l'emplacement (indice) de la derniere occurence de ce caractere de texte
    alphab = [-1]*long_alpha
    for i in range(len(texte)):
        alphab[ord(texte[i])] = i
    return alphab

def recherche(texte, paterne):
    assert type(texte) == str,"Le texte doit être un 'str' !"
    assert type(paterne) == str,"Le paterne doit être un 'str' !"
#     cette deuxième fonction éffectue la recherche même, on utilise la table créé par la fonction "alphabet" appelé ici "alphab" du paterne recherché, puis on utilise la variable "s" (initialisé a 0 au tout début) tant que la variable "s" est inférieur ou égale a la longueur du texte soustrait a la longueur du paterne , la fonction continuera.
    t = len(texte)
    p = len(paterne)
    alphab = alphabet(paterne)
    result=[]
    s = 0
# Afin de chercher le paterne , on initialise premierement "j" qui est égale a la longueur du paterne -1 (correspondant au dernier caractère du paterne) puis tant que j est supérieur ou égale a 0 ET que paterne[j] est égale a la position dans le texte alors on soustrait 1 a j pour vérifier le caractère précédent, si j arrive a 0 cela revien a dire que le paterne a été trouvé , si cela n'est pas le cas alors on re initialise j a la longueur du paterne -1
# la variable s dans les 2 cas change, si j arrive a 0 alors on note l'emplacement du premier caractère de la position du paterne dans le texte (s) dans la table result et s est incrémenté de la longueur du mot tout en vérifiant a ce que s ne sorte pas de la longueur du texte.Dans l'autre cas , donc si j n'arrive pas a 0, alors on incrémente s du maximum entre 1 et j soustrait a l'emplacement dans la table alphab du caractère ou "j" s'est arrété (s+j)
    while s <= t-p:
        j = p-1
        while j >= 0  and paterne[j] == texte[s+j]:
            j = j-1
        if j<0:
            result.append(s)
            s = s + (p-alphab[ord(texte[s+p])] if s+p<t else 1)
        else:
            s = s + max(1, j - alphab[ord(texte[s+j])])
# Á la fin nous renvoyons la table result contenant tout les indices des premier caractère du paterne présent dans le texte, si result est vide alors on renvoie "Le paterne n'est pas présent".
    if result == []:
        return "Le paterne n'est pas présent"
    print ("Le paterne a été détécté aux emplacements :")
    for elt in result:
        print(elt)



def recherche_naive(texte, mot):
    # Vérifie que les arguments sont des chaînes de caractères
    assert type(texte) == str, "Le texte doit être un 'str' !"
    assert type(mot) == str, "Le mot recherché doit être un 'str' !"
    assert texte != "", "Il n'y a pas de texte dans lequel chercher."
    assert mot != "", "Il n'y a pas de mot à chercher."
    # Initialisation du compteur de résultats
    result = 0

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
            # Si toutes les correspondances sont trouvées, incrémente le compteur de résultats
            if var == 0:
                result += 1

    # Renvoie le nombre total d'occurrences du motif dans le texte
    return result
