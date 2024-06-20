def load_file(file_name):
    """ Reads integers from a file.
    The file should have one integer per line """
    with open(file_name) as infile:
        integers = [int(line) for line in infile.read().splitlines()]
    return integers

def reversed_selection_sort(file_name):
    """ Loads numbers from the given file and returns them as a sorted list.
    The numbers are sorted using selection sort - surprise, surprise!
    """
    alist = load_file(file_name)
    n_comps = 0
    for fill_slot in range(len(alist) -1, 0, -1):
        index_of_max = 0
        for location in range(1, fill_slot +1):
            if alist[location] < alist[index_of_max]:
                n_comps += 1  # this is my code and not part of the template
                index_of_max = location
        # swap items in fill_slot and index_of_max - puts max into fill_slot
        alist[fill_slot], alist[index_of_max] = alist[index_of_max], alist[fill_slot]

    # Note: you will need to count the comparisons
    print('Selection sort on {}, {} items'.format(file_name, len(alist)))
    print('  Used {} comparisons.\n'.format(n_comps))
    return alist
