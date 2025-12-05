from classes.Member import*
from classes.Operator import*
from classes.Mentalist import*
from classes.Spaceship import*
from classes.Fleet import*
import json 

"""bayta = Spaceship("Bayata", "marchand")
gaal_dornick = Operator ("Gaal", "Dornick", "femme", 34, "technicien")
bayta.append_member(gaal_dornick)
gaal_dornick.introduce_yourself()
bayta.remove_member("Dornick")
bayta.remove_member("Riose")  
bayta.display_crew()"""

pilote = Operator("Jean", "Dupont", "Homme", 35, "pilot")
technicien = Operator("Alice", "Martin", "Femme", 28, "technicien")
commandant = Operator("Bel", "Riose", "Homme", 48, "commandant")
mentaliste = Mentalist("Clara", "Durand", "Femme", 40)

# --- Création d'un vaisseau ---
bayta = Spaceship("Bayta", "marchand")
bayta.append_member(pilote)
bayta.append_member(technicien)
bayta.append_member(commandant)
bayta.append_member(mentaliste)

bayta.display_crew()

print("\n=== Vérification préparation ===")
if bayta.check_preparation():
    print("✅ Le vaisseau Bayta est prêt à partir !")
else:
    print("❌ Le vaisseau Bayta n'est pas prêt.")

print("\n=== Suppression d'un membre ===")
bayta.remove_member("Riose")
bayta.display_crew()
