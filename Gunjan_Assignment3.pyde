import os
import random
# path = os.getcwd()
RESOLUTION1 = 200
RESOLUTION2 = 400
NUM_ROWS = RESOLUTION2//20
NUM_COLS = RESOLUTION1// 20
BLOCK_WIDTH = RESOLUTION1/NUM_COLS
BLOCK_HEIGHT = RESOLUTION2/NUM_ROWS


class Block():
    def __init__(self):
        
        self.row = 0
        # Randomly generating the column while keeping row 0
        self.col = random.randint(0, NUM_COLS-1)
        self.key_handler={"LEFT":False, "RIGHT":False}
        # Rndomly assigning colour to the blocks
        self.color = random.choice([(255,51,52),(12,150,228),(30,183,66),(246,187,0),(76,0,153),(255,255,255),(0,0,0)])
        
        
    def display(self):
        
        # Displaying the block
        
        fill(*self.color)
        rect(self.col*BLOCK_HEIGHT, self.row*BLOCK_WIDTH, BLOCK_WIDTH , BLOCK_HEIGHT)
        self.update()
    
        
        
    def update(self):
        self.move_side()
        # Checking if the block can move down and assigning colour to cell
    
        if self.row < NUM_ROWS-1 and b.board[self.row+1][self.col]==" " :
            self.row += 1
            b.board[self.row][self.col] = self.color
        
        # Removing assigned colour from the previous block so that it does not hinder movement of other blocks
            b.board[self.row-1][self.col] = " "
            
    def move_side(self):
        
        # Conditions to block movement of blocks out of the board and to see if there is already a block on left and right it doesn't move
        
        if self.key_handler["LEFT"] == True and self.col > 0 and b.board[self.row][self.col-1]==" " :
            self.col-=1
            # b.board[self.row][self.col-1] = self.color
            # b.board[self.row][self.col] = " "
            
        elif self.key_handler["RIGHT"] == True and self.col < NUM_COLS - 1 and b.board[self.row][self.col + 1]== " " :
            self.col+=1
            # b.board[self.row][self.col+1] = self.color
            # b.board[self.row][self.col] = " "
    
class Game():
    
    def __init__(self ):
   
   # Creating a list of all the blocks and appending them into it
   
        self.blocks = []
        self.block = Block()
        self.blocks.append(Block())
        self.board=[]
        self.speed=0
        self.score=0
        
        # Creating a 2D board
        
        for i in range(NUM_ROWS):
            list1=[]
            for j in range(NUM_COLS):
                list1.append(" ")
            self.board.append(list1)
            
            
        
    def display(self):
        
        # Displaying score 
        
    
        textSize(15)
        fill(0)
        text("Score:" + str(self.score ), 130 , 20)
        
        # Displaying grid lines
        
        for i in range(NUM_COLS):
                line(i*BLOCK_WIDTH , 0 , i*BLOCK_WIDTH, RESOLUTION2 )
        for j in range(NUM_ROWS):
                line(0 , j*BLOCK_HEIGHT , RESOLUTION2, j*BLOCK_HEIGHT)
                
        # Calling Block class functions for all the blocks added to list
                
        for block in self.blocks:
            block.display()
        self.add_block()
        self.match_block()
        self.terminate()
        self.update_speed()
         
        # Generating and appending a new block if previous one has got stacked or reached bottom
            
    def add_block(self):
   
        last_block=self.blocks[-1]  
        if last_block.row == NUM_ROWS-1 or self.board[last_block.row +1][last_block.col] !=" " :
            new_block=Block()
            self.blocks.append(new_block) 
        
           # Updating speed of the block 
           
    def update_speed(self):
        self.speed += 0.25 * len(self.blocks)  
        self.speed = max(self.speed, 4.0)
    
    # If 4 blocks of same color matches then player earns a point and spped truns 0
    
    def match_block(self):
   
    
         if self.board[self.blocks[-1].row][self.blocks[-1].col]== self.board[self.blocks[-1].row+1][self.blocks[-1].col] == self.board[self.blocks[-1].row+2][self.blocks[-1].col] == self.board[self.blocks[-1].row+3][self.blocks[-1].col]:
            self.board[self.blocks[-1].row][self.blocks[-1].col]=" "
            self.board[self.blocks[-1].row+1][self.blocks[-1].col]=" "
            self.board[self.blocks[-1].row+1][self.blocks[-1].col]=" "
            self.board[self.blocks[-1].row+1][self.blocks[-1].col]=" "
            
            self.speed= 0 
            self.score= 1
            
            
        # If a column of all the rows is filled then game terminates
        
    def terminate(self):
        for j in range(NUM_COLS):
            if all(self.board[i][j] != " " for i in range(NUM_ROWS)) :
     
                textSize(25)
                fill(0)
                text("GAME OVER" , 50, 180)
                textSize(20)
                fill(0)
                text("Score:" + str(self.score) , 75 , 250)
                noLoop()
            

b=Game()
# a=Block() 
def setup():
    global a,b
    size(RESOLUTION1,RESOLUTION2)

def draw():

    # background(210)
    # frameRate(10)
    if frameCount%(max(1, int(8 - b.speed)))==0 or frameCount==1: 
        background(210)

        b.display()


    
def keyPressed():
    if keyCode == LEFT:
        b.blocks[-1].key_handler["LEFT"] = True

        
    elif keyCode == RIGHT:
        b.blocks[-1].key_handler["RIGHT"] = True
    
        
def keyReleased():
    if keyCode == LEFT:
        b.blocks[-1].key_handler["LEFT"] = False
        # a.key_handler[LEFT] = False
        
    elif keyCode == RIGHT:
        b.blocks[-1].key_handler["RIGHT"] = False
        # a.key_handler[RIGHT] = False
        
        
# Restart Game after clicking mouse

def mouseClicked():
    global game
    game=Game()
    
game=Game()
