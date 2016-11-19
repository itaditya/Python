# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())


class castle:

    def __init__(self):
        self.grid = [list(raw_input().strip()) for i in xrange(N)]
        self.a, self.b, self.c, self.d = map(int, raw_input().split())
        self.x = self.a
        self.y = self.b

    def isPossible(self, x1, y1):
        if(x1 >= N or y1 >= N or x1 < 0 or y1 < 0 or self.grid[x1][y1] == 'X'):
            return False
        else:
            return True

    def moveTo()
c = castle()
print c.isPossible(0, 1)
