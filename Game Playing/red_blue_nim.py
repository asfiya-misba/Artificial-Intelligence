# Asfiya Misba - 1002028239
# AI Assignment 2
import sys


class RedBlueNim:
    def __init__(self, redMarbles, blueMarbles, currentPlayer):
        self.redMarbles = redMarbles
        self.blueMarbles = blueMarbles
        if currentPlayer == 'computer':
            self.current_player = 1  # 1 is for computer, 2 is for human
        else:
            self.current_player = 2

    # Method to print the state of the game
    def print_game_state(self):
        print(f"Number of red marbles left: {self.redMarbles}")
        print(f"Number of blue marbles left: {self.blueMarbles}")

    # Method to check if the game is over
    def game_over(self):
        return self.redMarbles == 0 or self.blueMarbles == 0

    # Method to calculate the score
    def get_score(self):
        return 2 * self.redMarbles + 3 * self.blueMarbles

    # Method to make the move
    def make_move(self, pile, num):
        if pile == 'red':
            self.redMarbles -= num
        else:
            self.blueMarbles -= num
        if self.current_player == 1:
            player = 'human'
        if self.current_player == 2:
            player = 'computer'
        # if self.redMarbles == 0 or self.blueMarbles == 0:
            # print('{} has won the game! in make move'.format(player))

    # Method to check if the moves are valid
    def get_valid_moves(self):
        valid_moves = []
        if self.redMarbles > 0:
            valid_moves.append(('red', 1))
        if self.blueMarbles > 0:
            valid_moves.append(('blue', 1))
        return valid_moves

    # eval fn.
    def evaluate(self):
        if self.game_over():
            score_computer = self.get_score()
            score_human = self.get_score()
            if score_computer > score_human:
                return float('inf')
            elif score_human > score_computer:
                return float('-inf')
            else:
                return 0

        score = self.get_score()
        if self.current_player == 1:
            score *= -1
        return score

    # Method for minimax algo
    def minimax(self, depth, alpha, beta):
        if self.game_over() or depth == 0:
            return self.evaluate()

        if self.current_player == 1:  # Computer turn
            max_val = -sys.maxsize
            for move in self.get_valid_moves():
                self.make_move(move[0], move[1])
                self.current_player = 2
                val = self.minimax(depth - 1, alpha, beta)
                self.make_move(move[0], -move[1])
                self.current_player = 1
                max_val = max(max_val, val)
                alpha = max(alpha, val)
                if beta <= alpha:
                    break
            return max_val
        else:  # Human turn
            min_val = sys.maxsize
            for move in self.get_valid_moves():
                self.make_move(move[0], move[1])
                self.current_player = 1
                val = self.minimax(depth - 1, alpha, beta)
                self.make_move(move[0], -move[1])
                self.current_player = 2
                min_val = min(min_val, val)
                beta = min(beta, val)
                if beta <= alpha:
                    break
            return min_val

    # Method to decide the computer's move
    def get_computer_move(self, depth):
        best_move = None
        max_val = -float('inf')
        for move in self.get_valid_moves():
            self.make_move(move[0], move[1])
            self.current_player = 2
            val = self.minimax(depth - 1, -float('inf'), float('inf'))
            self.make_move(move[0], -move[1])
            self.current_player = 1
            if val > max_val:
                max_val = val
                best_move = move
        return best_move

    # Method to decide the winner
    # self.current_player is updated after each move.
    # this means that the winner will always be printed as the opposite of who actually won
    def get_winner(self):
        if self.current_player == 1:
            return 'human'
        elif self.current_player == 2:
            return 'computer'
        else:
            return None


def main():
    redMarbles = int(sys.argv[1])
    blueMarbles = int(sys.argv[2])
    firstPlayer = 'computer' if len(sys.argv) < 4 else sys.argv[3]
    depth = 10 if len(sys.argv) < 5 else int(sys.argv[4])
    game = RedBlueNim(redMarbles, blueMarbles, firstPlayer)
    if firstPlayer == 'human':
        human_turn = True
    else:
        human_turn = False

    while not game.game_over():
        game.print_game_state()

        if human_turn:
            valid_moves = game.get_valid_moves()
            while True:
                print('Your turn:')
                print('Valid moves:', valid_moves)
                pile = input('Enter pile (red/blue): ')
                num = int(input('Enter the number of marbles to remove: '))
                if (pile, num) in valid_moves:
                    break
                else:
                    print('Invalid move, please try again.')

            game.make_move(pile, num)
            human_turn = False
        else:
            print('Computer turn:')
            move = game.get_computer_move(depth)
            print('Computer removes {} {} marbles.'.format(move[1], move[0]))
            game.make_move(move[0], move[1])
            human_turn = True

    game.print_game_state()
    if game.current_player == 1:
        player = 'human'
    if game.current_player == 2:
        player = 'computer'
    print('{} won the game!'.format(player))
    print('Final score: {}'.format(game.get_score()))


if __name__ == '__main__':
    main()
