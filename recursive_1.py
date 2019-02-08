sample = [
    "a",
    ["b", 1, [[["c", 2], 3], 4], "d"],
    ["e"]
]

def sum(n):
    if n <= 0:
        return n
    return n + sum(n-1)

def get_str(arg):
    result =[]
    if isinstance(arg, str):
        result.append(arg)

    if isinstance(arg, list):
        for item in arg:
            res = get_str(item)
            result += res
    return result

# def sum(n):
#     res = 0
#     for i in range(n+1):
#         res += i
#     return res

if __name__ == "__main__":
    print(get_str(sample))

    print(sum(10))