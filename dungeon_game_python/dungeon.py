import logging
import random

logging.basicConfig(filename='game.log', level=logging.DEBUG)

CELLS = [(0,0),(0,1),(0,2),
         (1,0),(1,1),(1,2),
         (2,0),(2, 1),(2,2)]


def get_loc():
    monster = random.choice(CELLS)
    door = random.choice(CELLS)
    start = random.choice(CELLS)

    if monster == door or monster == start or door == start:
        return get_loc()

    return monster,door,start


def move_player(player, move):
    x, y = player

    if move == 'LEFT':
        y -= 1
    elif move == 'RIGHT':
        y += 1
    elif move == 'UP':
        x -= 1
    elif move == 'DOWN':
        x += 1
    return x, y


def get_moves(player):
    moves = ['LEFT','RIGHT', 'UP','DOWN']

    if player[1] == 0:
        moves.remove('LEFT')
    if player[1] == 2:
        moves.remove('RIGHT')
    if player[0] == 0:
        moves.remove('UP')
    if player[0] == 2:
        moves.remove('DOWN')
    return moves


def draw_map(player):
    print " _  _  _"
    tile = '|{}'

    for idx,cell in enumerate(CELLS):
        if idx in [0,1,3,4,6,7]:
            if cell == player:
                print tile.format('X'),
            else:
                print tile.format('_'),
        else:
            if cell == player:
                print tile.format('X|')
            else:
                print tile.format('_|')

monster, door, player = get_loc()
logging.info('monster: {}, door: {}, player: {}'.format(monster, door, player))
print "Welcome to the dungeon!"


while True:
    draw_map(player)
    moves = get_moves(player)
    print "You're currently in a room {}".format(player)
    print "You can move {}".format(moves)
    print "Enter QUIT to quit."

    move = raw_input("-->> : ").upper()
    if move == "QUIT":
        break

    if move in moves:
        player = move_player(player, move)
    else:
        print "** Walls are hard, stop walking into them! **"
        continue

    if player == door:
        print "You escaped!"
        break
    if player == monster:
        print "You were eaten by The Grull!"
        break


