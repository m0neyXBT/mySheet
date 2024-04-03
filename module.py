

# The structure will be DATE,coin name,leverage,margin,DIRECTION(long or short),entry,exit
class Data:
    def __init__(self,read) -> None:
        v:list[str] = read.strip().split(';')
        self.date = v[0]
        self.pair = v[1]
        self.lev:float = float(v[2])
        self.margin:float = float(v[3])
        self.direction = v[4]
        self.entry:float = float(v[5])
        self.exit:float = float(v[6])
        self.size:float = self.margin/self.entry    #simple size calc
        self.profit:float = (self.exit-self.entry)*self.size*self.lev #Profit = (exit-entry)*size