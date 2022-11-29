import re

def main():
    print("Hello World!")

    mtxt = "jox r.nohre@jth.hj.se, bjox@se, adam@example.com, jox@jox@jox.com"

    print(find_email1(mtxt))
    simpsons()



def find_email1(emails):
    email_regex = r"[\s]+[\w\.]*?@[\w]+\.[\w]+"

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

    reg = r"Simpsons[\s]*(?:<.*[\s\w]*)+.*\s"

    print(re.findall(reg, file))



if __name__ == "__main__":
    main()