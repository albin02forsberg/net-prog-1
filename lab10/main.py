import re


def main():
    mtxt = "jox r.nohre@jth.hj.se, bjox@se, adam@example.com, jox@jox@jox.com"

    print(find_email1(mtxt))
    simpsons()


def find_email1(emails):
    email_regex = r"(?:^|\s)([\w.]+?@[\w\.]+\.[\w]+[\w])"

    return re.findall(email_regex, emails)


def open_file(name):
    try:
        with open(name, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("File not found")
        return None


def simpsons():
    file = open_file("tabla.html")
    if file is None:
        return

    # Get the table rows with all the data
    reg = '<tr class="svtTabla[\w\W]+?">[\w\W]+?<h4[\w\W]+?>[\w\W]+?<\/tr>'

    for match in re.findall(reg, file):
        # Remove unnecessary whitespace
        match = re.sub(r"\s+", " ", match)

        if "Simpsons" not in match:
            continue

        print("-" * 50)

        time = re.findall(r'<td class="svtTablaTime"> ([\d]+.[\d]+)', match)
        season = re.findall(r'Säsong ([\d]+)', match)
        part = re.findall(r'Del ([\d]+) av ([\d]+)', match)
        description = re.findall(r'Del [\d]+ av [\d]+. ([\w\W]+?)<', match)
        print("Tid:\t{}".format(time[0]))
        print("Säsong:\t{}".format(season[0]))
        print("Del:\t{}/{}".format(part[0][0], part[0][1]))
        print("Handling: {}".format(description[0]))
        print("\n")



if __name__ == "__main__":
    main()
