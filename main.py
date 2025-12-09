from classes.Member import *
from classes.Operator import *
from classes.Mentalist import *
from classes.Spaceship import *
from classes.Fleet import *
import json, ast

def save_data(fleet, file_name="data.json"):
    json_string = json.dumps(fleet, default=lambda o: o.__dict__, indent=4)
    json_dict = ast.literal_eval(json_string)
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(json_dict, file, indent=4)
    print("✅ Flotte sauvegardée dans", file_name)

def afficher_vaisseau(ship, fleet_name):
    print(f"\n🚀 {ship.name} ({ship.shipType}, {ship.condition})")
    # Construire une liste des noms de l'équipage
    noms = [f"{m.first_name} {m.last_name}" for m in ship.crew]
    print("   Équipage :", ", ".join(noms))
    print(f"   ✅ Vaisseau {ship.name} ajouté dans la flotte {fleet_name}")

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

        # --- Affichage formaté ---
        print(f"\n{ship.name} ({ship.shipType}, {ship.condition})")
        for member in ship.crew:
            role = getattr(member, "role", "inconnu")
            if member.gender == "femme":
                print(f"- {member.first_name} {member.last_name} est une femme de {member.age} ans, son rôle est : {role}")
            elif member.gender == "homme":
                print(f"- {member.first_name} {member.last_name} est un homme de {member.age} ans, son rôle est : {role}")
            else:
                print(f"- {member.first_name} {member.last_name} ({member.gender}) de {member.age} ans, rôle : {role}")

    print("\n✅ Flotte chargée depuis", file_name)
    return fleet

try:
    fleet = load_data("data.json")
except FileNotFoundError:
    print("Aucun fichier data.json trouvé. Création d'une flotte vide.")
    fleet = Fleet("Galactica")

# === Menu principal ===
while True:
    print("\n=== MENU PRINCIPAL ===")
    print("1. Créer un vaisseau")
    print("2. Ajouter un membre à un vaisseau")
    print("3. Afficher l'équipage d'un vaisseau")
    print("4. Supprimer un membre d'un vaisseau")
    print("5. Vérifier la préparation d'un vaisseau")
    print("6. Afficher les statistiques de la flotte")
    print("7. Sauvegarder la flotte")
    print("8. Charger une flotte")
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
            found = False
            for ship in fleet.spaceships:
                if ship.name == ship_name:
                    first_name = input("Prénom : ")
                    last_name = input("Nom : ")
                    gender = input("Genre (homme/femme) : ")
                    age = int(input("Âge : "))
                    role = input("Rôle (pilote/technicien/commandant) : ")
                    crew_member = Operator(first_name, last_name, gender, age, role)
                    ship.append_member(crew_member)
                    found = True
                    break
            if not found:
                print(f"Aucun vaisseau nommé {ship_name} n'a été trouvé.")

        case "3":
            ship_name = input("Nom du vaisseau : ")
            found = False
            for ship in fleet.spaceships:
                if ship.name == ship_name:
                    ship.display_crew()
                    found = True
                    break
            if not found:
                print(f"Aucun vaisseau nommé {ship_name} n'a été trouvé.")

        case "4":
            ship_name = input("Nom du vaisseau : ")
            last_name = input("Nom du membre à supprimer : ")
            found = False
            for ship in fleet.spaceships:
                if ship.name == ship_name:
                    ship.remove_member(last_name)
                    found = True
                    break
            if not found:
                print(f"Aucun vaisseau nommé {ship_name} n'a été trouvé.")

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
                print(f"Aucun vaisseau nommé {ship_name} n'a été trouvé.")

        case "6":
            fleet.statistics()

        case "7":
            save_data(fleet, "data.json")

        case "8":
            try:
                fleet = load_data("data.json")
            except FileNotFoundError:
                print("Le fichier data.json est introuvable.")

        case "0":
            print("Au revoir 👋")
            break

        case _:
            print("Choix invalide, réessayez.")