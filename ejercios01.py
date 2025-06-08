class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Rotaciones
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def inorder(self, root):
        result = []
        self._inorder(root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

# Función de prueba
def test_avl_insert():
    tests = [
        ([10, 20, 30], [10, 20, 30], "Rotate Right (RR)"),
        ([30, 20, 10], [10, 20, 30], "Rotate Left (LL)"),
        ([30, 10, 20], [10, 20, 30], "Left-Right (LR)"),
        ([10, 30, 20], [10, 20, 30], "Right-Left (RL)"),
        ([15, 10, 20, 25, 30], [10, 15, 20, 25, 30], "Balanced tree")
    ]

    for i, (values, expected, name) in enumerate(tests, start=1):
        avl = AVLTree()
        root = None
        for val in values:
            root = avl.insert(root, val)
        result = avl.inorder(root)
        print(f"🧪 Test {i} ({name}):", result == expected)

# Ejecutar
test_avl_insert()
