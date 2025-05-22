# Queue predefined songs


classic_dict = {
    "spotify:track:574y1r7o2tRA009FW0LE7v": ["spotify:track:2ctvdKmETyOzPb2GiJJT53"], # [Pink Floyd] Speak To Me / Breathe (In the Air),
    "spotify:track:05uGBKRCuePsf43Hfm0JwX": ["spotify:track:1tDWVeCR9oWGX8d5J9rswk"], # [Pink Floyd] Brain Damage / Eclipse
    "spotify:track:7K6xMPtAjTuLPNlJMLf5bS": ["spotify:track:2O3l4X1yTua8oMMCtazkyo", "spotify:track:4gMgiXfqyzZLMhsksGmbQV"], # [Pink Floyd] Brick 1 / Happiest Days / Brick 2
    "spotify:track:5yMyLZu4wPvWcbLFiRhYVM": ["spotify:track:3xGJuHvSxFJxxYlHj5BIoT"], # [Pink Floyd] Empty Spaces / Young Lust
    "spotify:track:54flyrjcdnQdco7300avMJ": ["spotify:track:7ccI9cStQbQdystvc6TvxD"], # [Queen] We Will Rock You / We Are The Champions
    "spotify:track:3buvRn4CDX86EO9LHTITGn": ["spotify:track:49C6EGQhCUSgyADHYvJ7ez"], # [Led Zeppelin] Heartbreaker / Living Loving Maid
    "spotify:track:3LRJbFT9rKoKv4aW7PuBJC": ["spotify:track:5kr3j5Clb9rjEposoMyLVt"], # [Green Day] Longview / Welcome To Paradise
    "spotify:track:1nLnpLXvl68RZCSjfkyiaa": ["spotify:track:6uWp8yAt8dN5ZaT7REJ6RV"], # [Green Day] Brain Stew / Jaded
    "spotify:track:6s2yqZbiPNPL1B2IeCMsUA": ["spotify:track:0uukw2CgEIApv4IWAjXrBC"], # [My Chemical Romance] The End. / Dead!
    "spotify:track:1jOLTO379yIu9aMnCkpMQl": ["spotify:track:4nwKdZID1ht0lDBJ5h2p87", "spotify:track:4JOyMhad5dD81uGYLGgKrS", "spotify:track:1FTCA6wQwulQFokDddKE68", "spotify:track:2jtUGFsqanQ82zqDlhiKIp", "spotify:track:01SfTM5nfCou5gQL70r6gs", "spotify:track:5eZrW59C3UgBhkqNlowEID", "spotify:track:5aHHf6jrqDRb1fcBmue2kn", "spotify:track:6UCFZ9ZOFRxK8oak7MdPZu"], # [The Beatles] Abbey Road Medley
    "spotify:track:4fUKE8EULjQdHF4zb0M8FO": ["spotify:track:2RnPATK99oGOZygnD2GTO6"], # [The Beatles] Sgt. Pepper's Lonely Hearts Club Band / With A Little Help From My Friends
    "spotify:track:2tAeN2TKlQLOoSPXtARzBV": ["spotify:track:0upLyFR8Rr52ZpMp5esQoq"], # [Van Halen] Eruption / You Really Got Me
    "spotify:track:3byoK5Yi2YT9Gcc4xS8qKE": ["spotify:track:17qrNfLq2XLWTlXO7jn4p7"] # [The Warning] Dust to Dust / Dull Knives (Cut Better)
}


# Queue predefined songs
#
# PARAMETERS
# sp: spotify interface
# track: track uri to search for in the dictionary
#
# Queues corresponding songs if currently playing a queue header
# Queues noting otherwise
#
def auto_queue(sp, track):
    if(track == None):
        return
    to_queue = classic_dict.get(track)
    if(to_queue == None):
        return
    for i in to_queue:
        sp.add_to_queue(i)
    return