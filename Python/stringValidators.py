if __name__ == '__main__':
    s = input()
    for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
        print(any(eval(f"c.{test}()") for c in s))
