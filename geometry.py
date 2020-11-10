"""
TP sur la POO, Nathan Heckmann, classe E1
Notes : certaines méthode de la classe Vector nécessitent d'être en
dimension trois, j'ai donc généralisé la classe Point et la classe
Vector à la dimension 3.
"""

import random
import sys
# pour simuler un random entre 0 et "l'infini" car l'infini
# n'existe pas pour un ordinateur


class Point:
    """
    Définit un point du plan à partir de ses coordonnées en x et y.
    Ces attributs doivent être de type entier ou réel.

    Attribut total : renvoie le nombre de points déjà créer par la classe Point
    jusqu'à celui qui vient d'être instancié inclus.

    Arguments :
        - coordonnée en x (de type entier ou réel)
        - coordonnée en y (de type entier ou réel)
        - coordonnée en z (de type entier ou réel)
        - id du point (de type entier)
    """

    total = 0

    def __init__(self, x, y, z, idd):
        # abscisse
        self.x = float(x)
        # ordonnée
        self.y = float(y)
        self.z = float(z)
        self.idd = int(idd)
        Point.total += 1

    def display(self):
        """
        Retourne les coordonnées du point. (Pas de print() car sinon on ne peut
        pas afficher la représentation du vecteur comme il est indiqué dans
        l'énoncé de la class Vector envoyé par mail.)
        """
        return '(' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ')'

    def move(self, x_move, y_move, z_move):
        """
        Déplace le point de x_move et y_move.
        (Ajoute x_move à l'attribut x et y_move à l'attribut y.)
        Arguments:
            x_move: le float à ajouté à x.
            y_move: le float à ajouté à y.
        """
        self.x += x_move
        self.y += y_move
        self.z += z_move

    def display_idd(self):
        """
        affiche l'id du point
        """
        print(self.idd)


# p0 = Point(0, 0, 58462) question 2.1.3

l_points = []

if __name__ == "__main__":
    for i in range(0, 10):
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        z = random.randint(0, 100)
        i = random.randint(0, sys.maxsize)
        # sys.maxsize sert juste à renvoyer un très grand
        # nombre pour simuler l'infini
        p = Point(x, y, z, i)
        t = (p.x, p.y, p.z, p.idd, p.total)
        l_points.append(t)

print("id premier point crée: ", l_points[0][3],
      "; compteur total du premier point: ", l_points[0][4])
print("id dernier point crée: ", l_points[-1][3],
      "; compteur total du dernier point: ", l_points[-1][4])


class Vector:
    """
    Définit un vecteur grâce à ses coordonnées en x, y et z OU alors grâce à
    deux points.

    Attributs :
        begin : Point d'où commence le vecteur (par défaut (0,0,0)
        si le vecteur est définit par ses coordonnées)
        end : Point où se termine le vecteur (par défaut (0,0,0)
        si le vecteur est définit par ses coordonnées)

    Arguments :
        - Option 1 : définir le vecteur par ses coordonnées de type entier
        ou réel, on donne alors en arguments la coordonnée en x, puis en y,
        puis en z. Exemple : Vector(1, 2, 3).
        - Option 2 : définir le vecteur par ses deux points de débuts
        et de fin, on donne alors en arguments le point (de type Point)
        ou commence le vecteur en premier, puis le point (de type Point)
        où il se fini en second.
        Exemple: Vector(Point(0,0,0,5482), Point(1,1,2,9392))
    """

    begin = Point(0, 0, 0, 0)  # points par défaut si on defini le vecteur
    # grâce à ses coordonnées
    end = Point(0, 0, 0, 0)

    def __init__(self, *args):
        if type(args[0]) == Point:
            # si un point est donné en  premier argument
            # on considère que le second argument est aussi un Point
            # (si l'utilisateur a comprit la doc) et on calcule donc les
            # coordonnées du vecteur.
            self.x = args[0].x - args[1].x
            self.y = args[0].y - args[1].y
            self.z = args[0].z - args[1].z
            Vector.begin = args[0]
            Vector.end = args[1]
        else:
            # sinon si c'est pas des Point on considère que ce sont des
            # coordonnées (si l'utilisateur a comprit la doc)
            self.x = float(args[0])
            self.y = float(args[1])
            self.z = float(args[2])

    def display_from_points(self):
        """
        Affiche une représentation du vecteur à partir de ses points.
        """
        print("(" + Vector.begin.display() + Vector.end.display() + ")")

    def display_coord(self):
        """
        Affiche une représentation du vecteur à partir de ses coordonnées.
        """
        print("(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")")

    def add(self, v1, v2):
        """
        Retourne l'addition de deux vecteurs.
        Arguments : deux vecteur v1 et v2 de type Vector()
        """
        somme_x = v1.x + v2.x
        somme_y = v1.y + v2.y
        somme_z = v1.z + v2.z
        return Vector(somme_x, somme_y, somme_z)

    def scalar_product(self, v1, v2):
        """
        Retourne le produit scalaire de deux vecteurs.
        Arguments : deux vecteurs v1 et v2 de type Vector()
        """
        return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

    def vector_product(self, v1, v2):
        """
        Retourne le produit vectoriel de deux vecteurs.
        Arguments : deux vecteurs v1 et v2 de type Vector()
        """
        x = v1.y * v2.z - v1.z * v2.y
        y = v1.z * v2.x - v1.x * v2.z
        z = v1.x * v2.y - v1.y * v2.x
        return Vector(x, y, z)

Vector(1,1,1)
