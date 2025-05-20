total_games_played=int(input("Enter you total games played : "))
games_won=int(input("Enter the games you won : "))
games_lost=int(input("Enter the games you lost : "))
games_tie=total_games_played - games_won - games_lost

tp=(games_won*4) + (games_tie*2)
print(f"Total points : {tp}")