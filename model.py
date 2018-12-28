from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
import numpy as np
import board_util as game
import finder
import random
import time
from collections import deque
#Based off of work from keon.io/deep-q-self.learning
class BejewledBot():
    def __init__(self):
        self.gamma = .6
        self.epsilon = 1.0
        self.ep_min = .01
        self.ep_dec = .995
        self.learn = .001
        self.action_size = 256
        self.memory = deque(maxlen=2000)
        #under construction brain will be made smarter soon tm
        self.model = self._build_model()

    def _build_model(self):
        model = Sequential()
        model.add(Flatten())
        model.add(Dense(64))
        model.add(Dense(self.action_size))
        model.compile(optimizer='adam',
                      loss='logcosh',
                      metrics=['accuracy'])
        return model

    def act(self, board):
        if np.random.rand() <= self.epsilon:
            return random.randrange(256)
        print("guessing.....")
        act_values = self.model.predict(board)
        return np.argmax(act_values)

    #Need to look for more examples for calculating this going to use all values in memory as it is sparse
    def targetQ(self):
        print("training")
        for state, action, reward, next_state, done in self.memory:
            target = reward
            if not done:
                target = reward + self.gamma * np.amax(self.model.predict(next_state))
            future = self.model.predict(state)
            future[0][action] = target
            self.model.fit(state, future, epochs=1, verbose=0)
        if self.epsilon > self.ep_min:
            self.epsilon *= self.ep_dec

    def find_move(self,action,board,score):
        dir = action%4
        gem = action//4
        x = gem%8
        y = gem//8
        #print("Using action " + str(action))
        #print("moving gem " + str(gem))
        #print("mapped to location " + str(x) +"," + str(y))
        #print("in direction "+ str(dir))
        if dir == 0:
            r = game.move_up(x,y)
        elif dir == 1:
            r = game.move_left(x,y)
        elif dir == 2:
            r = game.move_down(x,y)
        else:
            r = game.move_right(x,y)
        if r==-1:
            return board, r, False
        #wait for move if applicable
        time.sleep(1)
        nscore = finder.get_score()
        print("score: " + str(nscore))
        trys = 0
        while nscore==-1 or nscore%50!=0:
            time.sleep(1)
            nscore = finder.get_score()
            print("score: " + str(nscore))
            trys += 1
            #giveup should eventually not need to do this but need to upgrade finder
            if trys == 10:
                nscore = 0
        if nscore==score:
            return board, -1, False
        if nscore==0:
            #wait for level to transition/match if its real long
            time.sleep(5)
            nscore = finder.get_score()
            if nscore==score:
                return board, -1, False
            #gameover
            if nscore<=0:
                return board, -1, True
        return np.expand_dims(np.array(game.create_board()),axis=0), (nscore-score)/50, False

    def run_game(self):

        for i in range(0,10):
            game.reset_game()
            score = 0
            board = np.expand_dims(np.array(game.create_board()),axis=0)
            self.model.predict(board)
            runs = 0
            done = False
            while(done!=True):
                runs += 1
                action = self.act(board)
                next_board, reward, done = self.find_move(action,board,score)
                self.memory.append((board, action, reward, next_board, done))
                board = next_board
                if runs%50==0:
                    self.targetQ()
                if runs>=10000:
                    done = True
            targetQ()
bot = BejewledBot()
bot.run_game()
#print(board)
