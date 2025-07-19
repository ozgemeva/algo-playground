class IntFunction:

    def binary_gap(num):
        bin_str = bin(num)[2:]
        gaps = bin_str.strip("0").split("1")
        lengthsList = []
        for gap_len in gaps:
            lenGap = len(gap_len)
            lengthsList.append(lenGap)
            maxNum = max(lengthsList)
        print("lengthsList: ", lengthsList)
        return maxNum

    def missing_integer(arr):
        intarr = []
        initvalu = 1
        for num in arr:
            if num <= 0:
                pass
            else:
                intarr.append(num)
        intset = set(intarr)
        while initvalu in intset:
            initvalu += 1
        return initvalu

    def find_odd(arr):
        result = 0
        for num in arr:
            result ^= num  # xor
        return result

    def tape_equilibrium(arr):
        total = sum(arr)
        left_sum = 0
        min_diff = float("inf")  # çok büyükten başla

        for i in range(len(arr) - 1):  # son elemanda bölme olmaz
            left_sum += arr[i]
            right_sum = total - left_sum
            diff = abs(left_sum - right_sum)

            if diff < min_diff:
                min_diff = diff

        return min_diff

    def rotate(arr, K):
        K = K % len(arr)
        newArr = arr[-K:] + arr[:-K]
        print("K:", K)
        print("arr[-K:] ", arr[-K:])
        print("arr[:-K]", arr[:-K])
        return newArr
