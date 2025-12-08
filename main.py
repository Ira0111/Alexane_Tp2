from classes.Member import*
from classes.Operator import*
from classes.Mentalist import*
from classes.Spaceship import*
from classes.Fleet import*
import json 


fleet = Fleet("Galactica")

while True:
    print("\n=== MENU PRINCIPAL ===")
    print("1. Créer un vaisseau")
    print("2. Ajouter un membre à un vaisseau")
    print("3. Afficher l'équipage d'un vaisseau")
    print("4. Supprimer un membre d'un vaisseau")
    print("5. Vérifier la préparation d'un vaisseau")
    print("6. Afficher les statistiques de la flotte")
    print("0. Quitter")

    choice = input("Votre choix : ")

    match choice:
        case "1":
            ship_name = input("Nom du vaisseau : ")
            ship_type = input("Type du vaisseau (marchand/guerre) : ")
            ship = Spaceship(ship_name, ship_type)
            fleet.append_spaceship(ship)

        case "2":
            ship_name = input("Nom du vaisseau : ")
            for ship in fleet.spaceships:
                if ship.name == ship_name:
                    first_name = input("Prénom : ")
                    last_name = input("Nom : ")
                    gender = input("Genre (homme/femme) : ")
                    age = int(input("Âge : "))
                    role = input("Rôle (pilote/technicien/commandant) : ")
                    crew_member = Operator(first_name, last_name, gender, age, role)
                    ship.append_member(crew_member)
                    break

        case "3":
            ship_name = input("Nom du vaisseau : ")
            for ship in fleet.spaceships:
                if ship.name == ship_name:
                    ship.display_crew()
                    break

        case "4":
            ship_name = input("Nom du vaisseau : ")
            last_name = input("Nom du membre à supprimer : ")
            for ship in fleet.spaceships:
                if ship.name == ship_name:
                    ship.remove_member(last_name)
                    break

        case "5":
            ship_name = input("Nom du vaisseau : ")
            found = False
            for ship in fleet.spaceships:
                if ship.name == ship_name:
                    if ship.check_preparation():
                        print("Le vaisseau est prêt !")
                    else:
                        print("Le vaisseau n'est pas prêt.")
                    found = True
                    break
            if not found:
                print("Aucun vaisseau nommé", ship_name, "n'a été trouvé dans la flotte.")

        case "6":
            fleet.statistics()

        case "0":
            print("Au revoir 👋")
            break

        case _:
            print("Choix invalide, réessayez.")