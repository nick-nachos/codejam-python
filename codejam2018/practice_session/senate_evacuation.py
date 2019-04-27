from sys import stdin


def _read_input():
    party_num = int(stdin.readline())
    return [int(rep_count) for rep_count in stdin.readline().split(maxsplit=party_num - 1)]


def _format_output(output):
    def party_letter(party_id):
        return chr(ord('A') + party_id)

    def exit_step(party_ids):
        return ''.join([party_letter(party_id) for party_id in party_ids])

    return ' '.join([exit_step(plan_step) for plan_step in output])


def _solve(input_data):
    reps_by_party = [[party_id, input_data[party_id]] for party_id in range(0, len(input_data))]
    reps_by_party.sort(key=lambda t: t[1], reverse=True)
    first = reps_by_party[0][1]
    rest = sum([reps_by_party[party_id][1] for party_id in range(1, len(reps_by_party))])
    current_removing = 1
    exit_plan = []

    def remove_rep():
        nonlocal current_removing, rest

        if reps_by_party[current_removing][1] == 0:
            current_removing += 1

        reps_by_party[current_removing][1] -= 1
        rest -= 1

    while first + rest > 0:
        plan_step = []

        remove_rep()
        plan_step.append(reps_by_party[current_removing][0])

        if rest > first:
            remove_rep()
            plan_step.append(reps_by_party[current_removing][0])
        elif first > rest:
            first -= 1
            plan_step.append(reps_by_party[0][0])

        exit_plan.append(plan_step)

    return exit_plan


def _main():
    n = int(stdin.readline())

    for case_num in range(1, n + 1):
        input_data = _read_input()
        output = _solve(input_data)
        print('Case %d: %s' % (case_num, _format_output(output)))


if __name__ == '__main__':
    _main()
