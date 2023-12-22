# Il faut bien placer le shell dans le fichier "Genome" auparavant !

long_alpha = 256
def alphabet(texte):
    alphab = [-1]*long_alpha
    for i in range(len(texte)):
        alphab[ord(texte[i])] = i
    return alphab

def recherche(texte, paterne):
    assert type(texte) == str,"Le texte doit être un 'str' !"
    assert type(paterne) == str,"Le paterne rechercher doit être un 'str' !"
    paterne=paterne.upper() #Cette partie est appliquée pour que l'utilisateur ne puisse chercher des caractère autre que T,C,G et A qui ne sont pas présent dans le génome humain
    for carac in paterne:
        if carac!="T" and carac!="A" and carac!="C" and carac!="G" :
            return "les chromosomes qui constituent le génome humain sont une succession de brins antiparallèles. Ces brins sont composés d'une succession de bases nucléiques, ou bases azotées — adénine (A), cytosine (C), guanine (G) ou thymine (T).Il est donc impossible de trouver des bases azotées autre que T,A,C et G"
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
        print( "Le paterne n'est pas présent")
    if len(result) == 1 :
        print ("Le paterne a été détécté",len(result),"fois a l'emplacement :")
        return result
    else:
        print ("Le paterne a été détécté",len(result),"fois aux emplacements :")
        return result


def recherche_naive(texte, mot):
    assert type(texte) == str, "Le texte doit être un 'str' !"
    assert type(mot) == str, "Le mot recherché doit être un 'str' !"
    assert texte != "", "Il n'y a pas de texte dans lequel chercher."
    assert mot != "", "Il n'y a pas de mot à chercher."
    result = 0
    reresult = []
    for a in range(len(texte)):
        if texte[a] == mot[0]:
            var = 0
            for b in range(len(mot)):
                if (a + b) < len(texte) and texte[a + b] != mot[b]:
                    var += 1
            if var == 0:
                result += 1
                reresult.append(a)
    print("il y a", result ,"occurence du mot recherché aux emplacements:")
    print(reresult)

fichier=input("Veuillez écrire le nom du fichier qui contient le génome que vous voulez étudier :")
# Ouvre le fichier f'fichier' en mode lecture avec l'encodage 'utf-8'
with open(f'{fichier}', 'r', encoding='utf-8') as fichier_source:
    # Lit la première ligne du fichier
    premiere_ligne = fichier_source.readline()

    # Lit toutes les lignes restantes du fichier et les stocke dans la liste 'lignes'
    lignes = fichier_source.readlines()

# &r les caractères filtrés
genome = ""

# Parcourt chaque ligne dans la liste 'lignes'
for mot in lignes:
    # Parcourt chaque caractère dans la ligne actuelle
    for carac in mot:
        # Vérifie si le caractère est l'un des quatre acides nucléiques "T", "A", "C" ou "G"
        if carac == "T" or carac == "A" or carac == "C" or carac == "G":
            # Ajoute le caractère au génome
            genome += carac

paterne=input("veuillez écrire le paterne que vous comptez rechercher dans le génome:")
recherche(genome, paterne)