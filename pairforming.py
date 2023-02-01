def sockMerchant(n, ar):
    socks = {}
    count = 0
    for i in ar:
        if i not in socks:
            socks[i] = 1
        else:
            socks[i] += 1
            if socks[i] % 2 == 0:
                count += 1
    return count
*The remove operation in a list is time-consuming as it takes O(n) time in the worst case. It's better to use a dictionary to keep track of the count of each color of socks, which will eliminate the need for the remove operation and reduce the overall time complexity.
