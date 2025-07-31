#%%
import sqlite3
import matplotlib.pyplot as plt

def inspect_data():
    '''
    Reads and plots the data.
    '''
    conn = sqlite3.connect("data.sqlite3", isolation_level=None)
    conn.execute("CREATE TABLE IF NOT EXISTS 'workdays' (date STR NOT NULL, hours REAL NOT NULL)")

    res = conn.execute("SELECT * FROM 'workdays'").fetchall()

    print(res)

    hours = [day[3] for day in res]

    plt.plot(hours)


if __name__ == "__main__":
    inspect_data()
# %%
