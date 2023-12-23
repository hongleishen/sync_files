// 创建新节点
tree_node *create_node(const char *data, tree_node *parent) {
    tree_node *node = (tree_node*)malloc(sizeof(tree_node));
    node->data = strdup(data);
    node->children = NULL;
    node->child_count = 0;
    node->parent = parent; // 设置父节点
    node->depth = parent ? parent->depth + 1 : 0; // 设置深度
    return node;
}

// 添加子节点
void add_child(tree_node *parent, tree_node *child) {
    parent->child_count++;
    parent->children = (tree_node**)realloc(parent->children, sizeof(tree_node*)  *parent->child_count);
    parent->children[parent->child_count - 1] = child;
    child->parent = parent; // 更新子节点的父节点
    child->depth = parent->depth + 1; // 更新子节点的深度
}


int main() {
    tree_node *root = create_node("Root", NULL); // 根节点没有父节点
    tree_node *child1 = create_node("Child1", root);
    tree_node *child2 = create_node("Child2", root);
    tree_node *child3 = create_node("Child3", child1);
    tree_node *child4 = create_node("Child4", child2);

    add_child(root, child1);
    add_child(root, child2);
    add_child(child1, child3);
    add_child(child2, child4);

    // ... 其他代码 ...

    return 0;
}
