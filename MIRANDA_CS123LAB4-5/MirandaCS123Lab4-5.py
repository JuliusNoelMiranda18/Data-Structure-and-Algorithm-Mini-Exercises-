# ============================================================
# AVL TREE LAB  - PRODUCT INVENTORY MANAGEMENT SYSTEM
# ============================================================
# Use your knowledge of AVL trees to build a fast product catalog
# supporting insertion, deletion, and price-based lookups.
# ============================================================

from typing import Optional, Tuple

# ------------------- AVL Core -------------------

class AVLNode:
    def __init__(self, key: int, name: str, price: float):
        self.key = key                # Product ID (unique)
        self.val = (name, price)      # Product info: (name, price)
        self.left = None
        self.right = None
        self.height = 1


def _height(node: Optional[AVLNode]) -> int:
    return node.height if node else 0


def _update_height(node: AVLNode):
    node.height = 1 + max(_height(node.left), _height(node.right))


def _balance_factor(node: AVLNode) -> int:
    return _height(node.left) - _height(node.right)


def _rotate_right(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    _update_height(y)
    _update_height(x)
    return x


def _rotate_left(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    _update_height(x)
    _update_height(y)
    return y


# ------------------- AVL Operations -------------------

def avl_insert(node: Optional[AVLNode], key: int, name: str, price: float) -> AVLNode:
    """Insert or update a product."""
    if node is None:
        return AVLNode(key, name, price)

    if key < node.key:
        node.left = avl_insert(node.left, key, name, price)
    elif key > node.key:
        node.right = avl_insert(node.right, key, name, price)
    else:
        # TODO 1: Update product info if same product_id already exists
        # Hint: node.val = (name, price)
        node.val = (name, price)
        pass

    _update_height(node)
    bf = _balance_factor(node)

    # Left-Left
    if bf > 1 and key < node.left.key:
        return _rotate_right(node)
    # Right-Right
    if bf < -1 and key > node.right.key:
        return _rotate_left(node)
    # Left-Right
    if bf > 1 and key > node.left.key:
        node.left = _rotate_left(node.left)
        return _rotate_right(node)
    # Right-Left
    if bf < -1 and key < node.right.key:
        node.right = _rotate_right(node.right)
        return _rotate_left(node)

    return node


def avl_delete(node: Optional[AVLNode], key: int) -> Optional[AVLNode]:
    """Delete product by product_id."""
    if node is None:
        return None

    if key < node.key:
        node.left = avl_delete(node.left, key)
    elif key > node.key:
        node.right = avl_delete(node.right, key)
    else:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            # Find inorder successor
            succ_parent = node
            succ = node.right
            while succ.left:
                succ_parent = succ
                succ = succ.left
            node.key = succ.key
            node.val = succ.val
            if succ_parent is node:
                node.right = succ.right
            else:
                succ_parent.left = succ.right

    if node is None:
        return None

    _update_height(node)
    bf = _balance_factor(node)

    if bf > 1 and _balance_factor(node.left) >= 0:
        return _rotate_right(node)
    if bf > 1 and _balance_factor(node.left) < 0:
        node.left = _rotate_left(node.left)
        return _rotate_right(node)
    if bf < -1 and _balance_factor(node.right) <= 0:
        return _rotate_left(node)
    if bf < -1 and _balance_factor(node.right) > 0:
        node.right = _rotate_right(node.right)
        return _rotate_left(node)

    return node


# ------------------- Inventory Wrapper -------------------

class ProductInventory:
    def __init__(self):
        self.root: Optional[AVLNode] = None

    def add_product(self, pid: int, name: str, price: float):
        # TODO 2: Insert into AVL tree
        # Hint: self.root = avl_insert(self.root, pid, name, price)
        self.root = avl_insert(self.root, pid, name, price)
        pass

    def remove_product(self, pid: int):
        # TODO 3: Delete from AVL tree
        self.root = avl_delete(self.root, pid)
        pass

    def list_products(self):
        """Return sorted list of (product_id, name, price)."""
        # TODO 4: Implement inorder traversal
        def _inorder(n):
            if n is None: return []
            return _inorder(n.left) + [(n.key, *n.val)] + _inorder(n.right)
        return _inorder(self.root)

    def find_next_expensive(self, price: float):
        """Find product with the smallest price > given value."""
        # TODO 5: Traverse keeping a candidate (similar to successor search)
        cur = self.root
        candidate = None
        while cur:
            if cur.val[1] > price:
                candidate = cur
                cur = cur.left
            else:
                cur = cur.right
        return (candidate.key, *candidate.val) if candidate else None

    def height(self):
        return _height(self.root)


# ------------------- DEMO RUN -------------------
if __name__ == "__main__":
    inv = ProductInventory()

    # Insert sample products
    items = [
        (101, "Mouse", 15.5),
        (205, "Keyboard", 25.0),
        (150, "Webcam", 35.0),
        (250, "Monitor", 90.0),
        (120, "USB Cable", 5.5),
        (300, "Headset", 55.0),
    ]
    for pid, name, price in items:
        inv.add_product(pid, name, price)

    key_root = inv.root.key if inv.root else None
    print("Initial catalog:")
    print(inv.list_products())
    print("Root =", key_root, "| Height =", inv.height())
    print("--------------------------------------------------")

    # Test updates
    inv.add_product(150, "HD Webcam", 40.0)
    inv.remove_product(205)
    print("After updates:")
    print(inv.list_products())
    print("Root =", inv.root.key, "| Height =", inv.height())

    # Find next expensive
    print("Next product after $20.0:", inv.find_next_expensive(20.0))
    print("Next product after $90.0:", inv.find_next_expensive(90.0))

    print("\n✅ Done! Your AVL-based catalog should remain balanced.")


    bonus = ProductInventory()

    items_bonus = [
        (101, "Mouse", 15.5),
        (102, "Wireless Mouse", 25.0),
        (103, "Gaming Mouse", 45.0),
        (104, "Ergonomic Mouse", 35.0),
        (105, "Trackball Mouse", 40.0),
        (201, "Keyboard", 30.0),
        (202, "Mechanical Keyboard", 85.0),
        (203, "Wireless Keyboard", 50.0),
        (204, "Gaming Keyboard", 120.0),
        (205, "Compact Keyboard", 45.0),
        (301, "Monitor", 180.0),
        (302, "4K Monitor", 350.0),
        (303, "Ultrawide Monitor", 450.0),
        (304, "Gaming Monitor", 280.0),
        (305, "Portable Monitor", 150.0),
        (401, "Webcam", 35.0),
        (402, "HD Webcam", 55.0),
        (403, "4K Webcam", 95.0),
        (404, "Streaming Webcam", 120.0),
        (405, "Conference Webcam", 200.0),
        (501, "Headset", 40.0),
        (502, "Gaming Headset", 80.0),
        (503, "Wireless Headset", 90.0),
        (504, "Noise-Canceling Headset", 150.0),
        (505, "USB Headset", 35.0),
        (601, "USB Cable", 5.5),
        (602, "USB-C Cable", 8.0),
        (603, "HDMI Cable", 12.0),
        (604, "DisplayPort Cable", 15.0),
        (605, "Ethernet Cable", 10.0),
        (701, "External Hard Drive 1TB", 60.0),
        (702, "External Hard Drive 2TB", 85.0),
        (703, "SSD 500GB", 70.0),
        (704, "SSD 1TB", 120.0),
        (705, "USB Flash Drive 32GB", 12.0),
        (801, "Laptop Stand", 25.0),
        (802, "Monitor Stand", 35.0),
        (803, "Adjustable Desk", 250.0),
        (804, "Laptop Cooling Pad", 30.0),
        (805, "Cable Management Box", 15.0),
        (901, "Router", 65.0),
        (902, "Gaming Router", 180.0),
        (903, "Mesh WiFi System", 220.0),
        (904, "Range Extender", 35.0),
        (905, "Modem", 55.0),
        (1001, "Printer", 120.0),
        (1002, "Laser Printer", 280.0),
        (1003, "3D Printer", 450.0),
        (1004, "Photo Printer", 95.0),
        (1005, "Label Printer", 85.0),
        (1101, "Speaker", 45.0),
        (1102, "Soundbar", 120.0),
        (1103, "Studio Monitors", 280.0),
        (1104, "Bluetooth Speaker", 55.0),
        (1105, "Desktop Speakers", 35.0),
        (1201, "Microphone", 40.0),
        (1202, "USB Microphone", 65.0),
        (1203, "Studio Microphone", 150.0),
        (1204, "Lavalier Microphone", 25.0),
        (1205, "Shotgun Microphone", 180.0),
        (1301, "Graphics Tablet", 85.0),
        (1302, "Drawing Tablet", 250.0),
        (1303, "Pen Display", 450.0),
        (1304, "Stylus Pen", 35.0),
        (1305, "Digital Pen", 55.0),
        (1401, "Power Strip", 18.0),
        (1402, "Surge Protector", 25.0),
        (1403, "UPS Battery Backup", 120.0),
        (1404, "USB Power Adapter", 15.0),
        (1405, "Wireless Charger", 28.0),
        (1501, "Desk Lamp", 35.0),
        (1502, "LED Strip Lights", 22.0),
        (1503, "Ring Light", 45.0),
        (1504, "Monitor Light Bar", 55.0),
        (1505, "Smart Bulb", 18.0),
        (1601, "Docking Station", 120.0),
        (1602, "USB Hub", 25.0),
        (1603, "Card Reader", 15.0),
        (1604, "KVM Switch", 55.0),
        (1605, "USB Switch", 20.0),
        (1701, "Mouse Pad", 12.0),
        (1702, "Extended Mouse Pad", 25.0),
        (1703, "RGB Mouse Pad", 35.0),
        (1704, "Wrist Rest", 18.0),
        (1705, "Desk Mat", 30.0),
        (1801, "Monitor Arm", 85.0),
        (1802, "Dual Monitor Arm", 150.0),
        (1803, "TV Wall Mount", 45.0),
        (1804, "Laptop Arm", 95.0),
        (1805, "Tablet Stand", 28.0),
        (1901, "Cleaning Kit", 15.0),
        (1902, "Screen Cleaner", 8.0),
        (1903, "Compressed Air", 10.0),
        (1904, "Microfiber Cloth", 5.0),
        (1905, "Keyboard Brush", 7.0),
        (2001, "Privacy Screen", 35.0),
        (2002, "Screen Protector", 12.0),
        (2003, "Blue Light Filter", 25.0),
    ]

    for pid, name, price in items_bonus:
        bonus.add_product(pid, name, price)

    key_root = bonus.root.key if bonus.root else None
    print("Initial catalog:")
    print(bonus.list_products())
    print("Root =", key_root, "| Height =", bonus.height())
    print("--------------------------------------------------")

    # Apply price updates for promotional items
    print("\n📦 OPERATION 1: Holiday Sale Price Updates")
    bonus.add_product(102, "Wireless Mouse", 19.99)
    bonus.add_product(203, "Wireless Keyboard", 39.99)
    bonus.add_product(501, "Headset", 29.99)
    print("Applied discounts to 3 items")
    print("Root =", bonus.root.key, "| Height =", bonus.height())

    # Remove discontinued products
    print("\n🗑️ OPERATION 2: Removing Discontinued Items")
    discontinued = [605, 1904, 1905, 704, 305]
    for pid in discontinued:
        bonus.remove_product(pid)
    print(f"Removed {len(discontinued)} discontinued products")
    print("Root =", bonus.root.key, "| Height =", bonus.height())
    print("--------------------------------------------------")

    print("\nFinal catalog size:", len(bonus.list_products()))
    print("Next product after $50.0:", bonus.find_next_expensive(50.0))
    print("Next product after $200.0:", bonus.find_next_expensive(200.0))

    print("\n✅ Done! Your AVL-based catalog should remain balanced.")


# 1. To maintain efficiency, ensure all operations (insert, delete, search) run in O(log n) time.
# 2. Having balance factor outside (-1, 0, 1) indicates the tree is unbalanced and requires rotations. 
# 3. Tree with bigger height may slow down operations; AVL trees keep height minimal.
# 4. Inserting products with increasing IDs in a normal BST would result in a right-skewed tree, degrading performance to O(n).
# 5. Flight reservation systems - The balanced nature ensures that even during peak booking times with thousands of seats across multiple flights, operations remain fast.