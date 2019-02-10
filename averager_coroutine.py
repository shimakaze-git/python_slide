def averager_coroutine():
    total = 0.0
    count = 0
    average = None

    while True:
        term = yield average
        total += term
        count += 1
        average = total/count


def average():
    avg = averager_coroutine()
    # next()を入れてyieldの位置まで進めておく
    next(avg)
    return avg

avg = average()

print(avg.send(10))
# 10.0

print(avg.send(30))
# 20.0

print(avg.send(5))
# 15.0
