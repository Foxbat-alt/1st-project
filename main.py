def print_christmas_tree(height):
    for i in range(height):
        print(' ' * (height - i - 1) + '*' * (2 * i + 1))
    print(' ' * (height - 1) + '|')

    #x0 = "apple",y0 = "adcsfgyappa" --> True if all characters in x0 are in y0 in order,y0="bsdpple" --> False,"y0 = apple"-->True
def is_subsequence(x0, y0):
    it = iter(y0)
    return all(char in it for char in x0)

