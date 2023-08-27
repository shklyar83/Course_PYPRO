# #1
def fibonacci():
    previous, current = 0, 1

    def inner():
        nonlocal previous, current
        previous, current = current, current + previous
        return previous

    return inner


f = fibonacci()
for _ in range(10):
    print(f())


# #2
def factorial():
    buf = [1, 1]

    def inner(n):
        if n < len(buf):
            return buf[n]
        res = buf[-1]
        for i in range(len(buf), n + 1):
            res *= i
            buf.append(res)

        return res
    return inner


f = factorial()
print(f(5))
print(f(4))
print(f(8))
