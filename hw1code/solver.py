import sys 
import puzz

def misplaced_tile_count(board,goal_state ):
    count =0 
    index =0 
    for i in board._board: 
        if (int(i)!=int(goal_state[index])):
            count+=1
        index+=1
    return count         

def distance_covered( board2,explored_queue):  
    explored_queue.append(board2)
    exp = explored_queue 
    explored_queue.pop(-1)
    i =  len(exp)-2
    while i > 0:
       
        if (not(exp[i+1] in list(filter(None,exp[i].successors().values())))):
            exp.pop(i)
        i=i-1       
    return len(exp)-1    

def manhattan_distance(board,goal_state):
    distance= 0 
    inde= 0
    for i in board._board:
        xcur = int(inde)%3
        ycur = int(inde/3)
        
        xact = int(goal_state.index(i))%3
        yact=int(goal_state.index(i)/3)
        distance = distance + abs(xcur-xact) + abs(ycur-yact)
        inde+=1 
    return distance

def solution(explored_queue, frontiercount,exploredcount):
 
    i =  len(explored_queue)-2
    while i > 0:
       
        if (not(explored_queue[i+1] in list(filter(None,explored_queue[i].successors().values())))):
            explored_queue.pop(i)
        i=i-1    
    
    
    print("start", explored_queue[i],sep ='\t')
    for i in range(1,len(explored_queue)):
        children = explored_queue[i-1].successors()
        childrenf ={k: v for k, v in children.items() if v is not None}
        print(list(childrenf.keys())[list(childrenf.values()).index(explored_queue[i])] ,str(explored_queue[i]),sep ='\t')   



    print("path cost: "+ str(len(explored_queue)-1))
    print("frontier: "+ str(frontiercount))
    print("explored: "+ str(exploredcount))
            
def get_next_node(search_algo, queue, explored_queue,heuristic,goal ):
    if (search_algo!="astar"):
        if( heuristic==""):
            return  queue.pop(0)   
        elif (heuristic=="manhat"):
            min_index = 0
            counter=0 
            min_manhattan = 10000
            for i in queue[1:]:
                counter+=1
                if (manhattan_distance(i,goal)<min_manhattan):
                    min_manhattan=manhattan_distance(i,goal)
                    min_index = counter 
            return queue.pop(min_index)
        elif (heuristic=="count") :
            min_index = 0
            counter = 0 
            min_tile_count = 10
            for i in queue[1:]:
                counter +=1
                if (misplaced_tile_count(i,goal)<min_tile_count):
                    min_tile_count=misplaced_tile_count(i,goal )
                    min_index = counter
            return queue.pop(min_index)
        else :
            print("Invalid heuristic") 
    else :  
        if (heuristic=="manhat"):
            min_index = 0
            counter =-1 
            min_manhattan = 100000
            for i in queue:
                counter+=1
                val = manhattan_distance(i,goal)+distance_covered(i,explored_queue)
                if (val<min_manhattan):
                    min_manhattan=val 
                    min_index = counter
            return queue.pop(min_index)
        elif (heuristic=="count") :
            min_index = 0
            counter =-1
            min_tile_count = 100000
            for i in queue:
                counter +=1 
                val = misplaced_tile_count(i,goal )+distance_covered(i,explored_queue)
                if (val<min_tile_count):
                    min_tile_count=val
                    min_index = counter
            return queue.pop(min_index)
        else :
            print("Invalid heuristic") 
def search(search_algo, heuristic ,initial_state,final_state):
    exploredcount =0 
    frontiercount=0 
    puzz_board= puzz.EightPuzzleBoard(initial_state)
    frontier = []
    frontier.append(puzz_board)
    frontiercount+=1
    explored =[]

    while (len(frontier)>0 and len(explored)<100000 ):

        node = get_next_node(search_algo,frontier,explored,heuristic, final_state)

        explored.append(node)
        exploredcount+=1

        if (node._board==final_state):            
            return solution(explored, frontiercount,exploredcount)
       
        children =node.successors().values()   
        children=list(filter(None, children)) 
        for n in children:
            flag =0 
            if (type(n)==None):
                flag=1
            for i in frontier :
                if (n==i):
                    #print(type(i))
                    #print("same")
                    flag=1
            for i in explored:
                if (n==i):
                    #print("same")
                    flag=1        
          
            if flag==0:
                #print("added")
                #print(n._board)
                frontier.append(n)   
                frontiercount+=1  
    return "No solution found"


search_algo =  sys.argv[1].split("-")[0]
heuristic= ""
if (len(sys.argv[1].split("-"))>1):
    heuristic = sys.argv[1].split("-")[1]

initial_state = sys.argv[2]
final_state = [str(x) for x in sys.argv[3]]
search(search_algo, heuristic ,initial_state,final_state)