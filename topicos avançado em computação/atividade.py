def achaletra(s, l ):
    pos = 0
    for i in s:
        if l == i:
            return pos
        pos = pos + 1
    return -1
print ( achaletra("feevale", "v"))

