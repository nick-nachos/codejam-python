from sys import stdin
from sys import stdout
from sys import exit


_CORRECT = 'CORRECT'
_WRONG_ANSWER = 'WRONG_ANSWER'


def _read_line():
    input_text = stdin.readline().strip()

    if input_text == _WRONG_ANSWER:
        exit(1)

    return input_text


def _read_input():
    input_text = _read_line()

    if input_text == _CORRECT:
        exit(1)

    a, b = (int(t) for t in input_text.split(maxsplit=1))
    _read_line()

    return a + 1, b


def _init_answer(init_input):
    (a, b) = init_input

    return a, b, (a + b) // 2


def _format_init_answer(init_answer):
    return str(init_answer[2])


def _read_response():
    input_text = _read_line()

    if input_text == _CORRECT:
        return _CORRECT

    return input_text


def _inter_answer(response, state):
    (a, b, mid) = state

    if response == 'TOO_SMALL':
        return _init_answer((mid + 1, b))
    elif response == 'TOO_BIG':
        return _init_answer((a, mid - 1))


def _format_inter_answer(inter_answer):
    return _format_init_answer(inter_answer)


def _main():
    n = int(stdin.readline())

    for case_num in range(1, n + 1):
        init_answer = _init_answer(_read_input())
        print(_format_init_answer(init_answer))
        stdout.flush()
        response = _read_response()
        state = init_answer

        while response != _CORRECT:
            state = _inter_answer(response, state)
            print(_format_inter_answer(state))
            stdout.flush()
            response = _read_response()


if __name__ == '__main__':
    _main()
