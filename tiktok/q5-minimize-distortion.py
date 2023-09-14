"""
distortion = max abs difference between adjacent elements of the array.
replace 0 in the array with x and x is in the range of [0, max_frame] to minimize the distortion
given arr = [4,0,3,2], max_frame = 2 => return 2
"""

def calculate_distortion(arr):
    return max(abs(arr[i] - arr[i+1]) for i in range(len(arr)-1))

def minimize_distortion(arr, max_frame):
    initial_distortion = calculate_distortion(arr)
    min_distortion = initial_distortion
    
    for x in range(max_frame + 1):
        modified_arr = [x if val == 0 else val for val in arr]
        distortion = calculate_distortion(modified_arr)
        min_distortion = min(min_distortion, distortion)
    
    return min_distortion

# Example usage:
arr = [4, 0, 3, 2]
max_frame = 2
result = minimize_distortion(arr, max_frame)
print(result)  # Output: 2



