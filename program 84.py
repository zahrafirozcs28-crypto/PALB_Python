def time_to_seconds(t):
    h, m, s = map(int, t.split(':'))
    return h * 3600 + m * 60 + s

def min_time_difference(arr):
    seconds = sorted([time_to_seconds(t) for t in arr])
    
    min_diff = float('inf')
    total_seconds_in_day = 24 * 3600
    
    for i in range(len(seconds) - 1):
        min_diff = min(min_diff, seconds[i+1] - seconds[i])
        
    wrap_around_diff = (total_seconds_in_day - seconds[-1]) + seconds
    min_diff = min(min_diff, wrap_around_diff)
    
    return min_diff

arr1 = ["12:30:15", "12:30:45"]
print(min_time_difference(arr1))

arr2 = ["00:00:01", "23:59:59", "00:00:05"]
print(min_time_difference(arr2))
