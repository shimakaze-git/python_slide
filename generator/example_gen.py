def simeple_gen():
    yield "Hello"
    yield "World"

gen = simeple_gen()
print(next(gen))
print(next(gen))


def generate_nums():
    num = 0
    while True:
        yield num

        # num = num + 1
        num += 1

nums = generate_nums()

for x in nums:
    print(x)

    if x > 9:
        break
