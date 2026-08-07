class Node:
    """Represents a single node in the AVL tree."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # New nodes are initially added at leaf level (height 1)

class AVLTree:
    """Represents the self-balancing AVL Tree structure."""
    
    def get_height(self, node):
        """Helper to safely get the height of a node (handles None)."""
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        """Calculates the Balance Factor of a node."""
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        """Performs a single right rotation to fix Left-Heavy (LL) imbalances."""
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights (order matters: update child y first, then new parent x)
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        # Return the new root of this subtree
        return x

    def left_rotate(self, x):
        """Performs a single left rotation to fix Right-Heavy (RR) imbalances."""
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        # Return the new root of this subtree
        return y

    def insert(self, root, key):
        """Inserts a key and automatically rebalances the tree along the path."""
        # 1. Perform standard BST insertion
        if not root:
            return Node(key)
        
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # Duplicate keys are not allowed in this implementation

        # 2. Update the height of this ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # 3. Get the balance factor to check if it became unbalanced
        balance = self.get_balance(root)

        # 4. If unbalanced, handle one of the 4 cases:

        # Case 1: Left-Left (LL) -> Single Right Rotation
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Case 2: Right-Right (RR) -> Single Left Rotation
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Case 3: Left-Right (LR) -> Left Rotation then Right Rotation
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Case 4: Right-Left (RL) -> Right Rotation then Left Rotation
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def preorder(self, root):
        """Helper to print tree structure (Root, Left, Right)."""
        if root:
            print(f"{root.key} ", end="")
            self.preorder(root.left)
            self.preorder(root.right)
