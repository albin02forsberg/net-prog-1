import sqlite3


def main():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    file = getFile("score2.txt")

    create_players_table(cursor)
    create_scores_table(cursor)

    populate_players_table(conn, cursor, file)
    populate_scores_table(conn, cursor, file)

    inputQuestion = """"
    What would you like to do?
    (1) Print top 10
    (2) Print hardest questions
    (3) Print all players
    (4) Print questions
    """

    choice = input(inputQuestion)

    while choice in ["1", "2", "3", "4"]:
        if choice == "1":
            print_top_10(cursor)
        elif choice == "2":
            print_hardest_questions(cursor)
        elif choice == "3":
            print_players(cursor)
        elif choice == "4":
            print_all_questions(cursor)
        choice = input(inputQuestion)


def populate_scores_table(conn, cursor, file):
    for line in file.splitlines():
        upg, upgNum, firstName, lastName, score = line.split()
        # Get the playerId from the players table
        cursor.execute("""
            SELECT playerId FROM players
            WHERE firstName = ? AND lastName = ?
        """, (firstName, lastName))
        playerId = cursor.fetchone()[0]
        cursor.execute("""
            INSERT OR IGNORE INTO scores (upgNum, playerId, score)
            VALUES (?, ?, ?)
        """, (upgNum, playerId, score))
        conn.commit()


def populate_players_table(conn, cursor, file):
    for line in file.splitlines():
        upg, upgNum, firstName, lastName, score = line.split()
        cursor.execute("""
            INSERT OR IGNORE INTO players (firstName, lastName)
            VALUES (?, ?)
        """, (firstName, lastName))
        conn.commit()


def create_players_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS players (
            playerId INTEGER PRIMARY KEY AUTOINCREMENT,
            firstName TEXT NOT NULL,
            lastName TEXT NOT NULL,
            UNIQUE (firstName, lastName)
        )
    """)


def create_scores_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            upgNum INTEGER NOT NULL,
            playerId INTEGER NOT NULL,
            score INTEGER NOT NULL,
            FOREIGN KEY (playerId) REFERENCES players (playerId)
            UNIQUE (upgNum, playerId)
            )
            """)


def print_top_10(cursor):
    cursor.execute("""
        SELECT firstName, lastName, SUM(score) AS totalScore
        FROM players
        JOIN scores ON players.playerId = scores.playerId
        GROUP BY firstName, lastName
        ORDER BY totalScore DESC
        LIMIT 10
    """)
    for row in cursor.fetchall():
        print("{} {} got {} total points".format(row[0], row[1], row[2]))


def print_players(cursor):
    cursor.execute("""
        SELECT firstName, lastName
        FROM players
    """)
    for row in cursor.fetchall():
        print("{} {}".format(row[0], row[1]))


def print_hardest_questions(cursor):
    cursor.execute("""
        SELECT upgNum, SUM(score) AS totalScore
        FROM scores
        GROUP BY upgNum
        ORDER BY totalScore ASC
        LIMIT 10
    """)
    for row in cursor.fetchall():
        # print the question number
        print("Question: {} got {} total points".format(row[0], row[1]))


def print_all_questions(cursor):
    cursor.execute("""
        SELECT * FROM scores
    """)
    for row in cursor.fetchall():
        print(row)


def getFile(filename):
    f = open(filename, "r")
    file = f.read()
    f.close()
    return file


def open_file(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()


if __name__ == '__main__':
    main()
