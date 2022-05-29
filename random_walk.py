from random import choice


class RandomWalk:
    def __init__(self, num_points=10_000):
        self.num_points = num_points
        # all walks start at 0,0
        self.x_val = [0]
        self.y_val = [0]

    @staticmethod
    def get_step():
        return choice([1, -1]) * choice([0, 1, 2, 3, 4])

    def fill_walk(self):
        while len(self.x_val) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step and y_step == 0:
                continue

            x = self.x_val[-1] + x_step
            y = self.y_val[-1] + y_step

            self.x_val.append(x)
            self.y_val.append(y)
