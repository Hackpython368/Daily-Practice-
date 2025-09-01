import random

CHOICES = ["snake", "water", "paper"]

# who_ beats who
WIN_MAP = {
    ("snake", "water"): "snake",
    ("water", "paper"): "water",
    ("paper", "snake"): "paper",
    }

def decide_winner(player, comp):
    if player == comp:
        return "tie"
    # order pair so it matches our WIN_MAP keys (a,b) where a!=b
    pair = (player, comp)
    if pair in WIN_MAP:
        return "player" if WIN_MAP[pair] == player else "computer"
    else:
        # pair reversed must be in WIN_MAP
        pair = (comp, player)
        return "computer" if WIN_MAP[pair] == comp else "player"

def play_round():
    while True:
        user_in = input("Choose snake / water / paper: ").strip().lower()
        if user_in in CHOICES:
            break
        print("Invalid choice. Try again.")
        
    comp = random.choice(CHOICES)
    result = decide_winner(user_in, comp)

    print(f"You chose: {user_in}  |  Computer chose: {comp}")
    if result == "tie":
        print("Result: It's a tie!")
    elif result == "player":
        print("Result: You win 🎉")
    else:
        print("Result: Computer wins 🤖")

    return result

def main():
    print("=== Snake • Water • Paper ===")
    print("First to 3 wins the match.\n")

    scores = {"player": 0, "computer": 0}
    while scores["player"] < 3 and scores["computer"] < 3:
        r = play_round()
        if r in ("player", "computer"):
            scores[r] += 1
        print(f"Score → You: {scores['player']} | Computer: {scores['computer']}\n")

        if scores["player"] > scores["computer"]:
            print("🏆 You won the match!")
        else:
            print("💻 Computer won the match. Better luck next time!")

if __name__ == "__main__":
    main()
