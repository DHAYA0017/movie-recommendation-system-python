import random

movies_by_genre = {
    "Action": [
        "Gladiator", "Die Hard", "Rambo", "Rocky",
        "Predator", "Terminator", "Skyfall", "Troy",
        "Logan", "Deadpool", "Jaws", "Heat",
        "Scarface", "Commando", "Speed", "Twister",
        "Braveheart", "Casino Royale", "The Raid",
        "Taken", "Shooter", "Fury", "Sicario",
        "Extraction", "Crank", "Point Break",
        "Olympus Has Fallen", "The Transporter",
        "Unstoppable", "Con Air"
    ],

    "Comedy": [
        "Superbad", "The Mask", "Home Alone", "Jumanji",
        "Ted", "Click", "Norbit", "Zoolander",
        "Eurotrip", "Scary Movie", "Johnny English",
        "Grown Ups", "Big Daddy", "Rush Hour",
        "Dumb and Dumber", "Ace Ventura", "Yes Man",
        "Bridesmaids", "Neighbors", "Paul",
        "Zombieland", "Central Intelligence",
        "We're the Millers", "The Dictator",
        "Step Brothers", "Mean Girls",
        "Anchorman", "Hot Fuzz",
        "Mr Bean", "The Internship"
    ],

    "Drama": [
        "Forrest Gump", "Titanic", "Whiplash",
        "Joker", "Parasite", "Moonlight",
        "Cast Away", "Argo", "Glory",
        "Amadeus", "Rain Man", "The Pianist",
        "Life of Pi", "Slumdog Millionaire",
        "The Revenant", "A Beautiful Mind",
        "Million Dollar Baby", "Birdman",
        "Manchester by the Sea", "The Help",
        "Room", "Selma", "Capote",
        "Spotlight", "Fences", "Lincoln",
        "The Post", "Crash",
        "Mystic River", "Her"
    ],

    "Scifi": [
        "Interstellar", "Inception", "Avatar",
        "Dune", "Gravity", "Arrival",
        "Alien", "Aliens", "Looper",
        "Moon", "Oblivion", "Elysium",
        "District 9", "Ex Machina",
        "Sunshine", "Annihilation",
        "Prometheus", "Passengers",
        "Predestination", "Contact",
        "Minority Report", "I Robot",
        "War of the Worlds", "The Martian",
        "Edge of Tomorrow", "Upgrade",
        "Tenet", "After Earth",
        "Tron", "Gattaca"
    ],

    "Horror": [
        "Insidious", "Sinister", "Hereditary",
        "Halloween", "Saw", "Hostel",
        "Smile", "Get Out", "Us",
        "The Ring", "The Grudge", "Poltergeist",
        "The Exorcist", "Annabelle",
        "The Omen", "The Babadook",
        "The Witch", "The Others",
        "The Conjuring", "It",
        "Scream", "Carrie",
        "Evil Dead", "Orphan",
        "Lights Out", "Drag Me to Hell",
        "Paranormal Activity", "The Nun",
        "Doctor Sleep", "Creep"
    ]
}

def show_genres():
    print("\nAvailable Genres:")
    for genre in movies_by_genre:
        print("-", genre)

#recommedations

def get_recommendations():
    show_genres()
    genre = input("\nEnter genre: ").strip()

    if genre not in movies_by_genre:
        print("❌ Genre not found")
        return


    count = int(input("How many recommendations do you want? "))
    if count <= 0:
          print("❌ Enter number greater than 0")

    movie_list = movies_by_genre[genre]
    count = min(count, len(movie_list))

    picks = random.sample(movie_list, count)

    print(f"\n🎬 {genre} Movie Recommendations:")
    for i, movie in enumerate(picks, start=1):
        print(f"{i}. {movie}")

#add new movies

def add_new_movie():
    show_genres()
    genre = input("\nEnter genre: ").strip()

    if genre not in movies_by_genre:
        movies_by_genre[genre] = []

    title = input("Enter movie name: ").strip()

    if title.lower() in [m.lower() for m in movies_by_genre[genre]]:
        print("⚠️ Movie already exists")
        return

    movies_by_genre[genre].append(title)
    print("✅ Movie added")

#search movie

def search_movie():
    keyword = input("\nEnter movie name (full or part): ").strip().lower()
    found = False

    for genre, movie_list in movies_by_genre.items():
        for movie in movie_list:
            if keyword in movie.lower():
                print(f"- {movie} ({genre})")
                found = True

    if not found:
        print("❌ Movie not found")

#main manu

def main_menu():
    while True:
        print("\n==============================")
        print("🎥 Movie Recommendation System")
        print("==============================")
        print("1. Get Movie Recommendations")
        print("2. Add New Movie")
        print("3. Search Movie")
        print("4. Exit")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            get_recommendations()
        elif choice == "2":
            add_new_movie()
        elif choice == "3":
            search_movie()
        elif choice == "4":
            print("👋 Exiting... Thank you!")
            break
        else:
            print("❌ Invalid choice")

main_menu()
