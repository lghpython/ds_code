import time


def costtime(func):
    start_time = time.time()
    func()
    end_time = time.time()
    print(func.__name__ + "times:%f" % (end_time - start_time))
    print("finished")


# 求出a,b,c 使得a+b+c=2 且 a^2 +b^2 =c^2
# 思路一：分别迭代a,b,c 从0--1000
def cal_abc01():
    for a in range(1000):
        for b in range(1000):
            for c in range(1000):
                if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                    print("a,b,c:%d, %d, %d" % (a, b, c))


# 思路二：分别迭代a,b 从0--1000 ,c=1001-a-b
def cal_abc02():
    for a in range(1000):
        for b in range(1000):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                print("a,b,c:%d, %d, %d" % (a, b, c))


if __name__ == '__main__':
    costtime(cal_abc01)
    costtime(cal_abc02)
