import sqlite3
from sqlite3 import Error
import random


def main():
    
    database = "german.db"
    conn = create_connection(database)
    
    with conn:
        name = rules_and_name(conn)

    with conn:
        number_of_entries = get_number_of_entries(conn)

    lives = get_lives()

    score = 0
    while lives > 0:
        print(f"You have {lives} lives")
        print(f"Score: {score}")
        with conn:
            random_noun, article, english = get_random_noun(number_of_entries, conn)        
        if ask_question(random_noun, article, english) == True:
            if lives < 7:
                lives += 0.5
            elif lives < 10:
                live += 0.1
            score += 10
        else:
            lives -= 1

    with conn:
        record_score(conn, name, score)


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

        

def rules_and_name(conn):
    


    print("This program tests your knowledge of German noun genders.\n You will be given a noun the 3000 most common, and it's your job to guess the gender.\n Press 'm' for masculine, 'f' for feminine or 'n' for neuter.\n")
    while True:
        player = input('Player input name: ').lower()
        if player != '':
            break

    cur = conn.cursor()
    cur.execute("SELECT COUNT(name) FROM player_scores WHERE name = ?", [player])

    if cur.fetchone() == 1:
        return player
    else:    
        params = (player, 0)
        cur.execute("INSERT INTO player_scores(name, high_score) VALUES(?, ?)", params)
        return player



def get_number_of_entries(conn):
    """ Get the number of entries in the database
    This allows the game to dynamically adapt to changes in the database, introducing or removing words from the pool as necessary"""
    
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM nouns_de")

    return cur.fetchone()[0]


def record_score(conn, name, score):
    
    cur = conn.cursor()
    cur.execute("SELECT high_score FROM player_scores WHERE name = ?", [name])
    previous_high = cur.fetchone()[0]

    print(f"Your score: {score}")
    
    if score > previous_high:
        cur.execute("UPDATE player_scores SET high_score = ? WHERE name = ?", [score, name])
        print(f"your high score: {score}")
    
    else:
        print(f"Your high score: {previous_high}")

    cur.execute("SELECT name, MAX(high_score) FROM player_scores")
    winner, alltime_high = cur.fetchone()
    
    print(f"Highest score ever: {winner} ({alltime_high} points)")
    


def ask_question(noun, article, english):
    
    while True:
        answer = input(f"D__ {noun}: ")
        if answer in ['m', 'f', 'n']:
            break
    
    if answer == 'm':
        answer = 0
    elif answer == 'f':
        answer = 1
    elif answer == 'n':
        answer = 2
    
    derdiedas = ['Der', 'Die', 'Das']
    def_article = derdiedas[article]
    if answer == article:
        print('\n:-) Genau! Sehr gut gemacht!')
        print(f"{def_article} {noun} heißt 'The {english}' auf Englisch!\n")
        return True
    else:
        print('\n:-( Leider nicht! Viel glück beim nächsten mal')
        print(f"Die richtige Antwort ist {def_article}")
        print(f"{def_article} {noun} heißt 'The {english}' auf Englisch!\n")
        return False


def get_lives():
    """This is a placeholder for future development of a more complicated health system for the game.
    Currently a simple default of 5 lives is used."""
    return 5


def get_random_noun(number_of_entries, conn):
    
    
    noun_selection = random.randint(1, number_of_entries)
    
    cur = conn.cursor()

    cur.execute("SELECT noun, definite_article, english FROM nouns_de WHERE id=?", (noun_selection,))
    # This would probably work better as a dict of some kind?
    hold = list(cur.fetchone())

    return hold








if __name__ == '__main__':
    main()