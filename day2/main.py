import sys

if len(sys.argv) == 1:
    print('Missing file name argument!')
    exit()

def rock_paper_scissors_score(player_a_move: str, player_b_move: str) -> int:
    """Return the score of a rock-paper-scissors match according to the
    Advent of Code 2022's day 2 part 1 strategy guide.

    A win gives 6 points, a draw gives 3 points, and a loss gives 0 points.
    There are also additional points for the move selected:
        A / X - Rock (1 point)
        B / Y - Paper (2 points)
        C / Z - Scissors (3 points)

    Args:
        player_a_move: Move of player A
        player_b_move: Move of player B

    Returns:
        Score of the match considering the move selected and the result of the match.
    """

    score = 0

    match player_b_move:
        case 'X':
            result = 3 if player_a_move == 'A' else 6 if player_a_move == 'C' else 0

            score += 1 + result
                    
        case 'Y':
            result = 3 if player_a_move == 'B' else 6 if player_a_move == 'A' else 0

            score += 2 + result
        
        case 'Z':
            result = 3 if player_a_move == 'C' else 6 if player_a_move == 'B' else 0

            score += 3 + result

    return score

def rock_paper_scissors_top_secret_score(player_a_move: str, player_b_move: str) -> int:
    """Return the score of a rock-paper-scissors match according to the
    Advent of Code 2022's day 2 part 2 strategy guide.

    A win gives 6 points, a draw gives 3 points, and a loss gives 0 points.
    Player B's move now represents how the match needs to end:
        X - Loss (0 points)
        Y - Draw (3 points)
        Z - Win (6 points)

    There are also additional points for the move selected:
        A - Rock (1 point)
        B - Paper (2 points)
        C - Scissors (3 points)

    Args:
        player_a_move: Move of player A
        player_b_move: Move of player B

    Returns:
        Score of the match considering the move selected and the result of the match.
    """

    move_for_result = ''

    match player_a_move:
        case 'A':
            move_for_result = 'Z' if player_b_move == 'X' else 'X' if player_b_move == 'Y' else 'Y'

        case 'B':
            move_for_result = 'X' if player_b_move == 'X' else 'Y' if player_b_move == 'Y' else 'Z'

        case 'C':
            move_for_result = 'Y' if player_b_move == 'X' else 'Z' if player_b_move == 'Y' else 'X'

    return rock_paper_scissors_score(player_a_move, move_for_result)

total_score = 0
top_secret_score = 0

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    lines = f.readlines()

    for line in lines:
        total_score += rock_paper_scissors_score(line[0], line[2])
        top_secret_score += rock_paper_scissors_top_secret_score(line[0], line[2])

print('Total score according to the strategy guide is {}'.format(total_score))
print('Total score according to the ultra top secret strategy guide is {}'.format(top_secret_score), end='')