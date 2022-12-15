from time import perf_counter

with open('AdventCode/input15.txt', 'r') as file:
    location = []
    for f in file:
        f = [x.rstrip(",:") for x in f.rstrip('\n').split()]
        x1 = int(f[2].split('=')[1])
        y1 = int(f[3].split('=')[1])
        x2 = int(f[-2].split('=')[1])
        y2 = int(f[-1].split('=')[1])
        location.append([(x1, y1), (x2, y2)])


min_x = min(min(i[0] for i in row) for row in location)
max_x = max(max(i[0] for i in row) for row in location)
#min_y = min(min(i[1] for i in row) for row in location)
#max_y = max(max(i[1] for i in row) for row in location)


# Part 1
all_set = set()
for row_1 in location:
    all_set.add((row_1[1][1], row_1[1][0]))
    all_set.add((row_1[0][1], row_1[0][0]))

# Takes about 3 minutes to run
def no_beacons(location):
    row_interest = 2000000
    #row_interest = 10
    counter = 0
    for i in range(2 * min_x, 2 * (max_x + 1)):
        #print(i)
        for row in location:
            manhattan_b = abs(row[1][0] - row[0][0]) + abs(row[1][1] - row[0][1])
            manhattan_cur = abs(row_interest - row[0][1]) + abs(i - row[0][0])
            if manhattan_cur <= manhattan_b and (row_interest, i) not in all_set:
                counter += 1
                break
    return counter

#print(f'Counter is {no_beacons(location)}')


# Part 2
# Very fast
def distress_super_fast(location):

    def check(i, j):
        occupied = False
        for row_2 in location:
            manhattan_b = abs(row_2[1][0] - row_2[0][0]) + abs(row_2[1][1] - row_2[0][1])
            manhattan_cur = abs(i - row_2[0][1]) + abs(j - row_2[0][0])
            if manhattan_cur <= manhattan_b or (i, j) in all_set:
                occupied = True
                break
        if not occupied:
            return j * 4000000 + i
        else:
            return -1

    for row_1 in location:
        #max_num = 20
        max_num = 4_000_000
        manhattan = abs(row_1[1][0] - row_1[0][0]) + abs(row_1[1][1] - row_1[0][1])
        row_start = row_1[0][1] - manhattan - 1 if row_1[0][1] - manhattan - 1 > 0 else 0
        row_finish = row_1[0][1] + manhattan + 1 if row_1[0][1] + manhattan + 1 < max_num else max_num

        col_center = row_1[0][0]
        tmp = 0
        for i in range(row_start, (row_finish + row_start) // 2):
            if col_center - tmp < 0 or col_center + tmp > max_num:
                continue
            checked1 = check(i, col_center - tmp)
            checked2 = check(i, col_center + tmp)
            if checked1 != -1:
                return checked1
            if checked2 != -1:
                return checked2
            tmp += 1

        tmp = 0
        for i in range(row_finish, (row_finish + row_start) // 2, -1):
            if col_center - tmp < 0 or col_center + tmp > max_num:
                continue
            
            checked1 = check(i, col_center - tmp)
            if checked1 != -1:
                return checked1

            checked2 = check(i, col_center + tmp)
            if checked2 != -1:
                return checked2
            tmp += 1

    return -1


#time1 = perf_counter()
print(f'Distress location is {distress_super_fast(location)}')
#time2 = perf_counter()
#print(time2 - time1)
