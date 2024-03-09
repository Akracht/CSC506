class Node:
    def __init__(self, data): #Initialize Node Object, data = numerical value of node
        self.data = data
        self.left = None
        self.right = None
    
    def __lt__(self, other): #Compare node data to another node, returns true if source node less than other node
        return self.data < other.data

    def __eq__(self, other): #Compares equality of nodes, true if node data = to another nodes data (identify duplicates)
        return self.data == other.data


class Tree:
    def __init__(self, arr): #Initializes tree by processing an input array and employing build_tree functiojn
        self.root = self.build_tree(sorted(set(arr))) #Tree root node

    def build_tree(self, arr): #Builds tree using sorted array
        if not arr:
            return None
        mid = len(arr) // 2
        root = Node(arr[mid])
        root.left = self.build_tree(arr[:mid])
        root.right = self.build_tree(arr[mid+1:])
        return root
 
    def insert(self, root, data): #Inserts new node at correct position to maintain BST properties
        if root is None:
            return Node(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root

    def delete(self, root, data): #Deletes specified node and adjusts BST tree to maintain properties
        if root is None:
            return root
        if data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp_val = self.min_value_node(root.right)
            root.data = temp_val.data
            root.right = self.delete(root.right, temp_val.data)
        return root

    def min_value_node(self, node): #Finds minimum data value for nodes in given subtree and node. 
        current = node
        while current.left is not None:
            current = current.left
        return current


def PrintTree(root): #Prints a graphical representation of the tree
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1

    nlevels = height(root)
    width = pow(2, nlevels + 1)

    q = [(root, 0, width, 'c')]
    levels = []

    while q:
        node, level, x, align = q.pop(0)
        if node:
            if len(levels) <= level:
                levels.append([])

            levels[level].append([node, level, x, align])
            seg = width // (pow(2, level + 1))
            q.append((node.left, level + 1, x - seg, 'l'))
            q.append((node.right, level + 1, x + seg, 'r'))

    for i, l in enumerate(levels):
        pre = 0
        preline = 0
        linestr = ''
        pstr = ''
        seg = width // (pow(2, i + 1))
        for n in l:
            valstr = str(n[0].data)  # Changed from val to data to match Node class
            if n[3] == 'r':
                linestr += ' ' * (n[2] - preline - 1 - seg - seg // 2) + '¯' * (seg + seg // 2) + '\\'
                preline = n[2]
            if n[3] == 'l':
                linestr += ' ' * (n[2] - preline - 1) + '/' + '¯' * (seg + seg // 2)
                preline = n[2] + seg + seg // 2
            pstr += ' ' * (n[2] - pre - len(valstr)) + valstr  # Correct the position according to the number size
            pre = n[2]
        print(linestr)
        print(pstr)

# Accept Input Array & Generate Tree
arr = [1, 7, 4, 23, 8, 9, 4, 3, 5, 7, 9, 67, 6345, 324]
print("Input Array Used to Generate Tree:", arr)
tree = Tree(arr)

#Output the Root Node
print("Level 1 root node data:", tree.root.data)

# Insert new value
tree.insert(tree.root, 6)

# Delete a value
tree.delete(tree.root, 9)

# Print the tree graphically
PrintTree(tree.root)
