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
        for index_de_ligne in range(3):
            print(" ".join(self.grille[index_de_ligne]))


    def demander_au_joueur_ce_qu_il_veut_jouer(self):
        entree_valide = False
        while not entree_valide:
            try:
                self.user_input = int(input("Qu'est ce que tu veux jouer ?\n"))  # Le user joue.
            except ValueError:  # Si le user entre quelque chose qui n'est pas un nombre:
                self.user_input = 0  # On entre 0, qui ne peut pas entrer dans la grille.
            if self.user_input in self.grille_dict:  # Si le user met un nombre qui peut entrer dans la grille:
                entree_valide = True  # On se souvient que sont entree est valide.
            else:  # Au contraire, si son entree n'est pas valide:
                print("Desole je ne peux pas accepter cette entree.")  # On lui dit que son entree n'est pas valide.

    def mettre_des_lettres_sur_la_case(self):
        coord = self.grille_dict[self.user_input]
        self.grille[coord[0]][coord[1]] = self.tour_du_joueur

    def changer_de_joueur(self):
        if self.tour_du_joueur == "X":
            self.tour_du_joueur = "O"
        else:  # if self.tour_du_joueur == "O":
            self.tour_du_joueur = "X"

    def verifier_si_un_joueur_a_gagne(self):
        colonne_gagnee = []
        for colonne_index in range(3):
            colonne_gagnee.append(self.grille[0][colonne_index] == self.grille[1][colonne_index] == self.grille[2][colonne_index] != ".")

        ligne_gagnee = []
        for ligne_index in range(3):
            ligne_gagnee.append(self.grille[ligne_index][0] == self.grille[ligne_index][1] == self.grille[ligne_index][2] != ".")

        diagonale_gagnee = []
        ligne_gagnee.append(self.grille[0][0] == self.grille[1][1] == self.grille[2][2] != ".")
        ligne_gagnee.append(self.grille[2][0] == self.grille[1][1] == self.grille[0][2] != ".")

        return any(colonne_gagnee) or any(ligne_gagnee) or any(diagonale_gagnee)

    def lui_dire_bravo(self):
        print(f"Bravo au joueur {self.tour_du_joueur} ! Tu as gagne.")

    def verifier_si_la_grille_est_pleine(self):
        for index_de_ligne in range(3):
            if "." in self.grille[index_de_ligne]:
                return False
        return True

    def personne_n_a_gagne(self):
        print("La grille est pleine donc personne n'a gagne. ")

    def jouer(self):
        while True:
            self.afficher_la_grille()
            self.demander_au_joueur_ce_qu_il_veut_jouer()
            self.mettre_des_lettres_sur_la_case()
            il_a_gagne = self.verifier_si_un_joueur_a_gagne()

            if il_a_gagne:
                self.afficher_la_grille()
                self.lui_dire_bravo()
                break
            else:
                la_grille_est_pleine = self.verifier_si_la_grille_est_pleine()

                if la_grille_est_pleine:
                    self.afficher_la_grille()
                    self.personne_n_a_gagne()
                    break
                self.changer_de_joueur()


morpion = Morpion()
morpion.jouer()
