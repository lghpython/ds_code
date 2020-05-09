class Node(object):
    def __init__(self, elem=None):
        self.prev = None
        self.elem = elem
        self.next = None


class DoubleLinkedlist(object):
    def __init__(self):
        self.__head = None

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur is not None:
            print(cur.elem)
            cur = cur.next
        print("")

    def add(self, item):
        """链表头部添加"""
        node = Node(item)
        # 空链表添加到头部，节点保存_head
        if self.is_empty():
            self.__head = node
        else:
            self.__head.prev = node
            node.next = self.__head
            self.__head = node

    def append(self, item):
        """链表尾部添加"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            node.prev = cur
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            cur = self.__head
            node = Node(item)
            count = 0
            while count < (pos - 1):
                count += 1
                cur = cur.next
            # 新节点指向两边
            node.prev = cur
            node.next = cur.next
            # 两边指向新节点
            cur.next = node
            cur.next.prev = node

    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            return
        else:
            cur = self.__head
            # 第一个节点就是item
            if cur.elem == item:
                # 只有一个节点
                if cur.next is None:
                    self.__head = None
                else:
                    cur.next.prev = None
                    self.__head = cur.next
                return

            while cur.next is not None:
                if cur.elem == item:
                    cur.next.prev = cur.prev
                    cur.prev.next = cur.next
                    break
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            cur = cur.next
        return False


if __name__ == "__main__":
    ll = DoubleLinkedlist()
    ll.add(1)  # 1
    ll.add(2)  # 2 1
    ll.append(3) # 2 1 3
    ll.insert(2, 4) # 2 1 4 3
    ll.travel()
    ll.insert(4, 5) # 2 1 4 3 5
    ll.insert(0, 6) # 6 2 1 4 3 5
    print("length:", ll.length())
    ll.travel()
    print(ll.search(3))
    print(ll.search(4))
    ll.remove(1)
    print("length:", ll.length())
    ll.travel()
