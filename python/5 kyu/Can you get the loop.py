def loop_size(node):
    nodes = []
    while node not in nodes:
        nodes.append(node)
        node = node.next

    if node in nodes:
        nodes = nodes[nodes.index(node):]

    return len(nodes)