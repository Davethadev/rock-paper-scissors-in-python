import random
items = ['rock', 'paper', 'scissors']
score_board = {
    'player': 0,
    'computer': 0
}

def play_round(computer_selection, player_selection):
    if computer_selection == 'rock' and player_selection == 'paper':
        print('Player chose ' + player_selection + ' and Computer chose ' + computer_selection)
        score_board['player'] += 1
        print ('You win. Paper beats Rock')
        return "Computer score: " + str(score_board['computer']) + " Player score: " + str(score_board['player'])
    elif computer_selection == 'rock' and player_selection == 'scissors':
        print('Player chose ' + player_selection + ' and Computer chose ' + computer_selection)
        score_board['computer'] += 1
        print ('You lose. Rock beats Scissors')
        return "Computer score: " + str(score_board['computer']) + " Player score: " + str(score_board['player'])
    elif computer_selection == 'paper' and player_selection == 'rock':
        print('Player chose ' + player_selection + ' and Computer chose ' + computer_selection)
        score_board['computer'] += 1
        print ('You lose. Paper beats Rock')
        return "Computer score: " + str(score_board['computer']) + " Player score: " + str(score_board['player'])
    elif computer_selection == 'paper' and player_selection == 'scissors':
        print('Player chose ' + player_selection + ' and Computer chose ' + computer_selection)
        score_board['player'] += 1
        print ('You win. Scissors beats Paper')
        return "Computer score: " + str(score_board['computer']) + " Player score: " + str(score_board['player'])
    elif computer_selection == 'scissors' and player_selection == 'rock':
        print('Player chose ' + player_selection + ' and Computer chose ' + computer_selection)
        score_board['player'] += 1
        print ('You win. Rock beats Scissors')
        return "Computer score: " + str(score_board['computer']) + " Player score: " + str(score_board['player'])
    elif computer_selection == 'scissors' and player_selection == 'paper':
        print('Player chose ' + player_selection + ' and Computer chose ' + computer_selection)
        score_board['computer'] += 1
        print ('You lose. Scissors beats Paper')
        return "Computer score: " + str(score_board['computer']) + " Player score: " + str(score_board['player'])
    else:
        print('Player chose ' + player_selection + ' and Computer chose ' + computer_selection)
        print ("It's a draw")
        return "Computer score: " + str(score_board['computer']) + " Player score: " + str(score_board['player'])

def game():
    i = 0
    while i < 5:
        player_selection = input('Enter rock, paper or scissors: ')
        computer_selection = random.choice(items)
        print(play_round(computer_selection, player_selection))
        i += 1
    if score_board['computer'] > score_board['player']:
        print('COMPUTER WINS!')
    elif score_board['computer'] < score_board['player']:
        print('PLAYER WINS!')
    else:
        print('DRAW')
game()