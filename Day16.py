from collections import defaultdict, deque
from math import inf

def read_file(file_path):
    path = defaultdict(list)
    flow = defaultdict(int)
    with open(file_path, 'r') as file:
        for f in file:
            f = f.rstrip('\n').split()
            flow[f[1]] = int(f[4].split('=')[1].rstrip(';'))
            i = -1
            while f[i] != 'valves' and f[i] != 'valve':
                path[f[1]].append(f[i].rstrip(','))
                i -= 1
    return path, flow


def find_all_paths(path, flow):
    connections = defaultdict(list)
    for p in path.keys():
        for q in path.keys():
            if p == q: continue

            steps = 0
            seen = set(p)
            queue = deque([(p, steps)])
            
            while queue:
                cur_path, steps = queue.popleft()
                if cur_path == q:
                    connections[p].append((q, steps))
                    break

                for i in path[cur_path]:
                    if i not in seen:
                        queue.append((i, steps + 1))
                        seen.add(i)

    return connections


def dp1(all_connections, flow):
    # Part 1
    cur_pos = 'AA'
    pressure, time = 0, 0
    path_visited = {'AA'}
    time_lim = 30
    max_pressure = 0


    queue = deque([(cur_pos, pressure, time, path_visited)])

    while queue:
        cur_pos, pressure, time, path_visited = queue.popleft()

        if pressure > max_pressure: max_pressure = pressure

        for i in all_connections[cur_pos]:

            if time + i[1] + 1 <= time_lim and i[0] not in path_visited and flow[i[0]] != 0:
                pressure_tmp = flow[i[0]] * (time_lim - time - i[1] - 1)
                queue.append((i[0], pressure + pressure_tmp, time + i[1] + 1, path_visited.union({i[0]})))

    return max_pressure



def dp3(all_connections, flow, time_lim, path_given, allOutput=False):
    # Part 1
    cur_pos = 'AA'
    time, pressure = 0, 0
    path_visited = path_given.union({cur_pos})

    max_pressure = 0
    all_paths = []

    queue = deque([(cur_pos, pressure, time, path_visited)])

    while queue:
        cur_pos, pressure, time, path_visited = queue.popleft()

        if pressure > max_pressure: max_pressure = pressure

        for i in all_connections[cur_pos]:

            if time + i[1] + 1 <= time_lim and i[0] not in path_visited and flow[i[0]] != 0:
                pressure_tmp = flow[i[0]] * (time_lim - time - i[1] - 1)
                queue.append((i[0], pressure + pressure_tmp, time + i[1] + 1, path_visited.union({i[0]})))
                all_paths.append((queue[-1][-1], queue[-1][-3]))

    return (max_pressure, all_paths) if allOutput else max_pressure


def dp2(all_connections, flow):
    # Part 2
    cur_pos = ['AA', 'AA']
    pressure = 0
    time = [0, 0]                  
    path_visited = {'AA'}
    time_lim = 26
    max_pressure = 0


    queue = deque([(cur_pos, pressure, time, path_visited)])
    print(len(queue))
    while queue:
        cur_pos, pressure, time, path_visited = queue.popleft()

        if pressure > max_pressure: 
            max_pressure = pressure

        for i in all_connections[cur_pos[0]]:
            if time[0] + i[1] + 1 <= time_lim and i[0] not in path_visited and flow[i[0]] != 0:
                pressure_tmp = flow[i[0]] * (time_lim - time[0] - i[1] - 1)
                for j in all_connections[cur_pos[1]]:
                    if j[0] == i[0]: continue
                    if time[1] + j[1] + 1 <= time_lim and j[0] not in path_visited and flow[j[0]] != 0:
                        pressure_tmp_2 = flow[j[0]] * (time_lim - time[1] - j[1] - 1)
                        queue.append(([i[0], j[0]], pressure + pressure_tmp + pressure_tmp_2, [time[0] + i[1] + 1, time[1] + j[1] + 1], path_visited.union({i[0], j[0]})))
    return max_pressure

def greedy(all_connections, flow):
    # Wrong answer
    cur_pos = 'AA'
    time_left = 30
    seen = set()
    pressure = 0

    while time_left > 0:
        press_tmp = -inf
        for i in all_connections[cur_pos]:
            if time_left - i[1] * 1 - 1 >= 0 and (time_left - i[1] * 1 - 1) * flow[i[0]] > press_tmp and i[0] not in seen:
                press_tmp = (time_left - i[1] * 1 - 1) * flow[i[0]]
                next_path, time_taken = i[0], i[1] * 1 + 1

        if press_tmp == -inf: break
        cur_pos = next_path
        seen.add((next_path))
        time_left -= time_taken
        pressure += press_tmp
        if len(seen) == len(all_connections): break

    return pressure

if __name__ == '__main__':
    file_path = 'AdventCode/input16.txt'
    path, flow = read_file(file_path)

    all_connections = find_all_paths(path, flow)

    # Part 1
    time_limit = 30
    #res = dp3(all_connections, flow, time_limit, set(), False)
    #print(res)

    # Part 2
    time_limit = 26
    res, all_paths = dp3(all_connections, flow, time_limit, set(), True)
    print(len(all_paths))

    non_zero_pres = 0
    for i in flow.values():
        if i != 0: non_zero_pres += 1

    max_press = res
    counter = 0
    for i in all_paths:
        if len(i[0]) == 7 or len(i[0]) == 8 or len(i[0]) == 9:
            res_tmp = dp3(all_connections, flow, time_limit, i[0], False)
            if res_tmp + i[1] > max_press:
                max_press = res_tmp + i[1]
            counter += 1
    print(max_press)



