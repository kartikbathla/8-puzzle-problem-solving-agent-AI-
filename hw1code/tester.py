import sys
import puzz
search_algo =  sys.argv[1].split("-")[0]
heuristic = sys.argv[1].split("-")[1]
initial_state = [str(x) for x in sys.argv[2]]
final_state = [str(x) for x in sys.argv[3]]
puzz_board= puzz.EightPuzzleBoard(initial_state)
print(type( puzz_board.successors().values()))
for i in puzz_board.successors().values():    
    print(i)

