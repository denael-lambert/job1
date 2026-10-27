def arrondir_notes(notes):
    
    resultat = []
 
    for note in notes:
        if note >= 40:
            reste = note % 5
        
            if reste >= 3:
                note = note + (5 - reste)
        resultat.append(note)
 
    return resultat

print(arrondir_notes([83, 82,88,89,79])) 