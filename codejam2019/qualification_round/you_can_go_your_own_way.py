def _read_input():
    n = int(input())
    p = input()
    assert len(p) == 2 * (n - 1)

    return p


def _format_output(output):
    return ''.join(output)


def _solve(input_data):
    return ['E' if ch == 'S' else 'S' for ch in input_data]


def _main():
    t = int(input())

    for case_num in range(1, t + 1):
        input_data = _read_input()
        output = _solve(input_data)
        print('Case #{}: {}'.format(case_num, _format_output(output)))


if __name__ == '__main__':
    _main()
