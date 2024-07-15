import os

def generate_invitations(template, attendees):
    # Vérification des types d'entrée
    if not isinstance(template, str):
        print("Erreur : le modèle doit être une chaîne de caractères.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        print("Erreur : la liste des participants doit être une liste de dictionnaires.")
        return

    # Vérification des entrées vides
    if not template:
        print("Erreur : le modèle est vide, aucun fichier de sortie généré.")
        return
    
    if not attendees:
        print("Aucune donnée fournie, aucun fichier de sortie généré.")
        return

    # Traitement des participants et génération des fichiers
    for index, attendee in enumerate(attendees, start=1):
        processed_template = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A")
        )
        
        # Nom du fichier de sortie
        output_filename = f"output_{index}.txt"
        
        # Écriture dans le fichier de sortie
        with open(output_filename, 'w') as output_file:
            output_file.write(processed_template)
        
        print(f"Invitation générée pour {attendee.get('name', 'N/A')} dans {output_filename}.")

