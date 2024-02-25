def out_of_bound(dims, pos):
    row = pos[0]
    col = pos[1]
    if row < 0 or col < 0 or row >=dims[0] or col > dims[1]:
        return True
    return False
