def main():
    a = 5
    b = 3
    c = a/b
    print('a and b are {} and {}'.format(a,b))
    print('a divided by b is {}'.format(c))
    c = round(a/b, 2)
    print('a divided by b but rounded to two places is {}'.format(c))
    c = a//b
    print('a divided by b using integer division is {}'.format(c))
    c = a%b
    print('a modulus b is {}'.format(c))

if __name__ == "__main__": main()
