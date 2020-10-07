def word_count(s):
    # Your code here
    wdict = {}

    banned = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split()

    words = s.lower()

    for i in banned:
        words = words.replace(i, " ")

    for w in words.split():
        if w not in wdict:
            wdict[w] = 1
        else:
            wdict[w] += 1

    return wdict

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))