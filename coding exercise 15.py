albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

# We want: the title of the song 'The Way I Choose' from the "Bad Company" album
# The Way I Choose
print(albums[1][3][5][1])
print('-' * 80)
# The year that the album 'Nightflight' was released
# 1981
print(albums[2][2])
print('-' * 80)
# The track number of the song 'Kentish Town Waltz' from the Imelda May album 'More Mayhem'
# 4
print(albums[3][3][3][0])
print('-' * 80)
# The tuple representing the song 'Keeping a Rendezvous' from the Bungie album 'Nightflight'
# (2, 'Keeping a Rendezvous')
print(albums[2][3][1])

