import random

def player(prev_play, opponent_history=[]):
    if not prev_play:
        return random.choice(["R", "P", "S"])

    opponent_history.append(prev_play)

    move_counts = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        move_counts[move] += 1

    most_frequent_move = max(move_counts, key=move_counts.get)

    
    recent_games = len(opponent_history)
    random_threshold = 0.5 + (recent_games / 200)  

   
    win_rate_threshold = 0.6
  

    if random.random() < random_threshold or random.random() > win_rate_threshold:
        return random.choice(["R", "P", "S"])
    else:
        return {"R": "P", "P": "S", "S": "R"}[most_frequent_move]

prev_play = "R"
opponent_history = ["R", "P", "S", "R", "R", "P", "S", "R", "S", "S"]
next_move = player(prev_play, opponent_history)
print("Next move:", next_move)
