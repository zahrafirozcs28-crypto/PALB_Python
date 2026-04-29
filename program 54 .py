def min_people_to_cover(arr):
    n = len(arr)
    intervals = []
    
    for i in range(n):
        if arr[i] != -1:
            start = max(0, i - arr[i])
            end = min(n - 1, i + arr[i])
            intervals.append((start, end))
    
    intervals.sort()
    
    count = 0
    current_end = -1
    i = 0
    num_intervals = len(intervals)
    
    while current_end < n - 1:
        farthest = current_end
        found = False
        
        while i < num_intervals and intervals[i] <= current_end + 1:
            if intervals[i] > farthest:
                farthest = intervals[i]
                found = True
            i += 1
            
        if not found:
            return -1
        
        current_end = farthest
        count += 1
        
    return count

# Example 1
print(min_people_to_cover()) 

# Example 2
print(min_people_to_cover([2, 3, 4, -1, 2, 0, 0, -1, 0]))

# Example 3
print(min_people_to_cover([0, 1, 0, -1]))
