import math
import random
import zlib
import collections 

def main():
    txt = read_file('exempeltext.txt')

    byteArr = bytearray(txt, 'utf-8')

    # Length of the text 

    print("Length txt: {}".format(len(txt)))
    print("Length byteArr: {}".format(len(byteArr)))

    # Entropy of the text

    histo = makeHisto(byteArr)
    prob = makeProb(histo)
    ent = entropy(prob)

    print("Entropy (source): {}".format(ent))

    # Shuffle the text

    theCopy = byteArr.copy()

    random.shuffle(theCopy)

    if not byteArr == theCopy:
        print("Shuffled")

    # Entropy of the shuffled text (zlib)

    code = zlib.compress(theCopy)
    histo = makeHisto(code)
    prob = makeProb(histo)
    ent = entropy(prob)

    print("Entropy shuffled (zlib): {}".format(ent))

    # Entropy of the unshuffled text (zlib)

    code = zlib.compress(byteArr)
    histo = makeHisto(code)
    prob = makeProb(histo)
    ent = entropy(prob)

    print("Entropy unshuffled (zlib): {}".format(ent))

    # The smalles on is the source text
    # The biggest is the shuffled text

    t1 = """
    I hope this lab never ends because it is so incredibly thrilling!"""

    code = zlib.compress(bytearray(t1, 'utf-8'))

    print("Length t1: {}".format(len(t1)))
    print("Length compress: {}".format(len(code)))

    t10 = t1 * 10

    code = zlib.compress(bytearray(t10, 'utf-8'))

    print("Length t10: {}".format(len(t10)))
    print("Length compress: {}".format(len(code)))

    # No, because t10 is just repition of t1, hence we don't need to store 
    # the same information 10 times.



def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def makeHisto(byteArr):
    histo = [0] * 256
    for byte in byteArr:
        histo[byte] += 1

    return histo

def makeProb(histo):
    # Returns a probability distribution which is normalized
    prob = [0] * 256
    for x in range(256):
        prob[x] = histo[x] / sum(histo)

    return prob

def entropy(prob):
    # Returns the entropy of a probability distribution
    ent = 0
    for x in range(256):
        if prob[x] != 0:
            ent += prob[x] * math.log(prob[x], 2)

    return -ent

if __name__ == "__main__":
    main()