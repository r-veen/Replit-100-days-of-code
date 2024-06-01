import csv
import os

all_rows = []
names = []
count = 0

base_dir = "artist(s)"
os.makedirs(base_dir, exist_ok=True)

with open("Day-56/songs.csv", encoding="UTF-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        all_rows.append(row)
        artist_name = row["Artist(s)"].replace('/', '_').replace('\\', '_')
        artist_dir = os.path.join(base_dir, artist_name)
        
        if not artist_name:
            print(f"[Warning] Empty artist name for row: {row}")
            continue
        
        names.append(artist_dir)
        
        if not os.path.exists(artist_dir):
            try:
                os.mkdir(artist_dir)
                print(f"[Info] Directory created: {artist_dir}")
            except Exception as e:
                print(f"[Error] Failed to create directory {artist_dir}: {e}")

        song_name = row["Song"].replace('/', '_').replace('\\', '_').replace(':', '_')
        
        if not song_name:
            print(f"[Warning] Empty song name for row: {row}")
            continue
        
        file_path = os.path.join(artist_dir, song_name + '.txt')
        
        try:
            with open(file_path, 'a', encoding="UTF-8") as f:
                f.write(song_name + '\n')
            print(f"[Info] File created: {file_path}")
        except Exception as e:
            print(f"[Error] Failed to create file {file_path}: {e}")
        
        count += 1

print("\nSummary:")
print(f"Total directories and files created: {count}")
print("Directories created:")
for name in names:
    print(f" - {name}")
