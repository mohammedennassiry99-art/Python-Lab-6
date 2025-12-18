notes = [10, 18, 19, 9, 15, 7.5, 12]
seuil = 12

lignes = []
lignes.append("=== Rapport des notes ===")


if not notes:
     print("la liste de notes est vide.")
     exit()
else:
    nb_notes = len(notes)
    lignes.append(f"Nombre d'etudiants : {nb_notes}")
    lignes.append(f"Notes originales : {notes}")

    
    moyenne_initiale = sum(notes) / nb_notes

    notes_bonus = [min(note + 1, 20) for note in notes]
    moyenne_bonus = sum(notes_bonus) / nb_notes

    notes_valides = [note for note in notes if note >= seuil]



   
    validation = []
    rattrapage = []
   

    for note in notes:
        if note >= 12:
            validation.append(note)
        elif note >= 10:
            rattrapage.append(note)
        

    
    top_3 = sorted(notes, reverse=True)[:3]

    # Mon Rapport synthèse 
    lignes.append(f"Moyenne initiale : {moyenne_initiale:.2f}")
    lignes.append(f"Moyenne après bonus : {moyenne_bonus:.2f}")
    lignes.append(f"Notes après bonus : {notes_bonus}")
    lignes.append(f"Notes ≥ {seuil} : {notes_valides} ({len(notes_valides)} étudiants)")

    lignes.append(f"Top 3 des notes : {top_3}")

    lignes.append("Détails par étudiant :")
    for index, note in enumerate(notes, start=1):
        bonus = notes_bonus[index - 1]
        lignes.append(
            f"  Étudiant {index:02d} — note {note:>5.2f} → bonus {bonus:>5.2f}"
        )

rapport = "\n".join(lignes)
print(rapport)
