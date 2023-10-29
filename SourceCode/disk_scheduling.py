from copy import copy


def FCFS(Request, Start):
    Sum = 0                         # initialize to 0
    position = Start                # set current position = start
    Order = []                      # creates empty list of name Order
    Order.append(Start)             # adds Start to end of list Order
    # i is the current element in the list(first loop i = 95)
    for i in Request:
        # sum = sum + (distance of current position from next position)
        Sum += abs(i - position)
        position = i                # set position new position (i)
        Order.append(i)             # Add i to the end of the list Order
    return Order, Sum
# ------------------------------------------------------------------------------


def SSTF(Request, Start):
    templist = copy(Request)
    position = Start
    Order = []
    Order.append(Start)
    Sum = 0

    while len(templist) > 0:
        min_diff = float('inf')

        for i in templist:
            diff = abs(position - i)
            if diff < min_diff:
                min_diff = diff
                next_request = i
                j = next_request

        Order.append(j)
        Sum += abs(position - j)
        position = j
        templist.remove(j)

    return Order, Sum
# ------------------------------------------------------------------------------


def SCAN(Request, Start):
    n = len(Request)
    Order = []
    Request_tmp = copy(Request)
    Request_tmp.sort()
    if Start != 0 and Start < Request_tmp[n - 1]:
        Request_tmp.append(0)
    p = len(Request_tmp)

    i = Start - 1
    Order.append(Start)
    while i >= 0:
        for j in range(0, p):
            if Request_tmp[j] == i:
                Order.append(i)
        i -= 1

    k = Start + 1
    while k < 210:
        for l in range(0, n):
            if Request[l] == k:
                Order.append(k)
        k += 1

    Sum = 0
    for p in range(0, len(Order) - 1):
        Sum += abs(Order[p] - Order[p + 1])
    return Order, Sum
# ------------------------------------------------------------------------------


def CSCAN(Request, Start):
    n = len(Request)
    Order = []
    Request_tmp = Request.copy()
    Request_tmp.sort()
    if Start != 0 and Start < Request_tmp[n - 1]:
        Request_tmp.append(210)
    p = len(Request_tmp)

    i = Start
    Order.append(Start)

    # Move right until the outer boundary
    while i <= 210:
        for j in range(p):
            if Request_tmp[j] == i:
                Order.append(i)
        i += 1

    # Move to the outer least boundary
    Order.append(0)

    # Move right with services
    k = 0
    while k <= Start:
        for l in range(n):
            if Request[l] == k:
                Order.append(k)
                break
        k += 1

    Sum = 0
    for p in range(0, len(Order) - 1):
        Sum += abs(Order[p] - Order[p + 1])

    return Order, Sum
# ------------------------------------------------------------------------------


def CLOOK(Request, Start):
    n = len(Request)
    Order = []
    i = Start
    Order.append(Start)

    # Move right until the outer boundary
    while i <= 210:
        for j in range(n):
            if Request[j] == i:
                Order.append(i)
        i += 1

    k = 0
    while k <= Start:
        for l in range(n):
            if Request[l] == k:
                Order.append(k)
                break
        k += 1

    Sum = 0
    for p in range(0, len(Order) - 1):
        Sum += abs(Order[p] - Order[p + 1])

    return Order, Sum
