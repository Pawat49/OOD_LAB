class DoublyNode:
    def __init__(self, value=None, previous=None, next=None):
        self.value = value
        self.previous = previous
        self.next = next

class DoublyCircularLinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def appendHead(self, value):
        val = value.value
        new_node = DoublyNode(val)

        self.head = new_node
        self.tail = new_node
        # Because it's circular, connect it to itself initially
        self.head.next = self.tail
        self.head.previous = self.tail
        
        self._size += 1
        return

    def append(self, value):
        new_node = DoublyNode(value)
        if self.head is None:
            self.appendHead(new_node)
            return
        
        # Connect the new node at the end
        self.tail.next = new_node
        new_node.previous = self.tail
        
        # Make it circular
        new_node.next = self.head
        self.head.previous = new_node
        
        # Update the tail pointer
        self.tail = new_node
        self._size += 1
        return

    def search(self, value):
        if self.head is None:
            return None
        current = self.head
        while True:
            if current.value == value:
                return current
            current = current.next
            if current == self.head:
                break
        return None

    def travasal_forward(self, start, stop, silent_mode=False):
        if self.head is None:
            return 0
            
        current = self.search(start)
        if current is None:
            return 0
            
        count = 0
        route_str = ""
        
        # Traverse until we hit the destination
        while True:
            route_str += f"{current.value}"
            if current.value == stop:
                break
            route_str += "->"
            current = current.next
            count += 1
            
        if not silent_mode:
            print(f"Forward Route: {route_str},{count}")
            
        return count

    def travasal_backward(self, start, stop, silent_mode=False):
        if self.head is None:
            return 0
            
        current = self.search(start)
        if current is None:
            return 0
            
        count = 0
        route_str = ""
        
        # Traverse backward until we hit the destination
        while True:
            route_str += f"{current.value}"
            if current.value == stop:
                break
            route_str += "->"
            current = current.previous
            count += 1
            
        if not silent_mode:
            print(f"Backward Route: {route_str},{count}")
            
        return count

def convertListtoLinkList(ls):
    c_link = DoublyCircularLinkList()
    for l in ls:
        c_link.append(l)
    return c_link

print("***Railway on route***")
input_data = input("Input Station name/Source, Destination, Direction(optional): ").split("/")

# Parse inputs
station_name = input_data[0].split(",")
direction_args = input_data[1].split(",")

# Build the Linked List
myLinkList = convertListtoLinkList(station_name)

# Extract Source, Destination, and Direction (if any)
source = direction_args[0]
destination = direction_args[1]
direction = direction_args[2] if len(direction_args) > 2 else None

# Process output based on provided arguments
if not direction:
    # If no direction is specified, check which route is shorter
    # Use 'silent_mode' to just get the distance without printing
    forward_dist = myLinkList.travasal_forward(source, destination, silent_mode=True)
    backward_dist = myLinkList.travasal_backward(source, destination, silent_mode=True)
    
    if forward_dist < backward_dist:
        myLinkList.travasal_forward(source, destination)
    elif forward_dist == backward_dist:
        myLinkList.travasal_forward(source, destination)
        myLinkList.travasal_backward(source, destination)
    else:
        myLinkList.travasal_backward(source, destination)
        
elif direction == "F":
    myLinkList.travasal_forward(source, destination)
elif direction == "B":
    myLinkList.travasal_backward(source, destination)