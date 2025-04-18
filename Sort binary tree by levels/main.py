def tree_by_levels(node):
    stack = [node]
    out = []
    while stack != []:
        node = stack.pop()
        if node is None:
            continue
        out.append(node.value)
        stack = [node.right, node.left] + stack
    return out
