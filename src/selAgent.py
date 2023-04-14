import numpy as np


class Agent:

    def __init__(self, alpha=0.15, random_factor=0.2):
        self.state_History = [("None", 0)]  # state, reward
        self.alpha = alpha
        self.random_factor = random_factor

        # rewards table
        self.G = {}

    def init_reward(self, states):
        for i, row in enumerate(states):
            for j, col in enumerate(row):
                self.G[(j, i)] = np.random.uniform(low=1.0, high=0.1)

    def give_reward(self):
        pass
        # if the above the middle all fields have a value of 0 each round the agent will get a reward
        # unless if not depending how close to the border he is the more minus points he gets

    # def get_state_and_reward(self):
    #     return self.robot_position, self.give_reward()

    def updateStateHistory(self, state, reward):
        # each move will be saved
        self.state_History.append((state, reward))

    def learn(self):
        target = 0

        for prev, reward in reversed(self.state_history):
            self.G[prev] = self.G[prev] + self.alpha * (target - self.G[prev])
            target += reward

        self.state_history = []

        self.random_factor -= 10e-5  # decrease random factor each episode of play
