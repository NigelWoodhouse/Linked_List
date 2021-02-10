class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def append(self,data):
        new_node = node(data)
        if self.head is None:
            self.head=new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self,data):
        new_node = node(data)
        new_node.next=self.head
        self.head = new_node

    def length(self):
        total = 0
        cur_node = self.head
        while cur_node:
            total+=1
            cur_node = cur_node.next
        return total

    def length_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.length_recursive(node.next)

    def display(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" ")
            cur_node = cur_node.next
        print("")

    def get(self,index):
        if index>=self.length():
            print("ERROR -> index out of range")
            return None
        cur_idx=0
        cur_node=self.head
        while True:
            cur_node=cur_node.next
            if cur_idx==index:
                return cur_node.data
            cur_idx+=1

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return
        
        new_node = node(data)
        new_node.next=prev_node.next
        prev_node.next = new_node

    def insert_node_at_pos(self,data,pos):
        new_node = node(data)
        cur_node = self.head
        print(cur_node)
        if pos == 0:
            new_node.next = cur_node
            self.head = new_node
            return self
        
        prev = None
        count = 0
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count +=1

        if cur_node is None:
            return
        
        new_node.next=prev.next
        prev.next = new_node
        
    def delete(self,key):
        cur_node=self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        
        prev = None
        while cur_node and cur_node.data!=key:
            prev = cur_node
            cur_node = cur_node.next
        
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self,pos):
        cur_node = self.head
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return
        
        prev = None
        count = 1
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count +=1

        if cur_node is None:
            return
        
        prev.next = cur_node.next
        cur_node = None

    def swap_node(self, key_1, key_2):
        
        if key_1 == key_2:
            return
        
        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next
        
        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next
        
        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.headd = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def reverse_recursive(self):
        def _reverse_recursive(cur,prev):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur,prev)
        self.head = _reverse_recursive(cur=self.head, prev=None)
        


my_list = linked_list()
print(my_list.length())
# print(my_list.isEmpty())
my_list.append("B")
# print(my_list.isEmpty())
my_list.append("C")
my_list.append("D")
my_list.append("E")
my_list.prepend("A")
my_list.display()
# my_list.swap_node("A", "C")
my_list.reverse_recursive()
my_list.display()

# my_list.insert_node_at_pos("Z",3)
# print(my_list.length())
# my_list.display()
# my_list.delete("B")
# print(my_list.length())
# my_list.display()
# print(my_list.length_recursive(my_list.head))