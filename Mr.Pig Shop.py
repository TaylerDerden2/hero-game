import sqlite3

def create_shop():
    db = sqlite3.connect("Shop_DB.db")
    agent_tosya = db.cursor()

    agent_tosya.execute('''CREATE TABLE IF NOT EXISTS item_types(
                        id TEXT PRIMARY KEY,
                        name Text)''')
    agent_tosya.execute("INSERT INTO item_types VALUES ('it1','units')")
    agent_tosya.execute("INSERT INTO item_types VALUES ('it2','armor')")
    agent_tosya.execute("INSERT INTO item_types VALUES ('it3','weapons')")
    agent_tosya.execute("INSERT INTO item_types VALUES ('it4','abilities')")

    agent_tosya.execute('''CREATE TABLE IF NOT EXISTS units(
                        id TEXT PRIMARY KEY,
                        item_type TEXT,
                        name TEXT,
                        price INTEGER
                        )''')
    agent_tosya.execute("INSERT INTO units VALUES('u1', 'it1', 'Knight', 300)")
    agent_tosya.execute("INSERT INTO units VALUES('u2', 'it1', 'Healer', 300)")
    agent_tosya.execute("INSERT INTO units VALUES('u3', 'it1', 'Catapult', 300)")
    agent_tosya.execute("INSERT INTO units VALUES('u4', 'it1', 'Defender', 300)")
    agent_tosya.execute("INSERT INTO units VALUES('u5', 'it1', 'Wizard', 300)")
    agent_tosya.execute("INSERT INTO units VALUES('u6', 'it1', 'Archer', 300)")

    agent_tosya.execute('''CREATE TABLE IF NOT EXISTS armor(
                        id TEXT PRIMARY KEY,
                        item_type TEXT,
                        name TEXT,
                        usable_for_unit,
                        price INTEGER,
                        value INTENGER)
                        ''')

    agent_tosya.execute("INSERT INTO armor VALUES ('ar1', 'it2', 'wooden helmet', 'ALL', 100, 400)")
    agent_tosya.execute("INSERT INTO armor VALUES ('ar2', 'it2', 'iron helmet', 'ALL', 200, 600)")
    agent_tosya.execute("INSERT INTO armor VALUES ('ar3', 'it2', 'golden helmet', 'ALL', 300, 800)")
    agent_tosya.execute("INSERT INTO armor VALUES ('ar4', 'it2', 'sparta helmet', 'ALL', 400,900)")


    agent_tosya.execute("INSERT INTO armor VALUES ('ar5', 'it2', 'leather bodyarmor', 'ALL', 100, 400)")
    agent_tosya.execute("INSERT INTO armor VALUES ('ar6', 'it2', 'iron bodyarmor', 'ALL', 200, 600)")
    agent_tosya.execute("INSERT INTO armor VALUES ('ar7', 'it2', 'golden bodyarmor', 'ALL', 300, 800)")
    agent_tosya.execute("INSERT INTO armor VALUES ('ar8', 'it2', 'sparta bodyarmor', 'ALL', 400,900)")

    agent_tosya.execute("INSERT INTO armor VALUES ('ar9', 'it2', 'cowboy boots', 'ALL', 100, 400)")
    agent_tosya.execute("INSERT INTO armor VALUES ('ar10', 'it2', 'iron boots', 'ALL', 200, 600)")
    agent_tosya.execute("INSERT INTO armor VALUES ('ar11', 'it2', 'golden boots', 'ALL', 300, 800)")
    agent_tosya.execute("INSERT INTO armor VALUES ('ar12', 'it2', 'sparta boots', 'ALL', 400,900)")

    agent_tosya.execute("INSERT INTO armor VALUES ('ar13', 'it2', 'leather shield', 'ALL', 100, 400)")
    agent_tosya.execute("INSERT INTO armor VALUES ('ar14', 'it2', 'iron shield', 'ALL', 200, 600)")
    agent_tosya.execute("INSERT INTO armor VALUES ('ar15', 'it2', 'golden shield', 'ALL', 300, 800)")
    agent_tosya.execute("INSERT INTO armor VALUES ('ar16', 'it2', 'sparta shield', 'ALL', 400,900)")

    agent_tosya.execute('''CREATE TABLE IF NOT EXISTS weapons(
                        id TEXT PRIMARY KEY,
                        item_type TEXT,
                        name TEXT,
                        usable_for_unit,
                        price INTEGER,
                        value INTENGER)
                        ''')

    agent_tosya.execute("INSERT INTO weapons VALUES ('wp1', 'it3', 'wooden sword', 'u1', 100,800)")
    agent_tosya.execute("INSERT INTO weapons VALUES ('wp2', 'it3', 'iron sword', 'u1', 200,1000)")
    agent_tosya.execute("INSERT INTO weapons VALUES ('wp3', 'it3', 'gold sword', 'u1', 300,1200)")

    agent_tosya.execute("INSERT INTO weapons VALUES ('wp4', 'it3', 'wooden knife', 'u2', 100,800)")
    agent_tosya.execute("INSERT INTO weapons VALUES ('wp5', 'it3', 'iron knife', 'u2', 200,1000)")
    agent_tosya.execute("INSERT INTO weapons VALUES ('wp6', 'it3', 'gold knife', 'u2', 300,1200)")

    agent_tosya.execute("INSERT INTO weapons VALUES ('wp7', 'it3', 'stone projectiles', 'u3', 100,800)")
    agent_tosya.execute("INSERT INTO weapons VALUES ('wp8', 'it3', 'iron projectiles', 'u3', 200,1000)")
    agent_tosya.execute("INSERT INTO weapons VALUES ('wp9', 'it3', 'explosives projectiles', 'u3', 300,1200)")

    agent_tosya.execute("INSERT INTO weapons VALUES ('wp10', 'it3', 'wooden morgenster', 'u4', 100,800)")
    agent_tosya.execute("INSERT INTO weapons VALUES ('wp11', 'it3', 'iron morgenster', 'u4', 200,1000)")
    agent_tosya.execute("INSERT INTO weapons VALUES ('wp12', 'it3', 'magician morgenster', 'u4', 300,1200)")

    agent_tosya.execute("INSERT INTO weapons VALUES ('wp13', 'it3', 'wooden baculus', 'u5', 100,800)")
    agent_tosya.execute("INSERT INTO weapons VALUES ('wp14', 'it3', 'iron baculus', 'u5', 200,1000)")
    agent_tosya.execute("INSERT INTO weapons VALUES ('wp15', 'it3', 'magician baculus', 'u5', 300,1200)")

    agent_tosya.execute("INSERT INTO weapons VALUES ('wp16', 'it3', 'wooden arows', 'u6', 100,800)")
    agent_tosya.execute("INSERT INTO weapons VALUES ('wp17', 'it3', 'iron arows', 'u6', 200,1000)")
    agent_tosya.execute("INSERT INTO weapons VALUES ('wp18', 'it3', 'magician arows', 'u6', 300,1200)")

    agent_tosya.execute('''CREATE TABLE IF NOT EXISTS abilities(
                        id TEXT PRIMARY KEY,
                        item_type TEXT,
                        name TEXT,
                        usable_for_unit,
                        price INTEGER,
                        value INTENGER)
                        ''')
    agent_tosya.execute("INSERT INTO abilities VALUES ('abc1', 'it4', 'training splash lvl 1', 'u1', 0.6,800)")
    agent_tosya.execute("INSERT INTO abilities VALUES ('abc2', 'it4', 'training splash lvl 2', 'u1', 0.7,1200)")
    agent_tosya.execute("INSERT INTO abilities VALUES ('abc3', 'it4', 'training splash lvl 3', 'u1', 0.8,1600)")

    agent_tosya.execute("INSERT INTO abilities VALUES ('abc4', 'it4', 'training heal lvl 1', 'u2', 0.3,800)")
    agent_tosya.execute("INSERT INTO abilities VALUES ('abc5', 'it4', 'training heal lvl 2', 'u2', 0.4,1200)")
    agent_tosya.execute("INSERT INTO abilities VALUES ('abc6', 'it4', 'training heal lvl 3', 'u2', 0.5,1600)")

    agent_tosya.execute("INSERT INTO abilities VALUES ('abc7', 'it4', 'training catapult lvl 1', 'u3', 2.2,800)")
    agent_tosya.execute("INSERT INTO abilities VALUES ('abc8', 'it4', 'training catapult lvl 2', 'u3', 2.3,1200)")
    agent_tosya.execute("INSERT INTO abilities VALUES ('abc9', 'it4', 'training catapult lvl 3', 'u3', 2.4,1600)")

    agent_tosya.execute("INSERT INTO abilities VALUES ('abc10', 'it4', 'defender splash lvl 1', 'u4', 0.6,800)")
    agent_tosya.execute("INSERT INTO abilities VALUES ('abc11', 'it4', 'defender splash lvl 2', 'u4', 0.7,1200)")
    agent_tosya.execute("INSERT INTO abilities VALUES ('abc12', 'it4', 'defender splash lvl 3', 'u4', 0.8,1600)")

    agent_tosya.execute("INSERT INTO abilities VALUES ('abc13', 'it4', 'archer training lvl 1', 'u6', 60,800)")
    agent_tosya.execute("INSERT INTO abilities VALUES ('abc14', 'it4', 'archer training lvl 2', 'u6', 70,1200)")
    agent_tosya.execute("INSERT INTO abilities VALUES ('abc15', 'it4', 'archer training lvl 3', 'u6', 80,1600)")

    db.commit()
    db.close()

create_shop()