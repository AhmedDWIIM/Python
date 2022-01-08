
from tkinter import *


#! /usr/bin/python


"""
Petit jeu d'allumettes
-----------------------
Au départ il y a 30 allumettes, 2 joueurs prennent des à allumettes à tour de rôle.
Celui qui prend la dernière a perdu.
Chaque joueur peut prendre entre 1 et le double du nombre d'allumettes
prises par le précédent.

"""
class allumette():
    """
    La classe allumette contient l'ensemble des fonctions du jeu.
    à l'initialisation, on passe le nombre d'allumettes du jeu
    En revanche la limite du premier retrait est fixée à 2
    """
    def __init__(self, n):
        self.fenetre = Tk ( )
        label_title = Label(self.fenetre, text="Jeu des Allumettes", font=("Helvetica",30) )
        label_title.pack(side=TOP)
        self.canvas = Canvas ( width = 600, height = 300 )
        self.canvas.pack (side=BOTTOM )
        self.allumettes = n
        self.limit = 2
        
    def afficheStatut(self, text):
        """
        Méthode qui permet d'afficher à quel niveau du jeu nous sommes
        Elle reçoit en variable texte une chaine différente suivant
         que nous sommes dans le tour du joueur ou celui de l'ordi
        """
        print ("Il y a %i allumettes et %s en retirer de 1 à %i" % (self.allumettes, text, min(self.limit,self.allumettes)))
        #
        
        self.canvas.create_text ( 200 , 50 , text = "Il y a %i allumettes et %s en retirer de 1 à %i" % (self.allumettes, text, min(self.limit,self.allumettes)),font=("Helvetica",12) )
        
        
        #
    
    def display ( self,j,text ):
        try : self.canvas.delete ( ALL )
        except : pass
        
        x, xx, x1, xx1 = 0, 0, 10, 20
        for i in range ( j ):
            self.canvas.create_rectangle ( x + x1,100, xx + xx1, 200, fill="red" )
            x1 = x1 + 20
            xx1 = x1 + 10

    def retire(self, nb):
        """
        Méthode pour gérer un coup.
        C'est à dire retirer nb allumettes et mettre à jour la limite du coup suivant
        """
        retrait = min(nb, self.limit)
        self.allumettes -= retrait
        self.limit = 2*retrait
        if (self.allumettes > 0):
            return True
        else:
            return False

    def fin(self):
        """
        Méthode pour tester qu'il y a au moins une allumette en jeu
        """
        if (self.allumettes > 0):
            return True
        else:
            return False

    
    def joueur(self):
        """
        Le tour du joueur
        La méthode renvoie le nombre d'allumettes retirées par le joueur
        """
        ret = 0
        N = 0
        while (ret < 1 or ret > self.limit):
            self.afficheStatut("vous pouvez")
            def action():
                N = int(entryNbr.get())
            lbl_nbr = Label(self.fenetre, text ="Entrer la valeur :")
            lbl_nbr.place(x=15, y=120)
            entryNbr = Entry(self.fenetre)
            entryNbr.place(x=110, y= 120)
            Valider = Button(self.fenetre, text="Valider", command = action)
            Valider.place(x=235, y =115)
            ret = eval(input("Combien d'allumettes vous voulez retirer ? ==> "))
            
        return ret

    def ordi(self):
        """
        Le tour de l'ordinateur
        La méthode renvoie le nombre d'allumettes retirées par l'ordi
        L'IA du jeu (^_^);
        """
        self.afficheStatut("je peux")
        if self.allumettes == 1 :
            # Plus qu'une allumette, l'ordi a perdu
            # mais il est fair play et laisse un petit message
            nb = 1
            self.canvas.create_text ( 150, 50 , text = "Bien joué")
            print("Bien joué")
        elif self.limit >= (self.allumettes-1):
            # L'ordi a détecté un coup gagnant, il ne laisse qu'une allumette
            nb = self.allumettes-1
            self.canvas.create_text ( 150 , 50 , text = "Je crois que vous êtes mal parti...")
            print("Je crois que vous êtes mal parti...")
        else :
            # L'ordi se crée une situation gagnante
            # Il prend un nombre d'allumettes
            # - qui ne permet pas au joueur de gaganer
            # - qui devrait mettre le joueur en difficulté
            laisse = 2 * (self.limit+1)
            nb = max(1,min(self.limit,self.allumettes - laisse))
        self.canvas.create_text ( 100 , 50 , text = "A mon tour, je retire %i " % nb)
        print("A mon tour, je retire %i " % nb)
        return nb
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Le programme commence ici
#
# On peut choisi un nombre d'allumettes de départ à la création de l'instance


i = 30
monJeu = allumette(i)
liste = []
for j in range(i) :
    liste.append("|")
    
#JeuLabel = Label(fenetre, text=" ".join(liste), bg="yellow")
#JeuLabel.pack()

monJeu.display(len(liste),"")

while (monJeu.fin()):
    retire = monJeu.joueur()
    for z in range(retire):
            del liste[0]
            monJeu.display(len(liste),"vous pouvez")
    retour = monJeu.retire(retire)
    #JeuLabel.pack()

    if retour:
        retire = monJeu.ordi()
        for z in range(retire):
            del liste[0]
            monJeu.display(len(liste),"je peux")
        retour = monJeu.retire(retire)
        print(liste)
        if not retour:
            self.canvas.create_text ( 100 , 50 , text = "Vous avez gagné !" % nb)
            print("Vous avez gagné !")
    else:
        print("J'ai gagné !")

print("C'est terminé")