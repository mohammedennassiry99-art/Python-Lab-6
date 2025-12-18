notes = [10,18,19,9]
if not notes:
    print("la liste de notes est vide.")
    exit()
total = 0
nb_notes = len(notes);
print(nb_notes)
for note in notes:
    total += note  
moyenne = total / nb_notes
print(f"Moyenne : {moyenne:.2f}")

notes_bonus = [min(note + 1, 20) for note in notes]
print("Notes apres bonus :", notes_bonus)

seuil = 12
notes_valides = [note for note in notes if note >= seuil]

print(f"Notes ≥ {seuil} :", notes_valides) 