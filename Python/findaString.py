def count_substring(string, sub_string):
    count = 0
    for s in range(len(string)-len(sub_string)+1):
        new_string = ''
        for i in range(len(sub_string)):
            new_string += string[s+i]
        if new_string == sub_string:
            count += 1
        else:
            new_string = ''
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)