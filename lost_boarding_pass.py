# Filtering out invalid permutations inline improved the performance by more than two fold
def lost_boarding_pass_permute(xs, low=0):
    if low + 1 >= len(xs):
        yield xs
    else:
        for p in lost_boarding_pass_permute(xs, low + 1):
            yield p
        for i in range(low + 1, len(xs)):
            # filter out invalid permutations
            if (low != 0 and xs[low] <= xs[i]): continue
            xs[low], xs[i] = xs[i], xs[low]
            for p in lost_boarding_pass_permute(xs, low + 1):
                yield p
            xs[low], xs[i] = xs[i], xs[low]

# Inline filtering allows us to get up to 25 after which the program chokes;  Note:  Using itertools.permutations, we can only get up to 10
max=20
for n in range(3,max+1):
    count = 0
    total = 0
    l = lost_boarding_pass_permute(list(range(1, n+1)))
    for p in l:
        total += 1
        # check if the last person is sitting in her seat
        count += True if (p[len(p)-1] == n) else False
        # uncomment to print the seating arrangement
        #print(p)
    print(f'n={n}: {count} out of {total}')