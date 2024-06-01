import csv, os

all_rows = []
names = []
count = 0

base_dir = "artist(s)"
os.makedirs(base_dir, exist_ok=True)

with open("Day-56/songs.csv", encoding="UTF-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        all_rows.append(row)
        artist_name = row["Artist(s)"].replace('/', '_')
        artist_dir = os.path.join(base_dir, artist_name)
        names.append(artist_dir)
        
        if not os.path.exists(artist_dir):
            os.mkdir(artist_dir)
        with open(os.path.join(artist_dir, "songs.txt"), 'a', encoding="UTF-8") as f:
            song_name = row["Song"]
            f.write(song_name + '\n')
        
        count += 1

print(all_rows[2])
print(names)
