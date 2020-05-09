from timeit import Timer


def test1():
    l = []
    for i in range(1000):
        # l[i] = i
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l += [i]


def test3():
    l = []
    for i in range(1000):
        l.append(i)


def test4():
    l = []
    for i in range(1000):
        l.extend([1])


def test5():
    l = [i for i in range(1000)]


def test6():
    l = list(range(1000))


if __name__ == '__main__':
    t1 = Timer('test1()', 'from __main__ import test1')
    print("concat:", t1.timeit(number=1000), "seconds")
    t2 = Timer('test2()', 'from __main__ import test2')
    print("+=:", t2.timeit(number=1000), "seconds")
    t3 = Timer('test3()', 'from __main__ import test3')
    print("append:", t3.timeit(number=1000), "seconds")
    t4 = Timer('test4()', 'from __main__ import test4')
    print("extend:", t4.timeit(number=1000), "seconds")
    t5 = Timer('test5()', 'from __main__ import test5')
    print("iter:", t5.timeit(number=1000), "seconds")
    t6 = Timer('test6()', 'from __main__ import test6')
    print("list():", t6.timeit(number=1000), "seconds")
