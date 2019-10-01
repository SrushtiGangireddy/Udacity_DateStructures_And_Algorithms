def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """
    curr = head
    odd = None
    even = None
    odd_list = None
    even_list = None
    while curr:
        next_node = curr.next
        
        if curr.data % 2 == 0:
            if even is None:
                even = curr
                even_list = even
            else:
                even_list.next = curr
                even_list = even_list.next
        else:
            if odd is None:
                odd = curr
                odd_list = odd
            else:
                odd_list.next = curr
                odd_list = odd_list.next
        curr.next = None
        curr = next_node
    
    if odd is None:
        return even
    odd_list.next = even
    return odd
        
