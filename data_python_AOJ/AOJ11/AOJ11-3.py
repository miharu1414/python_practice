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
                return self.pos[2]
            elif c == self.pos[2]:
                return self.pos[4]
            elif c == self.pos[3]:
                return self.pos[1]
            elif c == self.pos[4]:
                return self.pos[3]
        
        elif b == self.pos[1]:
            if c == self.pos[0]:
                return self.pos[3]
            elif c == self.pos[2]:
                return self.pos[0]
            elif c == self.pos[3]:
                return self.pos[5]
            elif c == self.pos[5]:
                return self.pos[2]
                
        elif b == self.pos[2]:
            if c == self.pos[0]:
                return self.pos[1]
            elif c == self.pos[1]:
                return self.pos[5]
            elif c == self.pos[4]:
                return self.pos[0]
            elif c == self.pos[5]:
                return self.pos[4]
        
        elif b == self.pos[3]:
            if c == self.pos[0]:
                return self.pos[4]
            elif c == self.pos[1]:
                return self.pos[0]
            elif c == self.pos[4]:
                return self.pos[5]
            elif c == self.pos[5]:
                return self.pos[1]
        
        elif b == self.pos[4]:
            if c == self.pos[0]:
                return self.pos[2]
            elif c == self.pos[5]:
                return self.pos[3]
            elif c == self.pos[3]:
                return self.pos[0]
            elif c == self.pos[2]:
                return self.pos[5]

        elif b == self.pos[5]:
            if c == self.pos[1]:
                return self.pos[3]
            elif c == self.pos[2]:
                return self.pos[1]
            elif c == self.pos[3]:
                return self.pos[4]
            elif c == self.pos[4]:
                return self.pos[2]


top, s, e, w, n, bot = map(int, input().split())
s1 = saicoro()
s1.position(top ,s ,e ,w ,n ,bot)

a = list(map(int, input().split()))

topans = 0
for i in range(6):
    if (top == a[i]):
        topans = i
        break

if a[5 - topans] != bot:
    print('No')
    exit()

s2 = saicoro()
s2.position(a[0],a[1],a[2],a[3],a[4],a[5])

A = list((top, s, e, w, n, bot))


