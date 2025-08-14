class Player:
    def __init__(self):
        self.recorded_move = []

    def RecordMove(self, move):
        self.recorded_move.append(move)
        return f"You make a move: {move}"
    
    def UndoMove(self):
        return f"You undo the move: {self.recorded_move.pop()}"
    
def MoveController():
    player = Player()
    
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    RESET = '\033[0m'
    
    function_table = """ Use number to do an action:
        1. Make a move
        2. Undo move
        3. Exit
    """
    
    request = ""
    print(function_table)
    request = input(f"{BLUE}Request number: {RESET}")
    
    while request != "3":
        match request:
            case "1":
                move_name = input(f"{BLUE}Move: {RESET}").strip()
                if not move_name:
                    print(f"{RED}Move can not be empty{RESET}")
                    request = ""
                    continue
                print(player.RecordMove(move_name))
                print(f'Movement history: {player.recorded_move}')
            case "2":
                print(player.UndoMove())
                print(f'Movement history: {player.recorded_move}')
            case _:
                print(f"{RED}Invalid request number. Please try again {RESET}")
        print(" ")
        request = input(f"{BLUE}Request number: {RESET}")
    print(f"{GREEN}Exit program.{RESET}")
    
MoveController()