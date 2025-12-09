def jobseq(jobs: list[tuple[int, int]]) -> tuple[int, int]:
    profit: list[int] = []

    slots = [0 for _ in jobs]
    for job in sorted(jobs, key=lambda x: x[0], reverse=True):
        for j in range(-job[1], 0):
            if slots[j]:
                continue
            slots[j] = 1
            profit.append(job[0])
            break

    return len(profit), sum(profit)


assert jobseq([(100, 2), (19, 1), (27, 2), (25, 1), (15, 1)]) == (2, 127)
assert jobseq([(60, 2), (100, 1), (20, 3), (40, 2), (20, 1)]) == (3, 180)
assert jobseq([(201, 5), (181, 3), (191, 3), (301, 2), (121, 4), (101, 2)]) == (5, 995)
