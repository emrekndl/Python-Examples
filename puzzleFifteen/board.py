from copy import deepcopy
from os import system
from queue import Queue
from random import randint, seed

MAX_COL = 4
MAX_ROW = 4
SHUFFLE_MAGNITUDE = 20


class board:
    """ game board """

    def __init__(self):
        """ construct a board """

        self.goal = [[" 1", " 2", " 3", " 4"],
                     [" 5", " 6", " 7", " 8"],
                     [" 9", "10", "11", "12"],
                     ["13", "14", "15", "__"]]

        self.board1 = deepcopy(self.goal)

        self.empty_loc = [MAX_ROW - 1, MAX_COL - 1]
        #print(self.empty_loc)
        self.moves = {0:self.move_up, 1:self.move_right, 2:self.move_down, 3:self.move_left}

    def __repr__(self):
        """ represent the board """

        for i in range(MAX_ROW):
            for j in range(MAX_COL):
                print(self.board1[i][j], end=" ")
            print()

        # __repr__ must return something
        return ""

    def refresh(self):
        """ clear screen and print board """

        system("clear")
        print("Puzzle Fifteen\n")
        print(self)

        if self.board1 == self.goal:
            print("\nCongrats! You Won!")
            return False
        return True

    def shuffle(self):
        """ randommizes board """

        seed()
        for i in range(SHUFFLE_MAGNITUDE):
            m = randint(0, 3)
            self.moves[m](self.board1,self.empty_loc)

        #move the empty space to the right corner
        for i in range(MAX_ROW):
            self.moves[2](self.board1, self.empty_loc)

        for i in range(MAX_COL):
            self.moves[1](self.board1, self.empty_loc)

    def move(self, board1, empty_loc, x, y):
        """ makes legal move """

        #check legality of move
        if empty_loc[0] + x < 0 or empty_loc[0] + x > 3 or empty_loc[1] + y < 0 or empty_loc[1] + y > 3:
             return board1, empty_loc

        #swap
        board1[empty_loc[0]][empty_loc[1]], board1[empty_loc[0] + x][empty_loc[1] + y] = board1[empty_loc[0] + x][empty_loc[1] + y], board1[empty_loc[0]][empty_loc[1]]

        #update empty location
        empty_loc[0] += x # empty_loc[0] -> empty_row -> x
        empty_loc[1] += y # empty_loc[1] -> empty_col -> y

        return board1, empty_loc


    def move_up(self, board1, empty_loc):
        return self.move(board1, empty_loc, -1, 0) #x -> row | y -> col

    def move_right(self, board1, empty_loc):
        return self.move(board1, empty_loc, 0, 1)

    def move_down(self, board1, empty_loc):
        return self.move(board1, empty_loc, 1,  0)

    def move_left(self, board1, empty_loc):
        return self.move(board1, empty_loc, 0, -1)

    def solve(self):
        """ solves the game using Breath First Search algorithm """
        #self.board1 = deepcopy(self.goal)

        def successors(board1, empty_loc):
            board1_lst = [deepcopy(board1),deepcopy(board1),deepcopy(board1),deepcopy(board1)]
            empty_loc_lst = [list(empty_loc),list(empty_loc),list(empty_loc),list(empty_loc)]

            board1_lst[0], empty_loc_lst[0] = self.move_up(board1_lst[0], empty_loc_lst[0])
            board1_lst[1], empty_loc_lst[1] = self.move_right(board1_lst[1], empty_loc_lst[1])
            board1_lst[2], empty_loc_lst[2] = self.move_down(board1_lst[2], empty_loc_lst[2])
            board1_lst[3], empty_loc_lst[3] = self.move_left(board1_lst[3], empty_loc_lst[3])

            return [[board1_lst[0], empty_loc_lst[0], 0], [board1_lst[1], empty_loc_lst[1], 1], [board1_lst[2],
            empty_loc_lst[2], 2], [board1_lst[3], empty_loc_lst[3], 3]]


        searched = set()
        fringe = Queue()

        fringe.put({"board1": self.board1, "empty_loc": self.empty_loc, "path": []})

        while True:

            #quit if no solution is found
            if fringe.empty():
                return []

            #inspect cuurent node
            node = fringe.get()

            #quit if node contains goal
            if node["board1"] == self.goal:
                 return node["path"]

            #add current node to searched set: put children in fringe
            if str(node["board1"]) not in searched:
                searched.add(str(node["board1"]))
                for child in successors(node["board1"], node["empty_loc"]):
                    if str(child[0]) not in searched:
                        fringe.put({"board1": child[0], "empty_loc": child[1], "path": node["path"] +
                        [child[2]]})
