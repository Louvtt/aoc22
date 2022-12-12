VALUES = {
    # Rock | Paper | Scissors
    'A': 1, 'B': 2, 'C': 3,  # Left (oponnent / win,loose,draw)
    'X': 1, 'Y': 2, 'Z': 3   # right (player / opponnent)
}

ASSOC = [
    "Rock", "Paper", "Scissors"
]
ASSOC_PARTY = ["Loose", "Draw", "Win"]

if __name__ == "__main__":
    total_score = 0
    input = open("testinp.txt","r")
    input_list = input.readlines()

    for line in input_list:
        oppMove, _, partyState = line.strip()
        partyState = VALUES[partyState]
        oppMove    = VALUES[oppMove]
        
        # add party state score
        total_score += (partyState - 1) * 3 # 0 3 6
        
        # add symbol score
        play = oppMove
        if   partyState == 3: # Win
            play = (oppMove - 1)
            if play <= 0: play = 3
        elif partyState == 2: # Draw
            play = oppMove
        elif partyState == 1: # Loose
            play = (oppMove + 1) % 3 + 1
        
        print(f"'{line[:3]}' => You need to {ASSOC_PARTY[partyState-1]} : {ASSOC[oppMove-1]} vs {ASSOC[play-1]} [{(partyState - 1) * 3} + {play}]")
        total_score += play
        
    print(total_score)



