def __rle_util_encoder(enct, c, ccount):
    if ccount <= 2:
        enct += c * ccount
    else:
        enct += str(ccount) + c

    return enct

def encode(xs):
    count = 1
    prevc = 0
    encoded_text = ""

    for ch in xs:
        if ch.isdigit():
            return None

        if ch != prevc:
            if prevc:
                encoded_text = __rle_util_encoder(encoded_text, prevc, count)

            count = 1
            prevc = ch
        else:
            count += 1

    return __rle_util_encoder(encoded_text, prevc, count)

def decode(xs):
    ns = ""

    for i in range(len(xs)):
        if not xs[i].isdigit():
            ns += xs[i]
        else:
            ns += int(xs[i]) * xs[i+1]
            ns = ns[:-1]

    return ns
