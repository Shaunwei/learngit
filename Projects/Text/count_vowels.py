'''
**Count Vowels** - Enter a string and the program counts the number
of vowels in the text. For added complexity have it report a sum
of each vowel found.
'''

def count_vowels(string):
    vowels = 'aeiouy'
    total  = 0
    stats  = {}

    for character in string:
        if character not in vowels: continue
        if character not in stats:  stats[character] = 0

        stats[character] += 1
        total            += 1

    return (total, stats)

if __name__ == '__main__':
    while True:
        string = input('Enter a string: ')
        vowels = count_vowels(string)
        print( 'There are %d vowels' % vowels[0] )
        print( vowels[1] )
