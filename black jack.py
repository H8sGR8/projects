from random import randint
import os
def count (cards):
    points = 0
    AS = 0
    num = str()
    for card in cards:
        for j in range (0, card.index('-')):
            num += card[j]
        try:
            points += int(num)
            num = str()
        except ValueError:
            if (num == 'A'):
                AS += 1
                points += 11
                num = str()
            else:
                points += 10
                num = str()
    while (points > 21 and AS > 0):
        points -= 10
        AS -= 1
    return points
budget = 1000
table = int(input('1 to play, 0 to leave\n'))
while (table != 0):
    bet = 0
    play = 1
    play2 = 0
    d_points = 0
    s_points = 0
    p_points = 0
    deck = []
    player = []
    split = []
    dealer = []
    color = ['trefl', 'pik', 'kier', 'karo']
    number = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    for i in color:
        for j in number:
            deck.append(j + '-' + i)
    for i in range (2):
        x = randint(0, len(deck) - 1)
        dealer.append(deck[x])
        deck.pop(x)
        b = randint(0, len(deck) - 1)
        player.append(deck[b])
        deck.pop(b)
    os.system('cls')
    print('budget:',budget)
    while (bet <= 0 or bet>budget):
        bet = int(input('how much do you want to bet\n'))
    budget -= bet
    os.system('cls')
    print('budget:',budget, '\nbet:',bet, '\n',dealer[0], '\n', player, '\n', count(player))
    p_points = count(player)
    d_points = count(dealer)
    win = 0
    if (p_points == 21):
        win = 1
        budget += 0.5*bet
    else:
        a = int(input('1 to pass, 2 to hit, 3 to double, 4 to split\n'))
        if (a == 4 and player[0][0] == player[1][0]):
            budget -= bet
            split.append(player[1])
            player.pop(1)
            s_points = p_points = count(split)
            play2 = 1
            os.system('cls')
            print(budget, '\n',dealer[0], '\n',player, split,'\nmain\n', player)
        elif (a == 4 and player[0][0] != player[1][0]):
            a = int(input('cant split\n1 to pass, 2 to hit, 3 to double\n'))
        elif (a == 3 and bet <= budget):
            budget -= bet
            bet = 2*bet
            b = randint(0, len(deck) - 1)
            player.append(deck[b])
            deck.pop(b)
            p_points = count(player)
            play = 0
        elif(a == 3 and bet > budget):
            a = int(input('not enough money\n1 to pass, 2 to hit\n'))
    while (p_points < 21 and play == 1):
        if((len(player) > 2 and len(split) == 0) or (len(split) > 0)):
            a = int(input('1 to pass, 2 to hit\n'))
        if (a == 1):
            play = 0
        elif (a == 2):
            b = randint(0, len(deck) - 1)
            player.append(deck[b])
            deck.pop(b)
            p_points = count(player)
            os.system('cls')
            print('budget:',budget, '\nbet:',bet, '\n', player, '\n', count(player))
    if (len(split) > 0):
        print('splited\n', split)
        while (s_points < 21 and play2 == 1):
            a = int(input('1 to pass, 2 to hit\n'))
            if (a == 1):
                play2 = 0
            elif (a == 2):
                b = randint(0, len(deck) - 1)
                split.append(deck[b])
                deck.pop(b)
                s_points = count(split)
                os.system('cls')
                print('budget:',budget, '\nbet:',bet, '\n',dealer[0], '\n', split, '\n', count(split))
    if ((p_points <= 21 or (s_points <= 21 and len(split) > 0)) and win == 0):
        while (d_points <= 16):
            x = randint(0, len(deck) - 1)
            dealer.append(deck[x])
            deck.pop(x)
            d_points = count(dealer)
    d_points = count(dealer)
    os.system('cls')
    if((d_points > 21 or  p_points > d_points ) and p_points<=21):
        budget += 2 * bet
    elif(p_points == d_points):
        budget += bet
    else:
        pass
    if (len(split) > 0):
        if ((d_points > 21 or s_points > d_points) and s_points <= 21):
            budget += 2 * bet
        elif (s_points == d_points):
            budget += bet
        else:
            pass
    print('budget:',budget,'\nplayer\n',player,'\n',count(player))
    if (len(split) > 0):
        print('split\n', split, '\n', count(split))
    print('dealer\n', dealer, '\n', count(dealer))
    table = int(input('1 to play, 0 to leave\n'))
    if (budget <= 0):
        table = 0
os.system('cls')
print('you left the table with', budget,'$ so your bilance is', budget - 1000, '$')
