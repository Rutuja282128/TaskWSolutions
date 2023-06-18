def mySqrt(x):
    if x == 0:
        return 0

    left, right = 1, x

    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1

    return right


x = 4
print(mySqrt(x))

x = 8
print(mySqrt(x))