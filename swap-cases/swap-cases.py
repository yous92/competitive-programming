def swap_case(s):
    swapped_string: str = ""
    for char in s:
        if char.islower():
            swapped_string += char.upper()
        else:
            swapped_string += char.lower()
    return swapped_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)