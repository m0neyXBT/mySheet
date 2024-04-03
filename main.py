from module import *


#It contains the strucured data, you can work with that
datas:list[Data] = []


#change the first '' for your own file path
file = open('/media/pc/SSD_4801/python/asdasdas/mysheet/asd','r',encoding='utf-8')
for line in file:
    datas.append(Data(line))


#All of the trades
print(f'Date\t\tPair\tLevrage\tMargin\tDirection\tEntry\tExit\tSize\tPnL')
for i in datas:
    print(f'{i.date}\t{i.pair}\t{i.lev}\t{i.margin}\t {i.direction}\t\t{round(i.entry,2)}\t{round(i.exit,2)}\t{round(i.size,4)}\t{round(i.profit,2)}')


print()
print(f'Total trades: {len(datas)}')


# Total PnL calc
def PnL():
    Total_pnl:float = 0
    for i in datas:
        Total_pnl += i.profit
    return Total_pnl
pnl = PnL()
print(f'Total PnL: {round(pnl,2)}$')
print()


# Best Trade calc
maxii:float = 0
for i in range(1,len(datas)):
    if datas[i].profit > datas[maxii].profit:
        maxii = i
print(f'Personal best trade: {datas[maxii].date} {datas[maxii].pair} {round(datas[maxii].profit,2)}$')