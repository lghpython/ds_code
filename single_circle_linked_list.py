class SingleNode(object):
    def __init__(self, elem=None, next=None):
        self.elem = elem
        self.next = next


class SingleCircleLinkedList(object):
    def __init__(self):
        self.__head = None

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        # 空链表返回0
        if self.is_empty():
            return 0
        count = 1
        cur = self.__head
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        print(cur.elem)
        while cur.next != self.__head:
            cur = cur.next
            print(cur.elem)
        print("")

    def add(self, item):
        """链表头部添加元素"""
        node = SingleNode(item)
        # 当链表没有元素时，直接添加元素next指向自己
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            # 链表存在元素，将node插入
            node.next = self.__head
            self.__head = node

            cur = self.__head
            # 遍历最后元素指向第一元素
            while cur.next != self.head:
                cur = cur.next
            # cur.next = node
            cur.next = self.__head

    def append(self, item):
        """链表尾部添加元素"""
        node = SingleNode(item)
        cur = self.__head
        # 链表为空，直接插入node
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            # 链表不为空遍历元素到最后
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def insert(self, pos, item):
        """ 指定位置添加元素 """
        if pos <= 0:
            self.add(item)
        # 最后一个元素直接调用append方法
        elif pos > self.length() - 1:
            self.append(item)
        else:
            # 中间插入，与单链表没有区别
            node = SingleNode(item)
            pre = self.__head
            count = 0
            while count < pos - 1:
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        pre = None
        cur = self.__head
        if self.is_empty():
            return
        # 第一个就是要移除的元素，分元素是一个还是多个
        if cur.elem == item:
            # 不止一个元素
            if cur.next != self.__head:
                # 先找到尾节点，将next指向第二个节点
                while cur.next != self.__head:
                    cur = cur.next
                # 移除第一元素，尾节点和头节点指向第二节点
                cur.next = self.__head.next
                self.__head = self.__head.next
            else:
                # 只有一个节点
                self.__head = None

        else:
            pre = self.__head
            while cur.next !=self.__head:

                # 要删除的节点
                if cur.elem == item:
                    pre.next = cur.next
                    return
                else:
                    pre = cur
                    cur = cur.next
            # 删除最后节点
            if cur.elem == item:
                pre.next = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        # 如果为空链表，则返回False
        if self.is_empty():
            return False
        # 非空链表迭代查找
        while cur.next != self.__head:
            # 找到返回
            if cur.elem == item:
                return True
            cur = cur.next
        # 最后一个元素补充比较
        if cur.elem == item:
            return True
        return False


if __name__ == '__main__':
    s_list = SingleCircleLinkedList()
    print(s_list.is_empty())
    s_list.append(12)
    s_list.append(16)
    s_list.append(177)
    s_list.append(33)
    print(s_list.is_empty())
    print(s_list.length())
    s_list.travel()
    s_list.add(25)
    s_list.add(66)
    s_list.travel()
    s_list.insert(3, 86)
    s_list.insert(1, 90)
    s_list.travel()
    s_list.remove(90)
    s_list.remove(25)
    s_list.remove(12)
    s_list.travel()
