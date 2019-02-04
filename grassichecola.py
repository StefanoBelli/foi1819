def str_mid_same(xs):
    if len(xs) == 1:
        return True

    if not len(xs) % 2:
        l = int(len(xs) / 2)
        if xs[0] == xs[l]:
            return str_mid_same(xs[1:])

        return False

    return str_mid_same(xs[:int(len(xs) / 2)] + xs[int(len(xs) / 2) + 1:])

print(str_mid_same("kiiokik"))

def palindrome(xs):
    xslen = len(xs)
    if xslen <= 1:
        return True

    if xs[0] != xs[xslen - 1:]:
        return False

    return palindrome(xs[1:xslen - 1])

print(palindrome("acca"))
