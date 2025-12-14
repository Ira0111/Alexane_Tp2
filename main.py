from classes.Member import *
from classes.Operator import *
from classes.Mentalist import *
from classes.Spaceship import *
from classes.Fleet import *
import json, ast

def save_data(fleet, file_name="data.json"):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(fleet, file, default=custom_serializer, indent=4, ensure_ascii=False)
    print("Flotte sauvegardée")


def custom_serializer(obj):
    if isinstance(obj, Spaceship):
        return {
            "_Spaceship__name": obj.name,
            "_Spaceship__shipType": obj.shipType,
            "_Spaceship__condition": obj.condition,
            "_Spaceship__crew": obj.crew,
        }
    if isinstance(obj, Fleet):
        return {
            "_Fleet__name": obj.name,
            "_Fleet__spaceships": obj.spaceships
        }
    # Pour Operator et Mentalist, on laisse __dict__ car c'est déjà bien écrit
    return obj.__dict__

def load_data(file_name="data.json"):
    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file)

    fleet_name = data["_Fleet__name"]
    fleet = Fleet(fleet_name)

    for ship_data in data["_Fleet__spaceships"]:
        ship = Spaceship(ship_data["_Spaceship__name"], ship_data["_Spaceship__shipType"])
        ship.condition = ship_data["_Spaceship__condition"]

        for member_data in ship_data["_Spaceship__crew"]:
            first_name = member_data["_Member__first_name"]
            last_name = member_data["_Member__last_name"]
            gender = member_data["_Member__gender"]
            age = member_data["_Member__age"]

            if "_Operator__role" in member_data:
                role = member_data["_Operator__role"]
                experience = member_data["_Operator__experience"]
                crew_member = Operator(first_name, last_name, gender, age, role)
                crew_member.experience = experience
            else:
                mana = member_data.get("_Mentalist__mana", 0)
                crew_member = Mentalist(first_name, last_name, gender, age, mana)

            ship.append_member(crew_member)

        fleet.append_spaceship(ship)
    print("\nFlotte chargée")
    return fleet

try:
    fleet = load_data("data.json")
except FileNotFoundError:
    print("Aucun fichier data.json trouvé. Création d'une flotte vide.")
    fleet = Fleet("Galactica")

# === Menu principal ===
while True:
    print("\n=== MENU PRINCIPAL ===")
    print("Que voulez-vous faire ?")
    print("1. Ajouter")
    print("2. Supprimer")
    print("3. Modifier")
    print("4. Autres actions")
    print("0. Quitter")

    choice = input("Votre choix : ")

    match choice:
        case "1":  # Ajouter
            print("\n=== AJOUTER ===")
            print("1. Créer un vaisseau")
            print("2. Ajouter un membre à un vaisseau")
            sub_choice = input("Votre choix : ")
            match sub_choice:
                case "1":
                    ship_name = input("Nom du vaisseau : ")
                    ship_type = input("Type du vaisseau (marchand/guerre) : ")
                    ship = Spaceship(ship_name, ship_type)
                    fleet.append_spaceship(ship)
                    print(f"Le vaisseau {ship.name} a été ajouté dans la flotte {fleet.name}")
                    save_data(fleet)
                case "2":
                    ship_name = input("Nom du vaisseau : ").strip().lower()
                    found = False
                    for ship in fleet.spaceships:
                        if ship.name.lower() == ship_name:
                            print("Type de membre à ajouter :")
                            print("1. Opérateur")
                            print("2. Mentaliste")
                            choix = input("Votre choix : ")

                            first_name = input("Prénom : ")
                            last_name = input("Nom : ")
                            gender = input("Genre (homme/femme) : ")
                            age = int(input("Âge : "))
                            match choix :
                                case "1" :
                                    role = input("Rôle (pilote/technicien/commandant/armurier/entretien/marchand) : ")
                                    experience = int(input("Expérience (années) : "))
                                    crew_member = Operator(first_name, last_name, gender, age, role)
                                    crew_member.experience = experience
                                case "2":
                                    mana = int(input("Mana (max 100) : "))
                                    if mana > 100:
                                        mana = 100 
                                        print("Le mana ne peut pas dépasser 100, valeur fixée à 100.")
                                    elif mana < 0:
                                        mana = 0 
                                        print("Le mana ne peut pas être négatif, valeur fixée à 0.")

                                    crew_member = Mentalist(first_name, last_name, gender, age, mana)
                                case _:
                                    print("Choix invalide, membre non ajouté.")
                                    break
                            ship.append_member(crew_member)
                            print(f"{crew_member.first_name} {crew_member.last_name} à été ajouté à l'équipage du vaisseau {ship.name}")
                            save_data(fleet)
                            found = True
                            break
                    if not found:
                        print(f"Aucun vaisseau nommé{ship_name}n'a été trouvé.")
                case _:
                    print("Choix invalide.")

        case "2":  # Supprimer
            print("\n=== SUPPRIMER ===")
            print("1. Supprimer un vaisseau")
            print("2. Supprimer un membre d'un vaisseau")
            sub_choice = input("Votre choix : ")
            match sub_choice:
                case "1":
                    ship_name = input("Nom du vaisseau à supprimer : ").strip().lower()
                    if fleet.remove_spaceship(ship_name):
                        save_data(fleet)
                case "2":
                    ship_name = input("Nom du vaisseau : ").strip().lower()
                    last_name = input("Nom du membre à supprimer : ").strip().lower()
                    found = False
                    for ship in fleet.spaceships:
                        if ship.name.lower() == ship_name:
                            ship.remove_member(last_name)
                            save_data(fleet)
                            found = True
                            break
                    if not found:
                        print(f"Aucun vaisseau nommé {ship_name} n'a été trouvé.")
                case _:
                    print("Choix invalide.")

        case "3":  # Modifier
            print("\n=== MODIFIER ===")
            print("1. Modifier un vaisseau")
            print("2. Modifier la flotte")
            print("3. Modifier un membre d'un vaisseau")
            sub_choice = input("Votre choix : ")
            match sub_choice:
                case "1":
                    ship_name = input("Nom du vaisseau à modifier : ").strip().lower()
                    found = False
                    for ship in fleet.spaceships:
                        if ship.name.lower() == ship_name:
                            print("Que voulez-vous modifier ?")
                            print("1. Nom")
                            print("2. Type")
                            print("3. Condition")
                            sub_sub_choice = input("Votre choix : ")
                            match sub_sub_choice:
                                case "1":
                                    new_name = input("Nouveau nom : ")
                                    ship.update_spaceship(name=new_name)
                                case "2":
                                    new_type = input("Nouveau type (marchand/guerre) : ")
                                    ship.update_spaceship(shipType=new_type)
                                case "3":
                                    new_condition = input("Nouvelle condition : ")
                                    ship.update_spaceship(condition=new_condition)
                                case _:
                                    print("Choix invalide.")
                            save_data(fleet)
                            found = True
                            break
                    if not found:
                        print(f"Aucun vaisseau nommé {ship_name} n'a été trouvé.")
                case "2":
                    new_fleet_name = input("Nouveau nom de la flotte : ")
                    fleet.update_fleet(name=new_fleet_name)
                    save_data(fleet)
                case "3":
                    ship_name = input("Nom du vaisseau : ").strip().lower()
                    last_name = input("Nom du membre à modifier : ").strip().lower()
                    found = False
                    for ship in fleet.spaceships:
                        if ship.name.lower() == ship_name:
                            for member in ship.crew:
                                if member.last_name.lower() == last_name:
                                    print("Que voulez-vous modifier ?")
                                    print("1. Prénom")
                                    print("2. Nom")
                                    print("3. Genre")
                                    print("4. Âge")
                                    if isinstance(member, Operator):
                                        print("5. Rôle")
                                        print("6. Expérience")
                                        sub_sub_choice = input("Votre choix : ")
                                        match sub_sub_choice:
                                            case "1":
                                                new_first = input("Nouveau prénom : ")
                                                member.update_operator(first_name=new_first)
                                            case "2":
                                                new_last = input("Nouveau nom : ")
                                                member.update_operator(last_name=new_last)
                                            case "3":
                                                new_gender = input("Nouveau genre (homme/femme) : ")
                                                member.update_operator(gender=new_gender)
                                            case "4":
                                                new_age = int(input("Nouvel âge : "))
                                                member.update_operator(age=new_age)
                                            case "5":
                                                new_role = input("Nouveau rôle (pilote/technicien/commandant/armurier/entretien/marchand) : ")
                                                member.update_operator(role=new_role)
                                            case "6":
                                                new_exp = int(input("Nouvelle expérience : "))
                                                member.update_operator(experience=new_exp)
                                            case _:
                                                print("Choix invalide.")
                                    elif isinstance(member, Mentalist):
                                        print("5. Mana")
                                        sub_sub_choice = input("Votre choix : ")
                                        match sub_sub_choice:
                                            case "1":
                                                new_first = input("Nouveau prénom : ")
                                                member.update_mentalist(first_name=new_first)
                                            case "2":
                                                new_last = input("Nouveau nom : ")
                                                member.update_mentalist(last_name=new_last)
                                            case "3":
                                                new_gender = input("Nouveau genre (homme/femme) : ")
                                                member.update_mentalist(gender=new_gender)
                                            case "4":
                                                new_age = int(input("Nouvel âge : "))
                                                member.update_mentalist(age=new_age)
                                            case "5":
                                                new_mana = int(input("Nouveau mana (0-100) : "))
                                                member.update_mentalist(mana=new_mana)
                                            case _:
                                                print("Choix invalide.")
                                    save_data(fleet)
                                    found = True
                                    break
                            if found:
                                break
                    if not found:
                        print(f"Aucun membre nommé {last_name} n'a été trouvé dans le vaisseau {ship_name}.")
                case _:
                    print("Choix invalide.")

        case "4":  # Autres actions
            print("\n=== AUTRES ACTIONS ===")
            print("1. Afficher l'équipage d'un vaisseau")
            print("2. Vérifier la préparation d'un vaisseau")
            print("3. Afficher les statistiques de la flotte")
            print("4. Sauvegarder la flotte")
            print("5. Afficher la flotte")
            print("6. Faire agir un membre")
            sub_choice = input("Votre choix : ")
            match sub_choice:
                case "1":
                    ship_name = input("Nom du vaisseau : ").strip().lower()
                    found = False
                    for ship in fleet.spaceships:
                        if ship.name.lower() == ship_name:
                            ship.display_crew()
                            found = True
                            break
                    if not found:
                        print(f"Aucun vaisseau nommé {ship_name} n'a été trouvé.")
                case "2":
                    ship_name = input("Nom du vaisseau : ").strip().lower()
                    found = False
                    for ship in fleet.spaceships:
                        if ship.name.lower() == ship_name:
                            if ship.check_preparation():
                                print("Le vaisseau est prêt !")
                            else:
                                print("Le vaisseau n'est pas prêt.")
                            found = True
                            break
                    if not found:
                        print(f"Aucun vaisseau nommé {ship_name} n'a été trouvé.")
                case "3":
                    fleet.statistics()
                case "4":
                    save_data(fleet, "data.json")
                case "5":
                    try:
                        fleet = load_data("data.json")
                        for ship in fleet.spaceships:
                            ship.display_crew()
                    except FileNotFoundError:
                        print("Le fichier est introuvable.")
                case "6":
                    ship_name = input("Nom du vaisseau : ").strip().lower()
                    found = False
                    for ship in fleet.spaceships:
                        if ship.name.lower() == ship_name:
                            member_name = input("Nom du membre : ").strip().lower()
                            for member in ship.crew:
                                if member.last_name.lower() == member_name:
                                    if isinstance(member, Operator):
                                        member.act()
                                    elif isinstance(member, Mentalist):
                                        operator_name = input("Nom de l'opérateur à influencer : ").strip().lower()
                                        for op in ship.crew:
                                            if isinstance(op, Operator) and op.last_name.lower() == operator_name:
                                                member.act(op)
                                                break
                                        else:
                                            print("Opérateur non trouvé.")
                                    found = True
                                    break
                            if found:
                                break
                    if not found:
                        print(f"Aucun membre nommé {member_name} n'a été trouvé dans le vaisseau {ship_name}.")
                case _:
                    print("Choix invalide.")

        case "0":
            print("Au revoir 👋")
            break

        case _:
            print("Choix invalide, réessayez.")