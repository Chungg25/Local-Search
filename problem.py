import numpy as np
import matplotlib.pyplot as plt
import cv2
import random


class Problem:
    def __init__(self, filename, parent=None):
        self.filename = filename
        self.load_state_space()
        self.parent = parent

    def load_state_space(self):
        img = cv2.imread(self.filename, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        img = cv2.GaussianBlur(img, (5, 5), 0)
        self.h, self.w = img.shape
        self.X = np.arange(self.w)
        self.Y = np.arange(self.h)
        self.Z = img

    def evaluation(self, x, y):
        return self.Z[y, x] 

    def is_goal(self, current):
        for i in current:
            _, _, z, _ = i
            if z == np.max(self.Z):
                return True
        return False
    
    #jdnsd
    
    def find_goal(self, current):
        for i in current:
            _, _, z, _ = i
            if z == np.max(self.Z):
                return i
    
    def find_path(self, goal, state_start):
        best_path = []
        while len(goal) != 0:
            x, y, z, parent = goal
            best_path.insert(0, (x, y, z))
            goal = parent
            if isinstance(goal, tuple) == False:
                x, y, z, t = state_start
                best_path.insert(0, (x,y,z))
                break
        return best_path
    
    def get_neighbors(self, state):
        x, y, z, _ = state
        neighbors = []
        for dx in [0]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < len(self.X) and 0 <= new_y < len(self.Y):
                    neighbors.append((new_x, new_y, self.evaluation(new_x, new_y), state))
        return neighbors

    def random_state(self):
        x, y = random.choice(list(zip(self.X, self.Y)))
        z = self.evaluation(x, y)
        return (x, y, z, self)
    
    def random_neighbors(self, neighbors):
        return random.choice(neighbors)

    def show(self, title):
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        X, Y = np.meshgrid(self.X, self.Y)
        ax.plot_surface(X, Y, self.Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(title)
        plt.show()

    def draw_path(self, path, title):
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        X, Y = np.meshgrid(self.X, self.Y)
        ax.plot_surface(X, Y, self.Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        path_array = np.array(path)
        ax.plot(path_array[:, 0], path_array[:, 1], path_array[:, 2], 'r-', zorder=3, linewidth=0.5)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(title)
        plt.show()

