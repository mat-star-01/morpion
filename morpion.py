class Morpion:
    def __init__(self):
        self.grille = "...\n...\n..."


    def afficher_la_grille(self):
        print(self.grille)


    def demander_au_joueur_ce_qu_il_veut_jouer(self):
        pass


    def mettre_des_lettres_sur_la_case(self):
        pass


    def changer_de_joueur(self):
        pass


    def verifier_si_il_a_gagne(self):
        return True


    def lui_dire_bravo(self):
        pass


    def jouer(self):
        while True:
            a = "X"
            z = "O"
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
