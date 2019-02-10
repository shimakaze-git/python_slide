from inspect import getgeneratorstate


class DemoException(Exception):
    """ An Exception type for the demonstration."""


def demo_exec_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('DemoException handled.')
        else:
            print('-> coroutine started: {!r}'.format(x))
    raise RuntimeError('This line should never run.')

coroutine = demo_exec_handling()
next(coroutine)
# -> coroutine started

print(coroutine.send(11))
# -> coroutine started: 11
# None

print(coroutine.send(22))
# -> coroutine started: 22
# None

coroutine.throw(DemoException)
# DemoException handled.

# coroutine.throw(ZeroDivisionError)

status = getgeneratorstate(coroutine)
print(status)
# GEN_SUSPENDED


coroutine.close()

status = getgeneratorstate(coroutine)
print(status)
# GEN_CLOSED
