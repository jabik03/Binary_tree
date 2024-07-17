from abc import ABC, abstractmethod

class Tree(ABC):
    @abstractmethod
    def insert(self, value):
        pass

    @abstractmethod
    def inorder_traversal(self):
        pass

    @abstractmethod
    def preorder_traversal(self):
        pass

    @abstractmethod
    def postorder_traversal(self):
        pass


class TreeNode():
    def __init__(self, value: int) -> None:
        self.value: int = value         # Значение узла
        self.left: TreeNode = None      # Левое потомок
        self.right: TreeNode = None     # Правое потомок


class BinaryTree(Tree):
    def __init__(self) -> None:
        self.root: TreeNode = None      # Корень дерева

    def insert(self, value: int) -> None:
        """Вставка нового значения в дерево"""
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node: TreeNode, value: int) -> None:
        """Рекурсивная вставка нового значения в дерево"""
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)  # Вставка в левое поддерево
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)  # Вставка в правое поддерево
            else:
                self._insert_recursive(node.right, value)

    def inorder_traversal(self) -> list:
        """Симметричный обход дерева"""
        return self._inorder_traversal_recursive(self.root, [])
    
    def _inorder_traversal_recursive(self, node: TreeNode, traversal: list) -> list:
        """Рекурсивный симметричный обход дерева"""
        if node is not None:
            self._inorder_traversal_recursive(node.left, traversal)  # Обход левого поддерева
            traversal.append(node.value)  # Посещение узла
            self._inorder_traversal_recursive(node.right, traversal)  # Обход правого поддерева
        return traversal
    
    def preorder_traversal(self) -> list:
        """Предварительный обход дерева"""
        return self._preorder_traversal_recursive(self.root, [])

    def _preorder_traversal_recursive(self, node: TreeNode, traversal: list):
        """Рекурсивный предварительный обход дерева"""
        if node is not None:
            traversal.append(node.value)  # Посещение узла
            self._preorder_traversal_recursive(node.left, traversal)  # Обход левого поддерева
            self._preorder_traversal_recursive(node.right, traversal)  # Обход правого поддерева
        return traversal

    def postorder_traversal(self):
        """Обратный обход дерева"""
        return self._postorder_traversal_recursive(self.root, [])

    def _postorder_traversal_recursive(self, node: TreeNode, traversal: list) -> list:
        """Рекурсивный обратный обход дерева"""
        if node is not None:
            self._postorder_traversal_recursive(node.left, traversal)  # Обход левого поддерева
            self._postorder_traversal_recursive(node.right, traversal)  # Обход правого поддерева
            traversal.append(node.value)  # Посещение узла
        return traversal



if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(4)
    tree.insert(2)
    tree.insert(6)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)
    tree.insert(7)
    
    print(tree.inorder_traversal())
    print(tree.preorder_traversal())
    print(tree.postorder_traversal())
