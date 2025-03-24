"""
    1. Novērtē pašreizējā spēles stāvokļa heiristisko vērtību.
    2. Mainīgais sequence: Veselu skaitļu saraksts, kas attēlo pašreizējo skaitļu secību.
    3. Mainīgais ai_score: Vesels skaitlis, kas attēlo AI pašreizējo rezultātu.
    4. Mainīgais opponent_score: Vesels skaitlis, kas apzīmē pretinieka pašreizējo rezultātu.
    5. return: Atgriež heiristisko vērtību.
"""

def heuristic_function(sequence, ai_score, opponent_score):

    N1, N2, N3 = 0, 0, 0  # Skaita dažādu veidu gājienus
    
    for i in range(len(sequence) - 1):
        pair_sum = sequence[i] + sequence[i + 1]
        if pair_sum > 7:
            N1 += 1  # Labvēlīgs solis AI
        elif pair_sum < 7:
            N2 += 1  # Var samazināt pretinieka punktu skaitu
        else:  # pair_sum == 7
            N3 += 1  # Neitrāls gājiens, kas dod punktus abiem spēlētājiem
    
    # Heiristisko komponentu svari
    w1 = 1.5  # Svars labām gajienam (summa > 7)
    w2 = 1.0  # Svars pretinieku samazināšanas gājieniem (summa < 7)
    w3 = 0.5  # Svars neitrālām kustībām (summa == 7)
    
    # Heiristisko vērtību apreķināšana
    H = (ai_score - opponent_score) + (w1 * N1) - (w2 * N2) + (w3 * N3)
    
    return H