if __name__ == "__main__":
    pass



def Bell(L):
    if not L:
        return []

    sorted_L = sorted(L)

    result = []
    left, right = 0, len(sorted_L) - 1
    from_left = True  

    while left <= right:
        if from_left:
            result.append(sorted_L[left])
            left += 1
        else:
            result.append(sorted_L[right])
            right -= 1
        from_left = not from_left

    return result
