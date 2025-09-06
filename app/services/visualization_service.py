def generate_flowchart(modules):
    nodes = "\n".join([f'{i}[{m["name"]}]' for i, m in enumerate(modules)])
    connections = "\n".join([f"{i} --> {i+1}" for i in range(len(modules) - 1)])
    return f"flowchart LR\n{nodes}\n{connections}"


def generate_sequence_diagram(modules):
    steps = "\n".join([f"User->>+{m['name']}: send input" for m in modules])
    return f"sequenceDiagram\n{steps}"
