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

        else:
            a = self.pos[0]
            self.pos[0] = self.pos[2]
            self.pos[2] = self.pos[5]
            self.pos[5] = self.pos[3]
            self.pos[3] = a


top, s, e, w, n, bot = map(int, input().split())
command = input()

s1 = saicoro()
s1.position(top, s, e, w, n, bot)

for i in command:
    s1.roll(i)

print(s1.pos[0])