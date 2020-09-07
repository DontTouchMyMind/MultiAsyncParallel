def read_ints(path):
    lst = []
    with open(path, 'r') as f:
        while line := f.readline():
            lst.append(int(line))

    return lst


def count_three_sum(ints):
    print('Started count_three_sum function...')

    n = len(ints)
    counter = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if ints[i] + ints[j] + ints[k] == 0:
                    counter += 1
                    print(f'Triple found: {ints[i]}, {ints[j]}, {ints[k]}')

    print(f'Ended count_three_sum. Triplets counter={counter}')


if __name__ == '__main__':
    print('Started main.')

    ints = read_ints('../data/1Kints.txt')
    count_three_sum(ints)

    print('What are we waiting for?')
    print('Ended main.')
