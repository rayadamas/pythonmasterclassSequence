albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
           ("Bad Company", "Bad Company", 1974),
            ("Nightflight", "Budgie", 1981),
             ("More Mayhem", "Emilda May", 2011),
              ("Ride the Lightning", "Metallica", 1984),
          ]

# albums is Homogeneous as it only contains a single type: tuples
# the tuples themselves are heterogeneous, as they contain two types: str & int

print(len(albums))

# Unpack method 1
for album in albums:
    name, artist, year = album
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))

print("-" * 80)

# Unpack method 2
for name, artist, album in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))