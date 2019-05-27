to_find = [1, 2, 3, 4]


def non_linear_combo(arr):
    cur = []

    if not arr:
        return []
    else:
        cur.append(arr[0])
        for x in non_linear_combo(arr[1:]):
            cur.append([x])
            cur.append([arr[0], x])
        return cur


def remove_nesting(l, linear_list):
    if type(l) != list:
        linear_list.append(l)
    else:
        for i in l:
            if type(i) == list:
                remove_nesting(i, linear_list)
            else:
                linear_list.append(i)


def linear_combo(arr):
    result = [[]]

    for c in non_linear_combo(arr):
        linear = []
        remove_nesting(c, linear)
        result.append(linear)

    return result


def main():
    print(linear_combo(to_find))


if __name__ == '__main__':
    main()