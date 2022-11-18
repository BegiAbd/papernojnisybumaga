import random
choice = ['k', 'n','b']



def choice():
    if t == 'k':
        print('kamen')
    elif t== 'b':
        print('bumaga')
    elif t == 'n':
        print('nojnisy')

def main():
    while True:
        turn = input("Please enter your turn: ('k','n','b):").lower()
        if turn == exit:
            break
        else:
            check_ans(turn)
        c_turn = random.choice(choice)
        ckeck_ans(c_turn)

    if turn =='k' and c_turn == 'n' or turn == 'b' and c_turn == 'k' or turn == 'n' and c_turn == 'b':
        print('you win')
    elif c_turn == 'k' and turn == 'n' or c_turn == 'b' and turn == 'k' or c_turn == 'n' and turn == 'b':
        print('comp win')
main()
# def main():
#     pass
# main()
