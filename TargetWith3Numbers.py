def target_with3(arr, target):
    arr.sort()
    for i in range(len(arr)):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            sum = arr[i] + arr[left] + arr[right]
            if sum == target:
                return True
            elif sum > target:
                right -= 1
            else:
                left += 1
    return False
