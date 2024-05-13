import numpy as np
import matplotlib.pyplot as plt
import cv2
import random


class Problem:
    def __init__(self, filename, parent=None, state_start=None):
        self.filename = filename
        self.load_state_space()
        self.parent = parent
        self.state_start = state_start
    
    def get_initial_state(self):
        x, y = self.state_start
        return (x, y, self.evaluation(), self)

    def load_state_space(self):
        img = cv2.imread(self.filename, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        img = cv2.GaussianBlur(img, (5, 5), 0)
        self.h, self.w = img.shape
        self.X = np.arange(self.w)
        self.Y = np.arange(self.h)
        self.Z = img

    def evaluation(self):
        x, y = self.state_start
        return self.Z[y, x]
    
    def schedule(self, T):
        return T * 0.9

    def find_path(self):
        p = self
        best_path = []
        while p is not None:
            if p.state_start == None:
                break
            x, y = p.state_start
            z = p.evaluation()
            best_path.insert(0, (x, y, z))
            p = p.parent
        return best_path

    def get_neighbors(self):
        x, y = self.state_start
        neighbors = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                if dx != 0 and dy != 0:
                    continue
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < len(self.X) and 0 <= new_y < len(self.Y):
                    neighbors.append(Problem(filename=self.filename, parent=self, state_start=(new_x, new_y)))
        return neighbors

    def random_state(self):
        x, y = random.choice(list(self.X)), random.choice(list(self.Y))
        return Problem(filename=self.filename, parent=self, state_start = (x, y))
    
    def random_neighbors(self, neighbors):
        return random.choice(neighbors)
    
    def random_k_state(self, k):
        state = []
        for _ in range(k):
            state.append(self.random_state())
        return state
    
    def condition(self, state, current):
        if state.parent != None:
            state_va = state.parent
        if current.state_start == state_va.state_start and current.evaluation() <= state_va.evaluation():
            return True
        return False

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
