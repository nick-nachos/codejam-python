def _read_input():
    [n, l] = [int(token) for token in input().split(maxsplit=1)]
    products = [int(token) for token in input().split(maxsplit=(l - 1))]

    return n, products


def _format_output(output):
    return ''.join(output)


def _solve(input_data):
    (n, products) = input_data
    (index, common) = _common_prime(products)
    nums = [common]

    for i in range(index - 1, -1, -1):
        assert products[i] % nums[0] == 0
        nums.insert(0, products[i] // nums[0])

    for i in range(index, len(products)):
        assert products[i] % nums[i] == 0
        nums.append(products[i] // nums[i])

    for num in nums:
        assert num <= n

    nums_ordered = [num for num in set(nums)]
    nums_ordered.sort()
    mappings = {}

    assert len(nums_ordered) == 26

    for i in range(0, len(nums_ordered)):
        mappings[nums_ordered[i]] = chr(ord('A') + i)

    letters = [mappings[num] for num in nums]

    assert len(letters) == len(products) + 1

    return letters


def _common_prime(products):
    for i in range(1, len(products)):
        if products[i - 1] != products[i]:
            return i, _gcd(products[i - 1], products[i])

    raise ValueError()


def _gcd(x, y):
    while y > 0:
        x, y = y, x % y

    return x


def _main():
    t = int(input())

    for case_num in range(1, t + 1):
        input_data = _read_input()
        output = _solve(input_data)
        print('Case #{}: {}'.format(case_num, _format_output(output)))


if __name__ == '__main__':
    _main()
