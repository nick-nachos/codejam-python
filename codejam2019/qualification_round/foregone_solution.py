def _read_input():
    return input()


def _format_output(output):
    return '%s %s' % output


def _solve(input_data):
    digits = [int(digit) for digit in input_data]
    digits1 = [str(1 if digit == 4 else 0) for digit in digits]
    digits2 = [str(digit - 1 if digit == 4 else digit) for digit in digits]
    num_str1 = ''.join(digits1).lstrip('0')
    num_str2 = ''.join(digits2)

    return num_str1, num_str2


def _main():
    t = int(input())

    for case_num in range(1, t + 1):
        input_data = _read_input()
        output = _solve(input_data)
        print('Case #{}: {}'.format(case_num, _format_output(output)))


def _test():
    for i in range(0, 10000):
        text = str(i)

        if '4' in text:
            num1, num2 = _solve(text)
            assert str(int(num1)) == num1
            assert str(int(num2)) == num2
            assert int(text) == int(num1) + int(num2)


if __name__ == '__main__':
    _main()
    # _test()
