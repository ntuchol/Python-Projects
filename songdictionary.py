songs = {
    "Shape of You": 4.5,
    "Blinding Lights": 4.8,
    "Bohemian Rhapsody": 5.0,
    "Rolling in the Deep": 4.7
}

def display_songs():
    if not songs:
        print("No songs in the collection.")
    else:
        print("\nSongs and Ratings:")
        for song, rating in songs.items():
            print(f"{song}: {rating}/5")

def add_song(song_name, rating):
    if song_name in songs:
        print(f"'{song_name}' already exists in the collection.")
    else:
        songs[song_name] = rating
        print(f"Added '{song_name}' with a rating of {rating}/5.")

def update_rating(song_name, new_rating):
    if song_name in songs:
        songs[song_name] = new_rating
        print(f"Updated '{song_name}' to a new rating of {new_rating}/5.")
    else:
        print(f"'{song_name}' not found in the collection.")

def delete_song(song_name):
    if song_name in songs:
        del songs[song_name]
        print(f"Deleted '{song_name}' from the collection.")
    else:
        print(f"'{song_name}' not found in the collection.")

while True:
    print("\nMenu:")
    print("1. Display Songs")
    print("2. Add Song")
    print("3. Update Rating")
    print("4. Delete Song")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        display_songs()
    elif choice == "2":
        song_name = input("Enter the song name: ")
        try:
            rating = float(input("Enter the rating (0-5): "))
            if 0 <= rating <= 5:
                add_song(song_name, rating)
            else:
                print("Rating must be between 0 and 5.")
        except ValueError:
            print("Invalid rating. Please enter a number.")
    elif choice == "3":
        song_name = input("Enter the song name: ")
        try:
            new_rating = float(input("Enter the new rating (0-5): "))
            if 0 <= new_rating <= 5:
                update_rating(song_name, new_rating)
            else:
                print("Rating must be between 0 and 5.")
        except ValueError:
            print("Invalid rating. Please enter a number.")
    elif choice == "4":
        song_name = input("Enter the song name: ")
        delete_song(song_name)
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
