"""A text file contains some text, we need to know how often each letter appears in the text.
Such an analysis may be useful in cryptography, so we want to be able to do that in reference to the Latin alphabet.

Your task is to write a program which: asks the user for the input file's name;
reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
prints a simple histogram in alphabetical order (only non-zero counts should be presented)
Create a test file for the code, and check if your histogram contains valid results.
a -> 1
b -> 1"""

from os import strerror
my_dict = {}
try:
    stream = open("C:\\Users\\Ayantika\\Desktop\\test.txt", "rt")
    ch = stream.read(1).lower()
    while ch != '':
        if ch not in my_dict:
            my_dict[ch]=1
        else:
            my_dict[ch]=my_dict.get(ch)+1
        ch = stream.read(1).lower()
    stream.close()
    sorted_dict = dict(sorted(my_dict.items(),key=lambda item: item[1], reverse=True))
    fo = open("C:\\Users\\Ayantika\\Desktop\\testhist.txt", "wt")
    for i in sorted_dict.keys():
        print(i," -> ",sorted_dict[i])
    for key, value in sorted_dict.items():
        s=key+" -> "+str(value)+"\n"
        for alph in s:
            fo.write(alph)

except Exception as exc:
    print(strerror(exc.errno))
