def decode(data, code):
    horizontal_menu = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    table = [
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'BCDEFGHIJKLMNOPQRSTUVWXYZA', 'CDEFGHIJKLMNOPQRSTUVWXYZAB',
        'DEFGHIJKLMNOPQRSTUVWXYZABC', 'EFGHIJKLMNOPQRSTUVWXYZABCD', 'FGHIJKLMNOPQRSTUVWXYZABCDE',
        'GHIJKLMNOPQRSTUVWXYZABCDEF', 'HIJKLMNOPQRSTUVWXYZABCDEFG', 'IJKLMNOPQRSTUVWXYZABCDEFGH',
        'JKLMNOPQRSTUVWXYZABCDEFGHI', 'KLMNOPQRSTUVWXYZABCDEFGHIJ', 'LMNOPQRSTUVWXYZABCDEFGHIJK',
        'MNOPQRSTUVWXYZABCDEFGHIJKL', 'NOPQRSTUVWXYZABCDEFGHIJKLM', 'OPQRSTUVWXYZABCDEFGHIJKLMN',
        'PQRSTUVWXYZABCDEFGHIJKLMNO', 'QRSTUVWXYZABCDEFGHIJKLMNOP', 'RSTUVWXYZABCDEFGHIJKLMNOPQ',
        'STUVWXYZABCDEFGHIJKLMNOPQR', 'TUVWXYZABCDEFGHIJKLMNOPQRS', 'UVWXYZABCDEFGHIJKLMNOPQRST',
        'VWXYZABCDEFGHIJKLMNOPQRSTU', 'WXYZABCDEFGHIJKLMNOPQRSTUV', 'XYZABCDEFGHIJKLMNOPQRSTUVW',
        'YZABCDEFGHIJKLMNOPQRSTUVWX', 'ZABCDEFGHIJKLMNOPQRSTUVWXY'
    ]

    build_code = ''
    code_size = len(code)
    i = 0
    for character in data:
        if character == ' ':
            build_code += ' '
            continue
        if i == code_size:
            i = 0

        build_code += code[i]
        i += 1

    output = ''
    i = 0
    while i < len(data):
        if data[i] == ' ':
            output += ' '
            i += 1
            continue

        idx_horizontal = horizontal_menu.index(build_code[i])
        j = 0
        while j < len(table):
            if table[j][idx_horizontal] == data[i]:
                output += table[j][0]
                break
            j += 1

        i += 1

    return output