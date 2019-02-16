import pyximport
pyximport.install()

from integrate import integrate
from math import sin, pi
from fib import fib


def sin2(x):
    return sin(x) ** 2


def main():
    print(fib(100))

    a, b = 0.0, 2.0 * pi
    return integrate(a, b, sin2, N=400000)

if __name__ == "__main__":
    # main()
    import cProfile
    cProfile.run('main()', sort='time')
