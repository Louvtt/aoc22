def get_priority(letter):
    if letter >= 'a' and letter <= 'z':
        return ord(letter) - ord('a') + 1
    if letter >= 'A' and letter <= 'Z':
        return ord(letter) - ord('A') + 27
    return 0

if __name__ == "__main__":
    total_score = 0
    input = open("input.txt","r")
    input_list = input.readlines()

    total_priority = 0
    
    for rucksack_i in range(0, len(input_list), 3):
        group1 = input_list[rucksack_i + 0]
        group2 = input_list[rucksack_i + 1]
        group3 = input_list[rucksack_i + 2]

        for letter in group1:
            if letter in group2:
                if letter in group3:
                    lp = get_priority(letter)
                    # print(f"{letter} value is {lp}")
                    total_priority += lp
                    break
    
    print(total_priority)