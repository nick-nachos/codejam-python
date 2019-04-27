from sys import stdout
from sys import exit


_CORRECT = 'CORRECT'
_WRONG_ANSWER = 'WRONG_ANSWER'


def _read_line():
    input_text = input()

    if input_text == _WRONG_ANSWER:
        exit(1)

    return input_text


def _read_input():
    input_text = _read_line()

    if input_text == _CORRECT:
        exit(1)

    # TODO: add impl here
    return None


def _init_answer(init_input):
    # TODO: add impl here
    return None


def _format_init_answer(init_answer):
    # TODO: add impl here
    return None


def _read_response():
    input_text = _read_line()

    if input_text == _CORRECT:
        return _CORRECT

    # TODO: add impl here
    return None


def _inter_answer(response, state):
    # TODO: add impl here
    return None


def _format_inter_answer(inter_answer):
    # TODO: add impl here
    return None


def _main():
    t = int(input())

    for case_num in range(1, t + 1):
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
