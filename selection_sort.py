import time


def selection_sort(a_list):
    n = len(a_list)
    if n <= 1:
        return a_list
    for i in range(n-1):
        min_pos = i
        for j in range(i+1, n):
            if a_list[j] < a_list[min_pos]:
                 min_pos = j
        if min_pos != i:
            a_list[min_pos], a_list[i] = a_list[i], a_list[min_pos]
    return a_list


if __name__ == '__main__':
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    start_time = time.time()
    sorted_alist = selection_sort(a_list)
    end_time = time.time()
    print("times:" , (end_time - start_time))
    print(sorted_alist)
