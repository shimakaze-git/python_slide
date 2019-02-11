from inspect import iscoroutinefunction, iscoroutine, isawaitable
import types
import asyncio

data = {
    'girls;kg':
        [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'girls;m':
        [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'boys;kg':
        [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys;m':
        [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}


# averager に __await__() を定義する。
# __await__()でawaitableプロトコルを実装している限り, 
# 生成されたオブジェクトはawaitableとなる。

class averager:
    def __await__(self):
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


# ネイティブコルーチン関数は async def 文で定義
# コルーチン関数内でawait式を用いる。(awaitは、yeild fromの代わりになる)
# 結果が利用可能になるまでコルーチンの実行を停止することが可能
async def grouper(results, key):
    while True:
        results[key] = await averager()


# 従来のジェネレータベースのコルーチンに @asyncio.coroutine デコレータを付けることで, 
# awaitable となり async def 内で使用することが可能
# @asyncio.coroutine
@asyncio.coroutine
def averager():
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


if __name__ == "__main__":
    ave = averager()

    print(isawaitable(ave))

    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        group.send(None)
        for value in values:
            group.send(value)
        group.send(None)

    print(results)
