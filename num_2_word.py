ones = ('ZERO_ONES', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', )
teens = ('ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', )
tens = ('ZERO_TENS', 'TEN', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', )
hundreds = ones  # ones because hundreds use the same words with hundred prefixed
columns = [ones, tens, hundreds]

thousands = ['ZERO_THOUSANDS', 'thousand', 'million', 'billion', 'trillion']


def num_under_1000_to_word(n, hyphenate_words=True, as_list=False):
    TENS = 1
    HUNDREDS = 2
    ones_value = n % 10
    word = []  # word is constructed from left to right starting with lsd
    col_index = 0
    while n > 0:
        value = n % 10
        if col_index == TENS and value == 1:  # special case for teens
            word = [teens[ones_value]]
        elif value > 0:
            if col_index == HUNDREDS:
                if len(word) != 0:
                    word.append('and')
                word.append('hundred')
            if hyphenate_words and col_index == TENS and value > 1 and ones_value > 0:  # numbers like twenty-one
                word[-1] = '{}-{}'.format(columns[col_index][value], word[-1])
            else:
                word.append(columns[col_index][value])
        col_index += 1
        n //= 10

    word = reversed(word)
    if as_list:
        return list(word)
    else:
        return " ".join(word)


def num_2_word(n, hyphenate_words=True, as_list=False):
    word = []  # word is constructed from left to right starting with lsd
    insert_extra_and = (n > 1000 and n % 1000 < 100)  # eg 110,001 is one hundred and ten thousand AND one
    thousands_index = 0

    while n > 0:
        if thousands_index == 1 and insert_extra_and:
            word.append('and')

        three_lsds_as_word = num_under_1000_to_word(n % 1000, hyphenate_words=hyphenate_words, as_list=True)
        if len(three_lsds_as_word) > 0 and thousands_index > 0:
            word.append(thousands[thousands_index])

        word.extend(reversed(three_lsds_as_word))
        thousands_index += 1
        n //= 1000

    if as_list:
        return list(reversed(word))
    return " ".join(reversed(word))


if __name__ == "__main__":
    print(num_2_word(101010121))
    print(num_2_word(100000021))