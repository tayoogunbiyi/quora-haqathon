# https://www.quora.com/q/quorahaqathon/Quora-Haqathon-Upvotes

from typing import List, Tuple


def read_input() -> Tuple[int, List[int]]:
    input_lines: List[str] = []
    while True:
        try:
            input_lines.append(input().strip())
        except EOFError:
            break

    K = int(input_lines[0].split(" ")[1])
    upvote_data = list(map(int, input_lines[1].split(" ")))

    return (K, upvote_data)


window_sz, upvote_data = read_input()


def count_non_incr_and_non_decr_subranges(arr: List[int], start: int, end: int) -> int:
    non_incr_count = 0
    non_decr_count = 0
    for i in range(start, end + 1):
        for j in range(i + 2, end + 1):
            is_non_incr = all([arr[k] >= arr[k + 1] for k in range(i, j - 1)])
            non_incr_count += 1 if is_non_incr else 0
            is_non_decr = all([arr[k] >= arr[k - 1] for k in range(i + 1, j)])
            non_decr_count += 1 if is_non_decr else 0

    return non_incr_count, non_decr_count


def solve(arr: List[int], window_size: int):
    result = []
    for i in range(len(arr) - window_size + 1):
        non_incr_subranges, non_decr_subranges = count_non_incr_and_non_decr_subranges(
            arr, i, i + window_size
        )
        result.append(non_decr_subranges - non_incr_subranges)

    for v in result:
        print(v)


MAX = 100007

# key ideas from - https://discuss.codechef.com/t/coex06-editorial/12385
def solve2(arr: List[int], window_size: int):
    dp1 = [[0 for _ in range(MAX)] for _ in range(2)]
    dp2 = [[0 for _ in range(MAX)] for _ in range(2)]

    for i in range(len(arr)):
        dp1[0][i] = 1 + (dp1[0][i - 1] if (i > 0 and arr[i] >= arr[i - 1]) else 0)
        dp2[0][i] = 1 + (dp2[0][i - 1] if (i > 0 and arr[i] <= arr[i - 1]) else 0)

    for i in range(len(arr) - 1, -1, -1):
        dp1[1][i] = 1 + (
            dp1[1][i + 1] if i < len(arr) - 1 and arr[i] >= arr[i + 1] else 0
        )
        dp2[1][i] = 1 + (
            dp2[1][i + 1] if i < len(arr) - 1 and arr[i] <= arr[i + 1] else 0
        )

    incr_count = sum([dp1[0][i] for i in range(window_size - 1)])
    decr_count = sum([dp2[0][i] for i in range(window_size - 1)])

    for i in range(window_size - 1, len(arr)):
        incr_count += min(window_size, dp1[0][i])
        decr_count += min(window_size, dp2[0][i])

        print(incr_count - decr_count)

        incr_count -= min(window_size, dp2[1][i - (window_size - 1)])
        decr_count -= min(window_size, dp1[1][i - (window_size - 1)])


# solve(upvote_data, window_sz)
solve2(upvote_data, window_sz)
