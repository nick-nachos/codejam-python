def _read_input():
    # TODO: add impl here
    return None


def _format_output(output):
    # TODO: add impl here
    return None


def _solve(input_data):
    # TODO: add impl here
    return None


def _main():
    t = int(input())

    for case_num in range(1, t + 1):
        input_data = _read_input()
        output = _solve(input_data)
        print('Case #{}: {}'.format(case_num, _format_output(output)))


if __name__ == '__main__':
    _main()
