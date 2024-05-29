import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "#000000"  # Початковий колір (чорний)
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, step_colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 7))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def generate_colors(n):
    colors = list(mcolors.CSS4_COLORS.values())
    step_colors = []
    for i in range(n):
        step_colors.append(colors[int(i * len(colors) / n)])
    return step_colors

def depth_first_search(node, step_colors, step=0):
    if node is not None:
        node.color = step_colors[step]
        step += 1
        step = depth_first_search(node.left, step_colors, step)
        step = depth_first_search(node.right, step_colors, step)
    return step

def breadth_first_search(root, step_colors):
    queue = [root]
    step = 0
    while queue:
        current = queue.pop(0)
        if current:
            current.color = step_colors[step]
            step += 1
            queue.append(current.left)
            queue.append(current.right)

def main():
    # Створення дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # Генерація кольорів
    total_nodes = 6  # Загальна кількість вузлів у дереві
    step_colors = generate_colors(total_nodes)

    # Обхід у глибину та візуалізація
    depth_first_search(root, step_colors)
    print("Візуалізація обходу в глибину:")
    draw_tree(root, step_colors)

    # Скидання кольорів вузлів
    for node in [root, root.left, root.left.left, root.left.right, root.right, root.right.left]:
        node.color = "#000000"

    # Обхід у ширину та візуалізація
    breadth_first_search(root, step_colors)
    print("Візуалізація обходу в ширину:")
    draw_tree(root, step_colors)

if __name__ == "__main__":
    main()
