class Morpion:
    def __init__(self):
        self.grille = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
        self.user_input = 0
        self.tour_du_joueur = "X"
        self.grille_dict = {
            1: (2, 0),
            2: (2, 1),
            3: (2, 2),
            4: (1, 0),
            5: (1, 1),
            6: (1, 2),
            7: (0, 0),
            8: (0, 1),
            9: (0, 2),
        }

    def afficher_la_grille(self):
        print(" ".join(self.grille[0]))
        print(" ".join(self.grille[1]))
        print(" ".join(self.grille[2]))

    def demander_au_joueur_ce_qu_il_veut_jouer(self):
        self.user_input = int(input("Qu'est ce que tu veux jouer ?\n"))
        # TODO: Verifier que self.user_input est valide.
        #   ex invalide: 10
        #   ex invalide: 0
        #   ex invalide: -1
        #   ex invalide: y
        #   ex invalide: 102
        #   ex invalide: 1000564

    def mettre_des_lettres_sur_la_case(self):
        coord = self.grille_dict[self.user_input]
        self.grille[coord[0]][coord[1]] = self.tour_du_joueur

    def changer_de_joueur(self):
        if self.tour_du_joueur == "X":
            self.tour_du_joueur = "O"
        else:  # if self.tour_du_joueur == "O":
            self.tour_du_joueur = "X"

    def verifier_si_il_a_gagne(self):
        return False
        # TODO: a faire.

    def lui_dire_bravo(self):
        print("bravo")

    def jouer(self):
        while True:
            self.afficher_la_grille()
            self.demander_au_joueur_ce_qu_il_veut_jouer()
            self.mettre_des_lettres_sur_la_case()
            self.changer_de_joueur()
            il_a_gagne = self.verifier_si_il_a_gagne()

            if il_a_gagne:
                self.lui_dire_bravo()
                break


morpion = Morpion()
morpion.jouer()
