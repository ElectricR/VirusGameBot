import argparse
import random
import time

class AggressiveVirus:
    
    def __init__(self, field, player):
        self.field = field
        self.in_init = True
        self.player = player
        for i in range(10):
            for j in range(10):
                if self.field[i][j] == self.player:
                    self.in_init = False
                    break
            if not self.in_init:
                break
        self.enemy = {'1': '2', '2': '1'}[player]
        self.calc_distances()
    
    def move(self):
        if self.in_init:
            self.in_init = False
            if self.player == '1':
                self.field[9][0] = '1'
            else:
                self.field[0][9] = '2'
            return
        candidates = set()
        for x in range(10):
            for y in range(10):
                if self.field[x][y] == self.player:
                    for i, j in self.get_neighbours(x, y):
                        if self.field[i][j] in ['0', self.enemy]:
                            candidates.add((i, j))
        if not candidates:
            return
        candidates = sorted(list(candidates), key=lambda x: self.distances[x[0]][x[1]])
        candidates = list(filter(lambda x: self.distances[x[0]][x[1]]==self.distances[candidates[0][0]][candidates[0][1]], candidates))
        
        target = random.choice(candidates)
        if self.field[target[0]][target[1]] == '0':
            self.field[target[0]][target[1]] = self.player
        else:
            self.field[target[0]][target[1]] = {'1': '3', '2': '4'}[self.enemy]
        self.distances[target[0]][target[1]] = 'i'



    def calc_distances(self):
        self.distances = [['i' if i not in (self.enemy, '0') else float('inf') for i in j] for j in self.field]
        search_range = []
        for i in range(10):
            for j in range(10):
                if self.field[i][j] == self.enemy:
                    self.distances[i][j] = 0
                    search_range.append((i, j))
        current_dist = 1
        while search_range:
            current_range = search_range
            search_range = []
            for i, j in current_range:
                for x, y in self.get_neighbours(i, j):
                    if self.distances[x][y] == float('inf'):
                        self.distances[x][y] = current_dist
                        search_range.append((x, y))
            current_dist += 1

    def get_neighbours(self, x, y):
        ret = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= x + i < 10 and 0 <= y + j < 10 and (i, j) != (0, 0):
                    ret.append((x + i, y + j))
        return ret
            

if __name__ == "__main__":
    random.seed(time.time())
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--name', action="store_true")
    args = argparser.parse_args()
    if args.name:
        print("AggressiveVirus")
    field = []
    for i in range(10):
        row = list(input().strip())
        field.append(row)
    player = input().strip()
    vir = AggressiveVirus(field, player)
    for _ in range(3):
        vir.move()
    for i in range(10):
        print(''.join(vir.field[i]))

