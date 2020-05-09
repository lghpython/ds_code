import time


def insert_sort(a_list):
    n = len(a_list)
    if n <= 1:
        return a_list
    for i in range(1, n):
        for j in range(i, 0, -1):
            if a_list[j] < a_list[j - 1]:
                a_list[j - 1], a_list[j] = a_list[j], a_list[j - 1]
    return a_list


if __name__ == '__main__':
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    start_time = time.time()
    sorted_alist = insert_sort(a_list)
    end_time = time.time()
    print("times:", (end_time - start_time))
    print(sorted_alist)
