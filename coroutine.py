from inspect import getgeneratorstate


def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received', x)
    yield 10

coroutine = simple_coroutine()
# print(coroutine)

# .send()でも次のyieldまで処理を進める
next(coroutine)
test = coroutine.send(42)

print(test)
# 10


def simple_coroutine2(a):
    print('-> coroutine started: a=', a)
    b = yield a
    print('-> coroutine received: b=', b)
    c = yield a + b
    print('-> coroutine received: c=', c)

coroutine = simple_coroutine2(14)

status = getgeneratorstate(coroutine)
print(status)
# GEN_CREATED: 実行開始を待機

# コルーチンを次の状態まで進める
ret = next(coroutine)
print(ret)
# -> coroutine started: a= 14
# 14

status = getgeneratorstate(coroutine)
print(status)
# GEN_SUSPENDED: yield 式で現在一時停止

ret = coroutine.send(28)
print(ret)
# -> coroutine received: b= 28
# 42

status = getgeneratorstate(coroutine)
print(status)
# GEN_SUSPENDED: yield 式で現在一時停止

# coroutine.send(99)
# -> coroutine received: c= 99
# Traceback (most recent call last):
#  File "coroutine.py", line 53, in <module>
#    coroutine.send(99)
# StopIteration

# status = getgeneratorstate(coroutine)
# print(status)
# GEN_CLOSED: 実行完了

