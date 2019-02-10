def averager_coroutine():
    total = 0.0
    count = 0
    average = None

    while True:
        term = yield average
        total += term
        count += 1
        average = total/count


def averager_coroutine2():
    total = 0.0
    count = 0
    average = None

    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    return (count, average)


def average():
    # avg = averager_coroutine()
    avg = averager_coroutine2()
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

try:
    avg.send(None)
except StopIteration as e:
    result = e.value

print(result)
