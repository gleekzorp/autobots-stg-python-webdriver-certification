def max_min(string):

    final_data = sorted(string.split(), key=len)
    minimum = final_data[0]
    maximum = final_data[-1]
    return maximum, minimum


def the_real_max_min(string):
    final_data = sorted(string.split(), key=len)
    minimum = final_data[0]
    maximum = final_data[-1]

    the_real_max = []
    for x in final_data:
        if len(x) == len(maximum):
            the_real_max.append(x)

    the_real_min = []
    for x in final_data:
        if len(x) == len(minimum):
            the_real_min.append(x)

    return the_real_max, the_real_min


def test_longest():
    assert max_min('the is the greatest sentence') == ('sentence', 'is')


def test_max_min():
    result = max_min('a cow jumped over the moon')
    print(result)
    assert result[0] > result[1]


def test_the_real_max_min():
    result = the_real_max_min('a cow jumped over the moon and jumped again')
    print(result)
    assert len(result[0]) > len(result[1])


# Checkout these
# max()
# min()