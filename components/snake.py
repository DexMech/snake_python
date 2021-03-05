

class Snake():
    def __init__(self,x, y):
        self.body = [[x,y]]
        self.y = y
        self.x = x
        self.length = 1
    def move(self, direction):
        if len(self.body) >= self.length:
            del self.body[0]

        if(direction == 'DOWN'):
            self.y = self.y + 10
        elif(direction == 'UP'):
            self.y = self.y - 10
        elif(direction == 'LEFT'):
            self.x = self.x - 10
        elif(direction == 'RIGHT'):
            self.x = self.x + 10
        self.body.append([self.x,self.y])

    def eat(self):
        self.length = self.length + 1
