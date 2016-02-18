import string
#def checkMove(item):

#def killPiece(Position):
def initTable(table):
    for i in range(1,9):
        for key in string.ascii_lowercase[:8]:
            if i == 1:
                team = 1
                if key == 'a':
                    table[key+str(i)] = tower(key+str(i),team,"R{}(1)".format(team))
                elif key == 'h':
                    table[key+str(i)] = tower(key+str(i),team,"R{}(2)".format(team))
                else:
                    table[key+str(i)] = empty()
            elif i == 2:
                team = 1
                table[key+str(i)] = pawn(key+str(i),team,"P{}({})".format(team,ord(key)-96))
                # Na tabela ascii os caracteres estão em sequencia, como subtraimos um valor constante deles então \
                # obtemos uma sequencia de números crescente, no nosso caso começando do 1. ('a' em ascii = 97)
            elif i == 7:
                team = 2
                table[key+str(i)] = pawn(key+str(i),team,"P{}({})".format(team,ord(key)-96))
            else:
                table[key+str(i)] = empty()
def printTable(table):
    print("    ",end = "")
    for i in string.ascii_lowercase[:8]:
        print("{:^7s}".format(i), end = "")
    print("\n")
    for i in range(1,9):
        for key in string.ascii_lowercase[:8]:
            if key == 'a':
                print("{:<4s}".format(str(i)),end = "")
            print("{:^7s}".format(table[key+str(i)].name),end="")
            if key == 'h':
                print("{:>5s}".format(str(i)))
                print("")
    #print("")
    print("    ",end = "")
    for i in string.ascii_lowercase[:8]:
        print("{:^7s}".format(i), end = "")
    print("\n \n")
table = {
}
class piece(object):
    moveCount = 0
    def __init__(self,position,team,name):
        self.position = position
        self.team = team
        self.name = name
    def move(self,newPos):
        if self.checkMove(newPos):
            self.moveCount += 1
            aux = self.position
            self.position = newPos.lower()
            table[newPos] = self
            table[aux] = empty()
            return True
        else:
            return False
    def checkMove(self):
        pass
class pawn(piece):
    def checkMove(self,newPos):
        if self.position[0] == newPos[0]:
            if self.moveCount == 0:
                if ((int(self.position[1]) == int(newPos[1]) - 1 or int(self.position[1]) == int(newPos[1]) - 2) and checkBoard(self.team, newPos)):
                    return True
                else:
                    return False
            else:
                if int(self.position[1]) == int(newPos[1]) - 1 and checkBoard(self.team, newPos):
                    return True
                else:
                    return False
class tower(piece):
    pass
class knight(piece):
    pass
class bishop(piece):
    pass
class queen(piece):
    pass
class king(piece):
    pass
class empty(object):
    name = "X"
    team = 0
    def __init__(self):
        pass
def checkBoard(team, pos): # test if there is a friendly piece at a certain position and also kills enemy pieces there
    if table[pos].team == team :
        return False
    elif table[pos].team == 0:
        return True
    else:
        killPiece(pos)
        return True
def killPiece(pos):
    table[pos] = empty()
initTable(table)
printTable(table)
table["b2"].move("b4")
table["b4"].move("b5")
table["b5"].move("b6")
table["b6"].move("b7")
printTable(table)
del table
