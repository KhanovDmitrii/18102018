def main(*args):
    return sorted(args)


print(main(3, 2, 1, 49, 0))

if __name__ == '__main__':
    assert main(3, 2, 1, 49, 0) == [0, 1, 2, 3, 49], "Сортировка не удалась"
    assert main(4, 1, 7, 92, 3) == [1, 3, 4, 7, 92], "Сортировка не удалась"
    assert main(9, 21, 1, 38, 98, 56) == [1, 9, 21, 38, 56, 98], "Сортировка не удалась"
