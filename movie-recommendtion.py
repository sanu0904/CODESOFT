# Task 4 - Recommendation System
# Content based filtering using movie genres
# Idea: if A user like a movie it recommend the similar type of movie to the user.

# sample dataset of movies (made this up manually for the project)
movies = [
    {"id": 1, "title": "The Dark Knight", "type": ["Action","Crime","Drama"]},
    {"id": 2, "title": "Inception", "type": ["Action", "Sci-Fi", "Thriller"]},
    {"id": 3, "title": "Interstellar", "type": ["Sci-Fi", "Drama", "Adventure"]},
    {"id": 4, "title": "The Hangover", "type": ["Comedy"]},
    {"id": 5, "title": "Superbad", "type": ["Comedy", "Teen"]},
    {"id": 6, "title": "Titanic", "type": ["Romance", "Drama"]},
    {"id": 7, "title": "The Notebook", "type": ["Romance", "Drama"]},
    {"id": 8, "title": "John Wick", "type": ["Action", "Thriller"]},
    {"id": 9, "title": "Mad Max: Fury Road", "type": ["Action", "Adventure", "Sci-Fi"]},
    {"id": 10, "title": "Coco", "type": ["Animation", "Family", "Drama"]},
    {"id": 11, "title": "Toy Story", "type": ["Animation", "Family", "Comedy"]},
    {"id": 12, "title": "The Conjuring", "type": ["Horror", "Thriller"]},
    {"id": 13, "title": "It", "type": ["Horror", "Thriller"]},
    {"id": 14, "title": "La La Land", "type": ["Romance", "Drama", "Musical"]},
]


def get_movie_by_title(title):
    for movie in movies:
        if movie["title"].lower() == title.lower():
            return movie
    return None


# this calculates how two movies are based on common type
# simple approach -> count of overlapping genres
def genre_similarity(type1, type2):
    set1 = set(type1)
    set2 = set(type2)
    common = set1.intersection(set2)
    return len(common)


def recommend_movies(liked_title, top_n=3):
    liked_movie = get_movie_by_title(liked_title)

    if liked_movie is None:
        print(f"Sorry, '{liked_title}' not found in our database.")
        return []

    scores = []
    for movie in movies:
        if movie["id"] == liked_movie["id"]:
            continue  # don't recommend the same movie

        sim_score = type_similarity(liked_movie["type"], movie["type"])
        if sim_score > 0:
            scores.append((movie, sim_score))

    # sort by similarity score, highest first
    scores.sort(key=lambda x: x[1], reverse=True)

    return scores[:top_n]


def print_recommendations(liked_title):
    print(f"\nBecause you liked '{liked_title}', you might also like:\n")
    results = recommend_movies(liked_title)

    if not results:
        print("Couldn't find good recommendations for this movie.")
        return

    for movie, score in results:
        print(f"- {movie['title']}  (type: {', '.join(movie['genres'])}, match score: {score})")


def show_all_movies():
    print("\nAvailable movies in our database:")
    for movie in movies:
        print(f"{movie['id']}. {movie['title']} - {', '.join(movie['type'])}")


def main():
    print("=== Simple Movie Recommendation System ===")
    print("(Content-based filtering using type)")

    show_all_movies()

    while True:
        user_input = input("\nEnter a movie title you liked (or 'quit' to exit): ")

        if user_input.lower() == 'quit':
            print("Thanks for using the recommender, bye!")
            break

        print_recommendations(user_input)


if __name__ == "__main__":
    main()
