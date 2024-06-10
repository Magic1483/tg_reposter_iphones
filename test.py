

def t(old_price) -> str:
    new_price = old_price
    if new_price< 70000:
        new_price = str(new_price+4000)#0--70k +4k
    elif new_price < 90000:
        new_price = str(new_price+5000)#70--90 +5k
    elif new_price < 110000:
        new_price = str(new_price+6000)#90--110-- +6k
    elif new_price < 130000:
        new_price = str(new_price+7000)#110--130 +7k
    else:
        new_price = str(new_price+10000)#130--> +10k
    return new_price



for i in range(40000,150000,5000):
    print(t(i))