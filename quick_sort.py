import time


def quick_sort(a_list, start, end):
    n = num = len(a_list)
    # 代码为空或只有1个，直接返回列表
    if start >= end:
        return
    mid = a_list[start]
    low = start
    high = end

    while low < high:
        while low < high and a_list[high] >= mid:
            high -= 1
        a_list[low] = a_list[high]
        while low < high and a_list[low] < mid:
            low += 1
        a_list[high] = a_list[low]
        # print(a_list)
    # 当low和high重合时，跳出循环确定位置
    a_list[low] = mid
    # 小于基准数的列表递归排序
    quick_sort(a_list, start, low - 1)
    # 大于基准数的列表递归排序
    quick_sort(a_list, high+1, end)

    return a_list


if __name__ == '__main__':
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    start_time = time.time()
    sorted_alist = quick_sort(a_list, 0, len(a_list) - 1)
    end_time = time.time()
    print("times:", (end_time - start_time))
    print(sorted_alist)
