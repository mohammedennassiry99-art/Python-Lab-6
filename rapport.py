notes = [10,18,19,9,15,7.5,12]
nb_notes = len(notes);
moyenne_initiale = sum(notes) / nb_notes
notes_bonus = [min(note + 1, 20) for note in notes]
moyenne_bonus = sum(notes_bonus) / len(notes_bonus)
seuil = 12
notes_valides = [note for note in notes if note >= seuil]
lignes = []
lignes.append("=== Rapport des notes ===")
lignes.append(f"Nombre d'étudiants : {nb_notes}")
lignes.append(f"Notes originales : {notes}")
lignes.append(f"Notes après bonus : {notes_bonus}")
lignes.append(f"Moyenne initiale : {moyenne_initiale:.2f}")
lignes.append(f"Moyenne après bonus : {moyenne_bonus:.2f}")
lignes.append(f"Notes ≥ {seuil} : {notes_valides} (soit {len(notes_valides)} étudiants)")
lignes.append("Détails par étudiant :")
for index, note in enumerate(notes, start=1):
    bonus = notes_bonus[index - 1]
    lignes.append(f"  Étudiant {index:02d} — note {note:>5.2f} → bonus {bonus:>5.2f}")

rapport = "\n".join(lignes)
print(rapport)