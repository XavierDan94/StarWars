class Film:
    # Constructeur de la classe Film
    def __init__(self, titre, sortie, episode, cout, recette, acteurs=None, personnages=None):
        self.titre = titre
        self.sortie = sortie
        self.episode = episode
        self.cout = cout
        self.recette = recette
        if acteurs is None:
            self.acteurs = []
        self.acteurs = acteurs
        if personnages is None:
            self.personnages = []
        self.personnages = personnages

    # Getters
    def get_titre(self):
        return self.titre

    def get_sortie(self):
        return self.sortie

    def get_episode(self):
        return self.episode

    def get_cout(self):
        return self.cout

    def get_recette(self):
        return self.recette

    def get_acteurs(self):
        liste = ""
        for i in range(0, len(self.acteurs)):
            liste += str(self.acteurs[i]) + " / "
        return liste

    # Setters
    def set_titre(self, titre):
        self.titre = titre

    def set_sortie(self, sortie):
        self.sortie = sortie

    def set_episode(self, episode):
        self.episode = episode

    def set_cout(self, cout):
        self.cout = cout

    def set_recette(self, recette):
        self.recette = recette

    def set_acteurs(self, acteur):
        for i in range(0, len(acteur)):
            if i == 0:
                self.acteurs = [acteur[i]]
            else:
                self.acteurs += ([acteur[i]])

    # Redéfinition de la méthode __str__
    def __str__(self):
        acteurs = self.get_acteurs()
        return "Titre : " + self.get_titre() + "\nAnnée de sortie: " + str(self.get_sortie()) + "\nNuméro d'épisode: " \
               + self.get_episode() + "\nCoût: " + str(self.get_cout()) + " EUR\nRecette: " + str(self.get_recette()) +\
               " EUR\nActeurs: " + acteurs

    def nb_acteurs(self):
        return 0 if self.acteurs is None else len(self.acteurs)

    def nb_personnages(self):
        return 0 if self.personnages is None else len(self.personnages)

    def calcul_benefice(self):
        est_beneficiaire = False
        resultat = self.get_recette() - self.get_cout()
        if self.get_recette() > self.get_cout():
            est_beneficiaire = True
        return resultat, est_beneficiaire

    def is_before(self, annee):
        return True if self.get_sortie() < annee else False
