from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
import board_util as game
import finder
import random
import time
from collections import deque
#Based off of work from keon.io/deep-q-learning
gamma = .6
epsilon = 1.0
ep_min = .01
ep_dec = .995
learn = .001
action_size = 256
memory = deque(maxlen=2000)
score = 0
#under construction brain will be made smarter soon tm
model = Sequential()
model.add(Dense(64, input_shape=(3,)))
model.add(Dense(action_size))
model.compile(optimizer='adam',
              loss='logcosh',
              metrics=['accuracy'])
board = np.array(game.create_board())

def act(board):
    if np.random.rand() <= epsilon:
        return random.randrange(256)
    act_values = model.predict(board)
    print(act_values)
    return np.argmax(act_values[0])

#Need to look for more examples for calculating this
def targetQ(size):
    samp = random.sample(memory, size)
    for state, action, reward, next_state, done in samp:
        target = reward
        if not done:
            target = reward + gamma * np.amax(model.predict(next_state)[0])
        future = model.predict(state)
        future[0][action] = target
        model.fit(state, future, epochs=1, verbose=0)
    if epsilon > ep_min:
        epsilon *= ep_dec

def find_move(action):
    dir = action%4
    gem = action/64
    x = gem%8
    y = gem/8
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
    if nscore==score:
        return board, -1, False
    if nscore==0:
        #wait for level to transition/match if its real long
        time.sleep(5)
        nscore = finder.get_score()
        if nscore==score:
            return board, -1, False
        #gameover
        if nscore==0:
            return board, -1, True
    return game.create_board(), (nscore-score)/50, False

def run_game():
    for i in range(0,10):
        game.reset_game()
        score = 0
        board = np.array(game.create_board())
        runs = 0
        while(done!=True):
            runs += 1
            action = act(board)
            next_board, reward, done = find_move(action)
            memory.append((board, action, reward, next_board, done))
            board = next_board
            if runs%100==0:
                targetQ(20)
            if runs>=10000:
                done = True
        targetQ(32)

run_game()
#print(board)
