
def check_root(func):
    def wrapper(self, *args, **kwargs):
        if self.root:
            return func(*args, **kwargs)
        print('Операция невозможна, так как дерево пустое')
    return wrapper


class Tree:
    def __init__(self):
        self.root = None


class BinaryTree(Tree):
    @check_root
    def add(self, node):
        pass


class BinarySearchTree(BinaryTree):
    pass