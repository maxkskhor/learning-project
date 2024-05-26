# wrong practice: mutable as default argument
def append(n, store=[]):
    store.append(n)
    print(f'Current list is: {store}')
    return store


# correct practice
def correct_append(n, store=None):
    if store is None:
        store = []
    store.append(n)
    print(f'Current list is: {store}')
    return store


if __name__ == '__main__':
    print('Bad practice')
    l1 = append(0)
    l2 = append(1)
    print('Good practice')
    l3 = correct_append(0)
    l4 = correct_append(1)
