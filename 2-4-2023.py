# Takes in an array where player 1 plays against player 2, player 3 plays against player 4, etc.
# Returns an array half the size containing only the winners
def simulate_bracket(bracket):

    winners = []

    for i in range(0, len(bracket), 2): #(0, 2, 4, 6, 8) vs (0, 1, 2, 3, 4)
        player_one = bracket[i]
        player_two = bracket[i + 1]

        if player_one[1] > player_two[1]:
            winners.append(player_one)
        else:
            winners.append(player_two)

    return winners

print(simulate_bracket([['Larry', 6], ['Paul', 2], ['Sherley', 9], ['Winston', 3], ['Jeff', 1], ['Margret', 8], ['Eric', 6], ['Julia', 7], ['Leslie', 10], ['Marco', 4]]))

# Example:
# Input: [['Larry', 6], ['Paul', 2], ['Sherley', 9], ['Winston', 3], ['Jeff', 1], ['Margret', 8], ['Eric', 6], ['Julia', 7], ['Leslie', 10], ['Marco', 4]]
# Output: [['Larry', 6], ['Sherley', 9], ['Margret', 8], ['Julia', 7], ['Leslie', 10]]



# Remove all duplicates from an array
def remove_dups(arr):
    return

# Given 2 dice, return an array with all the possible values for the sums without duplicates
# Ex: all_sums(6, 10) should return [2, 3, 4, ..., 16] 
def all_sums(dice_1, dice_2):
    return

# Given 2 abnormal dice as arrays , list all possible values for the sums without duplicates
# Ex: all_sums_weird([3, 7, 8], [1, 2]) should return [4, 5, 8, 9, 10]
def all_sums_weird(dice_1, dice_2):
    return
