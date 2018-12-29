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
        self.score = 0

    def _build_model(self):
        model = Sequential()
        model.add(Flatten())
        model.add(Dense(224, activation='elu'))
        model.add(Dense(self.action_size))
        model.compile(optimizer='adam',
                      loss='logcosh',
                      metrics=['accuracy'])
        return model

    def act(self, board):
        if np.random.rand() <= self.epsilon:
            return random.randrange(256), False
        act_values = self.model.predict(board)
        return np.argmax(act_values), True

    #Need to look for more examples for calculating this going to use all values in memory as it is sparse
    def targetQ(self):
        print()
        for state, action, reward, next_state, done in self.memory:
            target = reward
            if not done:
                target = reward + self.gamma * np.amax(self.model.predict(next_state))
            future = self.model.predict(state)
            future[0][action] = target
            self.model.fit(state, future, epochs=1, verbose=0)
        if self.epsilon > self.ep_min:
            self.epsilon *= self.ep_dec

    def find_move(self, action, lboard):
        dir = action%4
        gem = action//4
        x = gem%8
        y = gem//8
        go = game.check_move(x,y,dir,lboard)
        if go != True:
            return -1, False
        #print("Coordinates: " + str((x,y)))
        #print("Direction: " + str(dir))
        #print("Valid Move: " + str(go))
        if dir == 0:
            r = game.move_up(x,y)
        elif dir == 1:
            r = game.move_left(x,y)
        elif dir == 2:
            r = game.move_down(x,y)
        else:
            r = game.move_right(x,y)
        if r==-1:
            return -1, False
        #wait for move if applicable still cleaning this up
        time.sleep(1)
        nscore1 = finder.get_score()
        nscore2 = 0
        trys = 0
        #wait for score to update if possible
        while nscore1!=nscore2:
            time.sleep(1)
            nscore2 = nscore1
            nscore1 = finder.get_score()
            trys += 1
            #giveup should eventually not need to do this but need to upgrade finder
            if trys == 20:
                nscore1 = 0
        if nscore1==self.score:
            print("No Change Move")
            return -1, False
        if nscore1==0:
            #wait for level to transition/match if its real long
            time.sleep(10)
            nscore1 = finder.get_score()
            #gameover
            if nscore1 <= 0:
                print("gameover")
                return -1, True
        if nscore1 > self.score:
            reward = (nscore1-self.score)/10
            self.score = nscore1
            print("Reward: " + str(reward))
            return reward, False
        else:
            #TODO understand when this is getting called, probably a problem with finder
            #Temp solution set score to whatever is registering
            print("Scores are: " + this.score + " New " + nscore1)
            #reset score to get better metrics and give no points to prevent bad training
            self.score = nscore1
            return 0, False
    def run_game(self):

        for i in range(0,10):
            game.reset_game()
            self.score = 0
            board, lboard = game.create_board()
            board = np.expand_dims(np.array(board),axis=0)
            self.model.predict(board)
            runs = 0
            done = False
            gflag = False
            gs = 0
            rm = 0
            while(done!=True):
                runs += 1
                action, gflag = self.act(board)
                reward, done = self.find_move(action,lboard)
                next_board, lboard = game.create_board()
                next_board = np.expand_dims(np.array(next_board),axis=0)
                self.memory.append((board, action, reward, next_board, done))
                board = next_board
                if reward > 0 and gflag:
                    gs += 1
                    print("Successful Guess: " + str(gs))
                elif reward > 0:
                    rm += 1
                    print("Random Match: " + str(rm))
                elif gflag:
                    print("Bad Guess")
                if runs%40==0:
                    print("Training")
                    self.targetQ()
                if runs>=10000:
                    done = True
            self.targetQ()
bot = BejewledBot()
bot.run_game()
#print(board)
