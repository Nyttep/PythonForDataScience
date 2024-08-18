from ft_filter import ft_filter
import sys

def tst(item) -> bool:
    if (item == 'a'):
        return True
    else:
        return False

def main():
    s = "abcdea"
    expected = filter(tst, s)
    mine = ft_filter(tst, s)
    print("expected :", expected)
    for item in expected:
        print(item)
    print("mine :", mine)
    for item in mine:
        print(item)

if __name__ == '__main__':
    main()