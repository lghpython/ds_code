class Node(object):
    def __init__(self, elem=None, left_sub=None, right_sub=None):
        self.elem = elem
        self.left_sub = left_sub
        self.right_sub = right_sub


class Tree(object):
    def __init__(self):
        self.root = None

    def __add__(self, elem):
        node = Node(elem)

        if self.root is None:
            self.root = node
            return
        else:
            # 若根为空则遍历子树，将验证过的弹出，找到空的分支
            queue = []
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                if cur.left_sub is None:
                    cur.left_sub = node
                    return
                elif cur.right_sub is None:
                    cur.right_sub = node
                    return
                else:
                    # 如果左树和右树都不为空继续迭代子树
                    queue.append(cur.left_sub)
                    queue.append(cur.right_sub)
