def count(lst, elem):
    counter = 0

    for xelem in lst:
        if xelem == elem:
            counter += 1

    return counter

things = [ 'd','i','o','m','a','i','a','l','e' ]

print(count(things, 'i'))
