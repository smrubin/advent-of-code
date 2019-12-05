with open('./day2.txt') as f:
    data = f.read()
    original = list(map(lambda i: int(i), data.split(',')))


def gravity_assist(noun, verb):
    inputs = original.copy()  # reset list

    # adjust inputs according to problem for part 1
    # inputs[1] = 12
    # inputs[2] = 2

    # adjust inputs as args for part 2
    inputs[1] = noun
    inputs[2] = verb

    index = 0
    while index <= len(inputs) - 4:
        intcode = inputs[index]

        # if intcode is 99 immediately halt (by setting index to length of list
        if intcode == 99:
            index = len(inputs)
        else:
            first = inputs[inputs[index + 1]]
            second = inputs[inputs[index + 2]]
            target = inputs[index + 3]

            if intcode == 1:
                inputs[target] = first + second
            elif intcode == 2:
                inputs[target] = first * second

            index = index + 4

    output = inputs[0]
    return output


# part 2. mark 1: brute force
goal = 19690720
n = None
v = None
for i in range(100):
    for j in range(100):
        if gravity_assist(i, j) == goal:
            n = i
            v = j

print(100 * n + v)
