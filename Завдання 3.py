class Triangule:
    def __init__(self,Ax,Ay,Bx,By,Cx,Cy):
        self.Ax = Ax
        self.Ay = Ay
        self.Bx = Bx
        self.By = By
        self.Cx = Cx
        self.Cy = Cy

    @property
    def AB(self):
        return ((self.Ax - self.Bx) ** 2 + (self.Ay - self.By) ** 2) ** 0.5

    @property
    def BC(self):
        return ((self.Bx - self.Cx) ** 2 + (self.By - self.Cy) ** 2) ** 0.5

    @property
    def AC(self):
        return ((self.Ax - self.Cx) ** 2 + (self.Ay - self.Cy) ** 2) ** 0.5

    def P(self):
        return self.AB + self.BC + self.AC

    def s(self):
        p = (self.AB + self.BC + self.AC) / 2
        return (p*(p-self.AB)*(p-self.AC)*(p-self.BC)) ** 0.5

    def __getitem__(self,key):
        if key == 1:
            return self.AB
        if key == 2:
            return self.BC
        if key == 3:
            return self.AC

t1 = Triangule(0,3,0,0,4,0)
print(t1.P())