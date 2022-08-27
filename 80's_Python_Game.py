import random
import time
 
joueur_1 = 50
joueur_2 = 50
potion = 3
 
while joueur_1 > 0 and joueur_2 > 0: 
    action = int(input("Souhaitez-vous attaquer (1) ou utiliser une potion (2)?"))
    if action == 1:
        joueur_2 = joueur_2 - random.randint(5, 10)
        print(f"Joueur 1 : {joueur_1} pdv. Joueur 2 : {joueur_2} pdv.")
        time.sleep(0.5)
        print("L'adversaire vous attaque.")
        time.sleep(1)
        joueur_1 = joueur_1 - random.randint(5, 15)
    elif action == 2:
        if potion == 0:
            print("Vous n'avez plus de potions.")
            continue
        else:
            gain = random.randint(15, 50)
            joueur_1 = joueur_1 + gain
            print(f"vous gagnez {gain} points de vie. Total : {joueur_1} points.")
            potion -= 1
        print(f"Il vous reste {potion} potions.")
        time.sleep(2)
        print(f"L'adversaire vous attaque.")
        time.sleep(2)
        joueur_1 = joueur_1 - random.randint(5, 15)
        print(f"Il vous reste {joueur_1} points de vies.")
        print("Vous passez votre tour. L'adversaire vous attaque à nouveau!")
        time.sleep(2)
        joueur_1 = joueur_1 - random.randint(5, 15)
    else:
        print("Commande invalide")
    print(f"Joueur 1 : {joueur_1} pdv. Joueur 2 : {joueur_2} pdv.")
 
if joueur_1 > 0 :
    print(f"Fin du jeu, vous avez gagné! Il vous reste {potion} potions.")
else:
    print("Fin du jeu, vous avez perdu.")
