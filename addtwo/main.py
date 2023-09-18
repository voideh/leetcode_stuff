class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return walk_list(self)


def create(ns: list[int]) -> ListNode:
    head = ListNode(val=ns[0])
    curr = head
    for n in ns[1:]:
        curr.next = ListNode(val = n)
        curr = curr.next
    return head

def walk_list(head: ListNode) -> str:
    curr = head
    st = '['
    while curr:
        st += f'{curr.val}'
        if curr.next:
            st += ','
        curr = curr.next
    return st + ']'
        
def add_two(l1: ListNode, l2: ListNode) -> ListNode:
    def nxt(self: ListNode):
        if self.next:
            return self.next 
        else:
            raise StopIteration
    ListNode.__iter__ = lambda self: self.val
    ListNode.__next__ = nxt
    ls_to_int = lambda ns: int(''.join(reversed([str(n) for n in ns])))
    n1 = ls_to_int(l1)
    n2 = ls_to_int(l2)
    s = n1 + n2
    int_to_ls = lambda n: [int(d) for d in reversed(str(n))]
    res = int_to_ls(s)
    head = ListNode(val=res[0])
    curr = head
    for n in res[1:]:
        curr.next = ListNode(val = n)
        curr = curr.next
    return head


def add_two_agg(l1: ListNode, l2: ListNode) -> ListNode:
    # get all nums
    def walk(ln: ListNode) -> list[int]:
        curr = ln
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
    # create lists
    ns1 = walk(l1)
    ns2 = walk(l2)

    # convert back and forth
    list_to_int = lambda ns: int(''.join(reversed([str(n) for n in ns])))
    s = list_to_int(ns1) + list_to_int(ns2)
    cnv = str(s)[::-1]

    head = ListNode(val=int(cnv[0]))
    curr = head
    for n in cnv[1:]:
        curr.next = ListNode(val=int(n))
        curr = curr.next

    return head
    







l1 = [2,4,3]
l2 = [5,6,4]

n1 = create(l1)
n2 = create(l2)


print(add_two_agg(n1, n2))