x_ = []
y_ = []

for i in range(3):
    x,y = map(int,input().split())
    x_.append(x)
    y_.append(y)

for j in range(3):
    if x_.count(x_[j]) == 1:
        x = x_[j]

    if y_.count(y_[j]) == 1:
        y = y_[j]
print(x,y)