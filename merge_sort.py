import time


def merge_sort(a_list):
    # 代码为空或只有1个，直接返回列表
    if len(a_list) <= 1:
        return a_list
    # 二分分解,最小两个元素
    num = len(a_list) // 2
    # left递归 下面有left和right right同
    left = merge_sort(a_list[:num])
    right = merge_sort(a_list[num:])
    # 合并
    return merge(left, right)


def merge(left, right):
    """ 合并操作,将两个有序数组left[] 和right[]合并成一个大的有序数组 """

    # left与right 的下标指针
    l, r = 0, 0
    result = []
    # 循环中筛选小的那个首先放入result，游标往后走。
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    # 游标走到最后，往result填剩下最后那个
    result += left[l:]
    result += right[r:]
    return result


if __name__ == '__main__':
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    start_time = time.time()
    sorted_alist = merge_sort(a_list)
    end_time = time.time()
    print("times:", (end_time - start_time))
    print(sorted_alist)
