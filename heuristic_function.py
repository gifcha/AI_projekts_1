def heuristic_function(sequence, ai_score, opponent_score):
    """
    Evaluates the heuristic value of the current game state.
    :param sequence: List of integers representing the current number sequence.
    :param ai_score: Integer representing AI's current score.
    :param opponent_score: Integer representing the opponent's current score.
    :return: Heuristic value of the state.
    """
    N1, N2, N3 = 0, 0, 0  # Counts of different types of moves
    
    for i in range(len(sequence) - 1):
        pair_sum = sequence[i] + sequence[i + 1]
        if pair_sum > 7:
            N1 += 1  # Favorable move for AI
        elif pair_sum < 7:
            N2 += 1  # Can reduce opponent’s score
        else:  # pair_sum == 7
            N3 += 1  # Neutral move that gives both players points
    
    # Weights for heuristic components
    w1 = 1.5  # Weight for good moves (sum > 7)
    w2 = 1.0  # Weight for opponent-reducing moves (sum < 7)
    w3 = 0.5  # Weight for neutral moves (sum == 7)
    
    # Compute heuristic value
    H = (ai_score - opponent_score) + (w1 * N1) - (w2 * N2) + (w3 * N3)
    
    return H

# Example usage:
sequence = [3, 5, 2, 6, 4, 1, 9]  # Example game state
ai_score = 4
opponent_score = 3

heuristic_value = heuristic_function(sequence, ai_score, opponent_score)
print("Heuristic Value:", heuristic_value)