# Le Jeu des allumettes

"""
Petit jeu d'allumettes
-----------------------
Au départ il y a 30 allumettes, 2 joueurs prennent des à allumettes à tour de rôle.
Celui qui prend la dernière a perdu.
Chaque joueur peut prendre entre 1 et le double du nombre d'allumettes
prises par le précédent.

"""

## Lancement du jeu
En premier temps placer vous dans le dossier racine du projet

Ensuite executer cette commande
```bash
python allumette.py
```

## Le Jeu
Le jeu se joue sur le terminal, cette partie-là et entièrement fonctionnel.
Aussi est integrée une IA qui répond selon les coups !
```python
Il y a 30 allumettes et vous pouvez en retirer de 1 à 2
Combien d'allumettes vous voulez retirer ? ==>
```
Une partie graphique a été intégrée, on peut voir les allumettes diminuées au fur et à mesureCependant les entre claviers par Tkinter ne fonctionne pas correctement

## Point de difficulté
Ici j'affiche mon form pour récupérer l'entre claviers cependant lorsque je retourne N il ne prend pas en compte la valeur de
```python
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
            
        return N
 ```
