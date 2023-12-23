class tree_node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child(self, child_node):
        self.children = [child for child in self.children if child != child_node]

    # 前序遍历
    def preorder_traversal(self):
        print(self.data, end=" ")
        for child in self.children:
            child.preorder_traversal()

    # 后序遍历
    def postorder_traversal(self):
        for child in self.children:
            child.postorder_traversal()
        print(self.data, end=" ")

    # 搜索
    def search(self, data):
        if self.data == data:
            return self
        for child in self.children:
            result = child.search(data)
            if result:
                return result
        return None

# 创建N叉树
root = tree_node("Root")
child1 = tree_node("Child1")
child2 = tree_node("Child2")
child3 = tree_node("Child3")
child4 = tree_node("Child4")

root.add_child(child1)
root.add_child(child2)
child1.add_child(child3)
child2.add_child(child4)

# 遍历树
print("Preorder Traversal:")
root.preorder_traversal()
print("\nPostorder Traversal:")
root.postorder_traversal()

# 搜索节点
search_result = root.search("Child3")
if search_result:
    print("\n\nNode found:", search_result.data)
else:
    print("\n\nNode not found")

# 移除节点
root.remove_child(child2)

# 再次遍历树
print("\nPreorder Traversal after removing Child2:")
root.preorder_traversal()


"""
Preorder Traversal:
Root Child1 Child3 Child2 Child4

Postorder Traversal:
Child3 Child1 Child4 Child2 Root

Node found: Child3

Preorder Traversal after removing Child2:
Root Child1 Child3
"""