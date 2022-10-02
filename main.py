from film import Film
from acteur import Acteur
from personnage import Personnage


# [Question 5] -> Création de la fonction permettant de parcourir une collection
def parcours_collection(collection):
    """Affiche le contenu d'une collection d'objets"""
    longueur = len(collection)
    for i in range(0, longueur):
        print(collection[i], "\n")


if __name__ == '__main__':
    # [Question 2] -> Code permettant la création de films
    film1 = Film("Star Wars, épisode IV : Un nouvel espoir", 1977, "Trilogie originale", 15000000, 43000000)
    film2 = Film("Star Wars, épisode V : L'empire contre-attaque", 1980, "Trilogie originale", 20000000, 46000000, [Acteur("Hayek", "Salma"), Acteur("Pogba", "Mathias"), Acteur("Cruise", "Tom")])
    # Remplissage des attributs du troisième film par l'utilisateur
    """
    titre = str(input("Saisissez le titre du film -> "))
    annee = int(input("Saisissez l'année de sortie du film -> "))
    episode = str(input("Saisissez l'épisode du film -> "))
    cout = int(input("Saisissez le cout du film -> "))
    recette = int(input("Saisissez la recette du film -> "))
    film3 = Film(titre, annee, episode, cout, recette)
    """
    # [Question 3] -> Code permettant la création d'un personnage
    pers1 = Personnage("Skywalker", "Luke")

    # [Question 4] -> Création d'une collection et insertion des 3 objets films
    liste_de_films = [film1, film2]

    # [Question 6] -> Parcours de la collection d'objets
    # parcours_collection(liste_de_films)

    # [Question 7] -> Stockage de plusieurs acteurs dans Films
    acteur1 = Acteur("Earl Jones", "James")
    acteur2 = Acteur("Ford", "Harrisson")
    liste_de_films[0].set_acteurs([acteur1, acteur2])
    parcours_collection(liste_de_films)

    # [Question 11] -> Test des méthodes nb_acteurs(), nb_personnages(), calcul_benefice(), is_before()
    print(liste_de_films[0].nb_acteurs())
    print(liste_de_films[1].nb_personnages())
    print(liste_de_films[0].calcul_benefice())
    print(liste_de_films[1].is_before(2021))
