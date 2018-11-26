t1 = [ (1,2), (3,4), (5,6), (7,8), (9,10), (11,12) ]
t2 = [ (3,4), (11,12) ]
set(t2).issubset(t1)
# returns true

# or equivalent use '<=' so
set(t2) <= set(t1)
# returns true

    # BS1 = [[0,3,1],[0,4,1],[0,5,1]]
    # BS2 = [[1,8,1],[2,8,1],[3,8,1],[4,8,1]]
    # BS3 = [[4,3,1],[5,3,1]]
    # BS4 = [[7,6,1],[7,7,1],[7,8,1]]
    # BS5 = [[8,0,1],[8,1,1],[8,2,1],[8,3,1],[8,4,1]]

    # BS1 = (0, 3), (0, 4), (0, 5)
    # BS2 = (1, 8), (2, 8), (3, 8), (4, 8)
    # BS3 = (4, 3), (5, 3)
    # BS4 = (7, 6), (7, 7), (7, 8)
    # BS5 = (8, 0), (8, 1), (8, 2), (8, 3), (8, 4)

        # if set(BS1) <= set(answerlist_matrix) : 
        #     print("You bombed Battle ship 1 !!!")
        # if set(BS2) <= set(answerlist_matrix) : 
        #     print("You bombed Battle ship 2 !!!")
        # if set(BS3) <= set(answerlist_matrix) : 
        #     print("You bombed Battle ship 3 !!!")
        # if set(BS4) <= set(answerlist_matrix) : 
        #     print("You bombed Battle ship 4 !!!")
        # if set(BS5) <= set(answerlist_matrix) : 
        #     print("You bombed Battle ship 5 !!!")