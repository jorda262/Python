def main():
        a = ('one','two','three','four')
        b = [3.3,1.1,2.2]
        c = {3333333: 'Carol Carolson', 2222222: 'Bill Billson', 1111111: 'Ann Annson'}
        print('First a tuple!')
        print(type(a),a)
        print('tuple sorted: {}\n'.format(sorted(a)))
    
        print('Next a list.')
        print(type(b),b)
        b.insert(0,0.0)
        b.append(4.4)
        print('list with two new values inserted! {}'.format(b))
        print('list sorted: {}\n'.format(sorted(b)))

        print('And last but not least, a dictionary!')
        print(type(c),c)
        print('dictionary sorted:')
        for k in sorted(c.keys()):
            print('{} {}'.format(k, c[k]))

if __name__ == "__main__": main()
    
