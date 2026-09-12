class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return new_node
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        return new_node

def solve():
    inp = input("Enter edges: ").strip()
    if not inp:
        print("No intersection")
        return

    nodes = {}  # Map: val -> Node object
    in_deg = {} # Map: val -> in-degree count

    def get_node(v):
        if v not in nodes:
            nodes[v] = Node(v)
            in_deg[v] = 0
        return nodes[v]

    # 1. Parse edges and construct Linked List references
    for edge in inp.split(','):
        if '>' in edge:
            u_val, v_val = map(int, edge.split('>'))
            u_node = get_node(u_val)
            v_node = get_node(v_val)
            u_node.next = v_node
            in_deg[v_val] = in_deg.get(v_val, 0) + 1

    # 2. Find Intersections (sorted without using standard python list)
    # Collect intersection node values in a sorted SingleLinkedList
    intersections = LinkedList()
    for val in sorted(in_deg.keys()):
        if in_deg[val] > 1:
            intersections.append(val)

    if not intersections.head:
        print("No intersection")
        return

    # Print intersection sizes
    curr_inter = intersections.head
    while curr_inter:
        node = nodes[curr_inter.val]
        # Calculate size (length until end or visited node)
        size = 0
        curr = node
        visited_nodes = set()
        while curr and curr not in visited_nodes:
            visited_nodes.add(curr)
            size += 1
            curr = curr.next
        print(f"Node({curr_inter.val}, size={size})")
        curr_inter = curr_inter.next

    # 3. Disconnect intersection nodes
    inter_set = set()
    curr_inter = intersections.head
    while curr_inter:
        inter_set.add(curr_inter.val)
        curr_inter = curr_inter.next

    for u_val, node in nodes.items():
        if u_val in inter_set:
            node.next = None
        elif node.next and node.next.val in inter_set:
            node.next = None

    # 4. Re-evaluate remaining nodes and collect valid head components
    rem_in_deg = {val: 0 for val in nodes if val not in inter_set}
    for val, node in nodes.items():
        if val not in inter_set and node.next and node.next.val not in inter_set:
            rem_in_deg[node.next.val] += 1

    # Create a list of chain heads (Sorted)
    heads_ll = LinkedList()
    for val in sorted(rem_in_deg.keys()):
        if rem_in_deg[val] == 0:
            heads_ll.append(val)

    # Filter out circular chains and build individual non-circular chains
    # Store heads of valid chains in a new LinkedList structure
    valid_heads = LinkedList()
    curr_h = heads_ll.head
    while curr_h:
        curr = nodes[curr_h.val]
        visited_nodes = set()
        is_circular = False
        while curr:
            if curr in visited_nodes:
                is_circular = True
                break
            visited_nodes.add(curr)
            curr = curr.next
        if not is_circular:
            valid_heads.append(curr_h.val)
        curr_h = curr_h.next

    # 5. Swap Merge directly on pointers without Python lists
    # We will traverse layer by layer (pointers moving in parallel)
    print("Delete intersection then swap merge:")
    
    # Store current traversal pointers for each chain using a dynamic dictionary
    pointers = {}
    curr_h = valid_heads.head
    while curr_h:
        pointers[curr_h.val] = nodes[curr_h.val]
        curr_h = curr_h.next

    first = True
    while True:
        any_active = False
        curr_h = valid_heads.head
        while curr_h:
            ptr = pointers[curr_h.val]
            if ptr:
                if not first:
                    print(" -> ", end="")
                print(ptr.val, end="")
                first = False
                pointers[curr_h.val] = ptr.next
                any_active = True
            curr_h = curr_h.next
        if not any_active:
            break
    print()

solve()