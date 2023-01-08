def dec_to_snafu(dec):
    snafu = []
    while dec > 0:
        remainder = dec % 5
        dec //= 5
        # we cannot use the digits 3 and 4 in the snafu number system
        # instead, we use = and -, representing -2 and -1 respectively
        # effectively, instead of doing e.g. 3 * 5^n, we do -2 * 5^n.
        # this means that we must add 5 * 5^n to our number in the following iteration, to compensate.
        # since 5 * 5^n is the same as 5^(n+1), we can just add one to dec, which is the same as adding 5^(n+1).
        if remainder > 2:
            snafu.append("   =-"[remainder])
            dec += 1
        else:
            snafu.append(str(remainder))
    return ''.join(snafu[::-1])

def snafu_to_dec(snafu):
    total = 0
    mult = 1
    for digit in snafu[::-1]:
        if digit == '=':
            total -= 2 * mult
        elif digit == '-':
            total -= mult
        else:
            total += int(digit) * mult
        mult *= 5
    return total


if __name__ == '__main__':
    total = 0
    with open('day25/input.txt') as f:
        lines = f.read().splitlines()
        for line in lines:
            total += snafu_to_dec(line)
    print(dec_to_snafu(total))