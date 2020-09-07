from multithreading.count_three_sum import count_three_sum, read_ints

if __name__ == '__main__':
    print('Started main.')

    ints = read_ints('../data/1Kints.txt')
    count_three_sum(ints)

    print('What are we waiting for?')
    print('Ended main.')
