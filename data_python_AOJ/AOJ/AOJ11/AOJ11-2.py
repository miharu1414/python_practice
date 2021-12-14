class saicoro:

    def __init__(self):
        self.nameplate = self
        self.pos = [0, 0, 0, 0, 0, 0]
        
    def position(self, top, s, e, w, n, bot):
        self.pos[0] = top
        self.pos[1] = s
        self.pos[2] = e
        self.pos[3] = w
        self.pos[4] = n
        self.pos[5] = bot
    
    def roll(self, str):
        if str == 'N':
            a = self.pos[0]
            self.pos[0] = self.pos[1]
            self.pos[1] = self.pos[5]
            self.pos[5] = self.pos[4]
            self.pos[4] = a

        elif str == 'S':
            a = self.pos[0]
            self.pos[0] = self.pos[4]
            self.pos[4] = self.pos[5]
            self.pos[5] = self.pos[1]
            self.pos[1] = a

        elif str == 'E':
            a = self.pos[0]
            self.pos[0] = self.pos[3]
            self.pos[3] = self.pos[5]
            self.pos[5] = self.pos[2]
            self.pos[2] = a
        elif str == 'no':
            return 0

        else:
            a = self.pos[0]
            self.pos[0] = self.pos[2]
            self.pos[2] = self.pos[5]
            self.pos[5] = self.pos[3]
            self.pos[3] = a

    def identify(self, b, c):
        if b == self.pos[0]:
            if c == self.pos[1]:
                print(self.pos[2])
            elif c == self.pos[2]:
                print(self.pos[4])
            elif c == self.pos[3]:
                print(self.pos[1])
            elif c == self.pos[4]:
                print(self.pos[3])
        
        elif b == self.pos[1]:
            if c == self.pos[0]:
                print(self.pos[3])
            elif c == self.pos[2]:
                print(self.pos[0])
            elif c == self.pos[3]:
                print(self.pos[5])
            elif c == self.pos[5]:
                print(self.pos[2])
                
        elif b == self.pos[2]:
            if c == self.pos[0]:
                print(self.pos[1])
            elif c == self.pos[1]:
                print(self.pos[5])
            elif c == self.pos[4]:
                print(self.pos[0])
            elif c == self.pos[5]:
                print(self.pos[4])
        
        elif b == self.pos[3]:
            if c == self.pos[0]:
                print(self.pos[4])
            elif c == self.pos[1]:
                print(self.pos[0])
            elif c == self.pos[4]:
                print(self.pos[5])
            elif c == self.pos[5]:
                print(self.pos[1])
        
        elif b == self.pos[4]:
            if c == self.pos[0]:
                print(self.pos[2])
            elif c == self.pos[5]:
                print(self.pos[3])
            elif c == self.pos[3]:
                print(self.pos[0])
            elif c == self.pos[2]:
                print(self.pos[5])

        elif b == self.pos[5]:
            if c == self.pos[1]:
                print(self.pos[3])
            elif c == self.pos[2]:
                print(self.pos[1])
            elif c == self.pos[3]:
                print(self.pos[4])
            elif c == self.pos[4]:
                print(self.pos[2])


top, s, e, w, n, bot = map(int, input().split())
qa = []
qb = []
num = int(input())
for _ in range(num):
    A, B = map(int, input().split())
    qa.append(A)
    qb.append(B)

s1 = saicoro()
s1.position(top, s, e, w, n, bot)
cnt = 0
for i, j in zip(qa, qb):
    s1.identify(i, j)

