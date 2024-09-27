"""Fonction """
#### Imports et définition des variables globales
import csv

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l=[]
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f, delimiter = ";")
        for row in reader :
            int_row = list(map(int, row))
            l.append(int_row)
    return l

print(read_data(FILENAME))



def get_list_k(data, k):
    """retourne le kieme element"""
    return data[k]



def get_first(l):
    """premier element"""
    return l[0]

def get_last(l):
    """dernier element"""
    return l[len(l)-1]


def get_max(l):
    """maximum de la liste"""
    return max(l)


def get_min(l):
    """minimum de la liste"""
    return min(l)


def get_sum(l):
    """Somme de la liste"""
    s = 0
    for i, nombre in enumerate(l):
        i+=1
        s += nombre
    return s



#### Fonction principale


def main():
    """Fonction main"""
    # data = read_data(FILENAME)
    # for i, l in enumerate(data):
    #     print(i, l)
    # k = 37
    # print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
