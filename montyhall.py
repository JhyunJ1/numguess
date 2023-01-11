from random import shuffle, choice

doors = [0,0,1]

n = 100000

nochange = 0.0
change = 0.0

for _ in range(100000):
    shuffle(doors)
    c = choice(doors)
    print(doors)
    if c == 1:
        nochange += 1

nochange /= float(n)
change = 1.0 - float(nochange)


print(f"If, nothing change? {nochange}!!")
print(f"if, change? {change}!!")

