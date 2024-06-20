def  parent_index_7_heap(child_index):
    """Returns the parent of the given child, else it retruns None if the child 
       has no parent ie the root"""
       
    if child_index == 1:
        return None
    else:
        if child_index == 2:
            return 1
        else:
            return (child_index-1)//2
    
print(parent_index_7_heap(2))
print(parent_index_7_heap(11))