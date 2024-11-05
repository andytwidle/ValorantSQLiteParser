import sqlite3
import valschema

def get_match_info():
    return get_data('SELECT * FROM match_info', valschema.Match_info)

def get_player_info():
    return get_data('SELECT * FROM match_player', valschema.Match_player)

def get_round_info():
    return get_data('SELECT * FROM match_round where matchId in (select matchId from match_info where isRanked = 1) ', valschema.Match_round)

def get_data(query, schema):
    
    conn = sqlite3.connect('f:\\valorant.db')
    #conn = sqlite3.connect("C:\\Users\\andro\\OneDrive - Queensland University of Technology\\valorant.db")
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute(query)
    rows = c.fetchall()
    conn.close()
    return [schema.from_row(row) for row in rows]

def get_puuids() -> set[str]:
    guids :set[str] = set()  # Using a set to store unique GUIDs
    try:
        #C:\develop\uni\IFN704-val
        with open('valorant_puuids.txt', 'r') as file:
        #with open('f:\\valorant_puuids.txt', 'r') as file:
            for line in file:
                # Strip any leading/trailing whitespace and add the GUID to the set
                guid = line.strip()
                if guid:
                    guids.add(guid)
    except IOError as e:
        print(f"Error reading file: {e}")
    
    return guids