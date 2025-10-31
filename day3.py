# 🎬 Movie Recommendation Console App
# Author: Ashutosh Kumar Singh

# Movie database (you can expand this anytime)
movies = [
    {"title": "Inception", "genre": "Sci-Fi", "rating": 8.8},
    {"title": "The Dark Knight", "genre": "Action", "rating": 9.0},
    {"title": "Interstellar", "genre": "Sci-Fi", "rating": 8.6},
    {"title": "The Shawshank Redemption", "genre": "Drama", "rating": 9.3},
    {"title": "The Godfather", "genre": "Crime", "rating": 9.2},
    {"title": "Spider-Man: No Way Home", "genre": "Action", "rating": 8.3},
    {"title": "Inside Out", "genre": "Animation", "rating": 8.1},
    {"title": "Coco", "genre": "Animation", "rating": 8.4},
    {"title": "Titanic", "genre": "Romance", "rating": 7.8},
    {"title": "La La Land", "genre": "Romance", "rating": 8.0}
]

print("🎥 Welcome to Movie Recommendation App 🎥")
print("------------------------------------------------")

while True:
    print("\nHow would you like to get recommendations?")
    print("1. By Genre")
    print("2. By Minimum Rating")
    print("3. View All Movies")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        genre = input("Enter genre (Action, Sci-Fi, Drama, Crime, Animation, Romance): ").capitalize()
        found = False
        print(f"\nMovies in {genre} genre:")
        for movie in movies:
            if movie["genre"] == genre:
                print(f"🎬 {movie['title']} ({movie['rating']}/10)")
                found = True
        if not found:
            print("No movies found in this genre.")

    elif choice == '2':
        try:
            rating = float(input("Enter minimum rating (0-10): "))
            print(f"\nMovies with rating >= {rating}:")
            found = False
            for movie in movies:
                if movie["rating"] >= rating:
                    print(f"⭐ {movie['title']} - {movie['genre']} ({movie['rating']}/10)")
                    found = True
            if not found:
                print("No movies found above this rating.")
        except ValueError:
            print("Please enter a valid number!")

    elif choice == '3':
        print("\nAll Available Movies:")
        for movie in movies:
            print(f"{movie['title']} - {movie['genre']} ({movie['rating']}/10)")

    elif choice == '4':
        print("Thank you for using the Movie Recommendation App! 🎬")
        break

    else:
        print("Invalid choice. Please try again.")
