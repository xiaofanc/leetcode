"""
You are given an array of non-negative integers numbers. You are allowed to choose any number from this array and swap any two digits in it. If after the swap operation the number contains leading zeros, they can be omitted and not considered (eg: 010 will be considered just 10).
Your task is to check whether it is possible to apply the swap operation at most once, so that the elements of the resulting array are strictly increasing.

For numbers = [1, 5, 10, 20], the output should be solution(numbers) = true.
For numbers = [1, 3, 900, 10], the output should be solution(numbers) = true.
For numbers = [1000, 10, 100], the output should be solution(numbers) = true.
For numbers = [13, 31, 30], the output should be solution(numbers) = false.
"""

# 19/20 passed
def solution(numbers):
    if numbers == sorted(numbers):
        return True
    
    swap = 0
    for i in range(len(numbers)):
        # edge case: the first number and the last number
        if (i == 0 or numbers[i-1] < numbers[i]) and (i == len(numbers)-1 or numbers[i] < numbers[i+1]):
            continue
        else:
            # swap 2 sigits in numbers[i] to make it > numbers[i-1] and < numbers[i+1]
            # print("swap....", numbers[i])
            temp = [c for c in str(numbers[i])]
            # if more than one swap is needed
            if swap == 1:
                return False
            success = False
            for x in range(len(temp)):
                for y in range(x+1, len(temp)):
                    temp[x], temp[y] = temp[y], temp[x]
                    new = int("".join(temp)) 
                    # if success
                    if (i == 0 or new > numbers[i-1]) and (i == len(numbers)-1 or new < numbers[i+1]):
                        numbers[i] = new
                        success = True
                        swap += 1
                        break # y
                    else:
                        # return back to the original number
                        temp = [c for c in str(numbers[i])] 
                if success:
                    break # x
            # if no swap is successful
            if not success:
                return False
    return True
                        
                    
                
        


                        
                    
                
        

