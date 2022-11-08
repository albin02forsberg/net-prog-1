def getFile(filename):
    f = open(filename, "r")
    file = f.read()
    f.close()
    return file


def main():
    file = getFile("score2.txt")
    dictionary = {}

    for line in file.splitlines():
        upg, upgNum, firstName, lastName, score = line.split()
        if firstName + " " + lastName in dictionary:
            dictionary[firstName + " " + lastName] += int(score)
        else:
            dictionary[firstName + " " + lastName] = int(score)

    for key, value in dictionary.items():
        if value == max(dictionary.values()):
            print(key, value)


if __name__ == '__main__':
    main()
