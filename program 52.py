def get_min_in_range(a, r1, r2, c1, c2):
    if r1 > r2 or c1 > c2:
        return 0
    res = float('inf')
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            if a[i][j] < res:
                res = a[i][j]
    return res if res != float('inf') else 0

def solve_construction_cost(n, m, a, queries):
    outputs = []
    for R, C in queries:
        r, c = R - 1, C - 1
        
        tl = get_min_in_range(a, 0, r - 1, 0, c - 1)
        tr = get_min_in_range(a, 0, r - 1, c + 1, m - 1)
        bl = get_min_in_range(a, r + 1, n - 1, 0, c - 1)
        br = get_min_in_range(a, r + 1, n - 1, c + 1, m - 1)
        
        outputs.append(tl + tr + bl + br)
    return outputs

n = 3
m = 3
a = [,,]
q_list = []

result = solve_construction_cost(n, m, a, q_list)
for val in result:
    print(val)
