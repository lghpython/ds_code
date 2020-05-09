class SingleNode(object):
    def __init__(self, elem=None):
        self.elem = elem
        self.next = None


class SingleLinkedList(object):
    def __init__(self):
        self.__head = None

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        count = 0
        cur = self.__head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur is not None:
            print(cur.elem)
            cur = cur.next
        print("")

    def add(self, item):
        """链表头部添加元素"""
        node = SingleNode(item)
        if self.__head is not None:
            node.next = self.__head
        self.__head = node

    def append(self, item):
        """链表尾部添加元素"""
        node = SingleNode(item)
        cur = self.__head

        if self.is_empty():
            self.__head = node
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
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
        while cur is not None:
            # 当前节点是要删除的节点
            if cur.elem == item:
                # 第一个节点就是删除节点
                if not pre:
                    # 第一节点删除，头节点指向删除的下一个节点
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

        return

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            cur = cur.next

        return False


if __name__ == '__main__':
    s_list = SingleLinkedList()
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
