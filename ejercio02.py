class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        return node.height if node else 0

    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        # Realizar rotación
        y.left = z
        z.right = T2

        # Actualizar alturas
        self.update_height(z)
        self.update_height(y)

        return y

    def rotate_right(self, z):
        y = z.left
        T3 = y.right

        # Realizar rotación
        y.right = z
        z.left = T3

        # Actualizar alturas
        self.update_height(z)
        self.update_height(y)

        return y

# 🧪 Pruebas
def test_rotations():
    tree = AVLTree()

    # Test 1: Rotación Izquierda
    z = AVLNode(10)
    y = AVLNode(20)
    x = AVLNode(30)
    z.right = y
    y.right = x
    tree.update_height(x)
    tree.update_height(y)
    tree.update_height(z)
    new_root = tree.rotate_left(z)
    print("🧪 Test 1 (Rotate Left):", new_root.key == 20)

    # Test 2: Rotación Derecha
    z = AVLNode(30)
    y = AVLNode(20)
    x = AVLNode(10)
    z.left = y
    y.left = x
    tree.update_height(x)
    tree.update_height(y)
    tree.update_height(z)
    new_root = tree.rotate_right(z)
    print("🧪 Test 2 (Rotate Right):", new_root.key == 20)

    # Test 3: Altura correcta
    expected_height = 1 + max(tree.get_height(new_root.left), tree.get_height(new_root.right))
    print("🧪 Test 3 (Altura correcta):", new_root.height == expected_height)

    # Test 4: Hijo izquierdo correcto
    print("🧪 Test 4 (Hijo izquierdo correcto):", new_root.left.key == 10)

    # Test 5: Hijo derecho correcto
    print("🧪 Test 5 (Hijo derecho correcto):", new_root.right.key == 30)

# 🚀 Ejecutar
test_rotations()
