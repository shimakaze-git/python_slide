# 呼び出されるとジェネレータオブジェクトを返すジェネレーター関数(PEP 255)という
# ジェネレータはイテレータとして動作

# オブジェクト x に対して反復処理するときは、
# 組み込み関数 iter(x) を呼びイテレータを取得する

# メソッド __iter__ を実装しイテレータを返すオブジェクトはイテラブルとなる。
# Python のコレクション(list,set,dict,tupple)はすべてイテラブルである。


def generator_123():
    yield 1
    yield 2
    yield 3

g = generator_123()

print(next(g))
# 1
print(next(g))
# 2
print(next(g))
# 3

# 組み込み関数next()を読んでいけば、関数内が次のyieldまで進む
# yieldが末尾まで到達すると、Iteratorプロトコルに従ってStopIterationを上げる。

g = generator_123()
for i in g:
    print(i)


print("-------------------------------")

# フィボナッチ数列,next()を進めていけばbにはb+aの計算がされる
# aにはbが入る

max_count = 10


def fibonacci():
    count = 0
    a, b = 0, 1

    # while True:
    while count < max_count:
        count += 1
        yield a
        a, b = b, b+a

for i in fibonacci():
    print(i)