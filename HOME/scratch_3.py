import sqlite3

#wyświetl menu
def instructions():
    print(
        "\n"
        "Wybierz akcję jaką chcesz wykonać \n"
        "1 >> dodawanie nowych relacji (syn-ojciec-dziadek) \n"
        "2 >> pokaż całą tabelę \n"
        "3 >> wyszukaj wg kolumny'syn' \n"
        "4 >> wyszukaj wg kolumny 'ojciec'\n"
        "5 >> wyszukaj wg kolumny 'dziadek'\n"
        "6 >> usuń wybrane rekordy'\n"
        "Q >> Zakończ zabawę'\n"
    )

#utwórz tabelę 'rodzina' z kolumnami - syn,ojciec,dziadek
def new_table():

    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    # Create table
    c.execute('''CREATE TABLE rodzina
        (syn text, ojciec text, dziadek text)''')
    # Save (commit) the changes
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()
    # Save (commit) the changes

#dodaj nowy rekord do tabeli
def insert_val(syn,ojciec,dziadek):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    ins_val=[syn,ojciec,dziadek]
    # Insert a row of data
    c.execute("INSERT INTO rodzina VALUES (?,?,?)", ins_val)

    #Save (commit) the changes
    conn.commit()

    #Save (commit) the changes
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()

#wyszukaj wg imienia syna
def select_syn(syn):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    for row in c.execute("SELECT * FROM rodzina WHERE syn LIKE ? ORDER BY ?", ('%'+syn+'%',syn)):
        print(row)
    conn.close()

#wyszukaj wg imienia ojca
def select_ojciec(ojciec):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    for row in c.execute("SELECT * FROM rodzina WHERE ojciec='%s' ORDER BY syn" % ojciec):
        print(row)
    conn.close()

#wyszukaj wg imienia dziadka
def select_dziadek(dziadek):
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        for row in c.execute("SELECT * FROM rodzina WHERE dziadek='%s' ORDER BY syn" % dziadek):
            print(row)
        conn.close()

#wybierz wszystkie rekordy
def select_all():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    for row in c.execute("SELECT * FROM rodzina ORDER BY syn"):
        print(row)
    conn.close()

#usuń rekord z tabeli (wg syn)
def delete_row(syn):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    print("Usuwane rekordy: \n")
    for row in c.execute("SELECT * FROM rodzina WHERE syn LIKE ? ORDER BY ?", ('%' + syn + '%', syn)):
        print(row)
    qdel = input("\n Czy chcesz usunąć powyższe rekordy (T/N)? \n")
    if qdel.upper() == "T":
        c.execute("DELETE FROM rodzina WHERE syn LIKE ?", ('%' + syn + '%',))
    conn.commit()
    conn.close()


#new_table()

instructions()

while  True:
    opt = input("\n Wybierz opcję: ")

    if opt == "1":
        syn = input("Podaj imię syna: ")
        ojciec = input("Podaj imię ojca: ")
        dziadek = input("Podaj imię dziadka: ")
        insert_val(syn,ojciec,dziadek)

    if opt == "2":
        select_all()

    if opt == "3":
        syn = input("Podaj imię syna: ")
        select_syn(syn)

    if opt == "4":
        ojciec = input("Podaj imię ojca: ")
        select_ojciec(ojciec)

    if opt == "5":
        dziadek = input("Podaj imię dziadka: ")
        select_dziadek(dziadek)

    if opt == "6":
        syn = input("Podaj imię syna (dla rekordów, które chcesz usunąć): ")
        delete_row(syn)

    if opt == "Q":
        break