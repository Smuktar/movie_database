import json
import os

from colorama import Fore, Style, init
init(autoreset=True)

# initialize empty dictionary for storing movie data
movie_database = {}

# -------- COLOR --------
def title(text):
    print(Fore.CYAN + Style.BRIGHT + text)

def success(text):
    print(Fore.GREEN + text)

def error(text):
    print(Fore.RED + text)

def warning(text):
    print(Fore.YELLOW + text)

def highlight(text):
    print(Fore.MAGENTA + text)


# validation 
def valid_date(date_str):
    # check: YYYY-MM-DD 
    if len(date_str) != 10:
        return False
    if date_str[4] != "-" or date_str[7] != "-":        #Checks that character 5 and 8 are dashes (-)
        return False

    y = date_str[0:4]          # Where year should be located (starts at index 0 and stops before index 4)
    m = date_str[5:7]          # Where month should be located
    d = date_str[8:10]         # Where day should be located

    if not (y.isdigit() and m.isdigit() and d.isdigit()):    # Checks year/month/day are all numbers.
        return False

    return True

# Function to add a new movie to the database
def add_movie():
    title_in = input(Fore.YELLOW + "Enter the movie title: ")
    genre = input(Fore.YELLOW + "Enter the movie genre: ")
    director = input(Fore.YELLOW + "Enter the name of the director: ")
    release_date = input(Fore.YELLOW + "Enter the release date of the movie (YYYY-MM-DD): ")
    actors = input(Fore.YELLOW + "Enter the names of the actors (separated by commas + space): ")

    # validation 
    if title_in == "":
        warning("Title cannot be empty.")
        return
    if genre == "":
        warning("Genre cannot be empty.")
        return
    if director == "":
        warning("Director cannot be empty.")
        return
    if not valid_date(release_date):
        error("Invalid date format. Use YYYY-MM-DD.")
        return

    # split 
    actors_list = actors.split(", ")

    movie_database[title_in] = {
        "genre": genre,
        "director": director,
        "release_date": release_date,
        "actors": actors_list
    }

    success(f"✅ {title_in} has been added to the database.")

# Function to edit an existing movie in the database
def edit_movie():
    title_in = input(Fore.YELLOW + "Enter the movie title to edit: ")
    if title_in in movie_database:
        title(f"\nCurrent information for {title_in}:")
        print(json.dumps(movie_database[title_in], indent=4))

        print(Fore.YELLOW + "\nPress Enter to keep the current value.\n")

        # Prompt user for updated information
        genre = input(Fore.YELLOW + "Enter the movie genre (or press Enter to keep current value): ")
        director = input(Fore.YELLOW + "Enter the name of the director (or press Enter to keep current value): ")
        release_date = input(Fore.YELLOW + "Enter the release date (YYYY-MM-DD) (or press Enter to keep current value): ")
        actors = input(Fore.YELLOW + "Enter the names of the actors (comma + space) (or press Enter to keep current value): ")

        # Update the dictionary with the new information
        if genre != "":
            movie_database[title_in]["genre"] = genre
        if director != "":
            movie_database[title_in]["director"] = director
        if release_date != "":
            if valid_date(release_date):
                movie_database[title_in]["release_date"] = release_date
            else:
                warning("Invalid date format. Keeping old value.")
        if actors != "":
            movie_database[title_in]["actors"] = actors.split(", ")

        success(f"✅ {title_in} has been updated.")
    else:
        error(f"❌ {title_in} is not in the database.")

# Function to delete a movie from the database
def delete_movie():
    title_in = input(Fore.YELLOW + "Enter the movie title to delete: ")
    if title_in in movie_database:
        confirm = input(Fore.YELLOW + f"Are you sure you want to delete '{title_in}'? (y/n): ")
        if confirm.lower() == "y":
            del movie_database[title_in]
            success(f"🗑️ {title_in} has been deleted from the database.")
        else:
            warning("Delete cancelled.")
    else:
        error(f"❌ {title_in} is not in the database.")

# Function to view all movies in the database
def view_all_movies():
    if len(movie_database) == 0:
        warning("No movies in the database.")
        return

    title("\n--- All Movies in the Database ---")
    for movie, info in movie_database.items():
        highlight(f"\n🎬 {movie}")
        print(Fore.WHITE + json.dumps(info, indent=4))

# Function to search for a movie based on user-specified criteria
def search_movies():
    if len(movie_database) == 0:
        warning("No movies to search.")
        return

    title("\n--- Search Movies ---")
    criteria = input(Fore.YELLOW + "Enter the search criteria: ")

    matches = []
    for movie, info in movie_database.items():
        actor_found = False
        for a in info["actors"]:
            if criteria in a:
                actor_found = True

        if (criteria in movie or
            criteria in info["genre"] or
            criteria in info["director"] or
            actor_found):
            matches.append(movie)

    if matches:
        success("\nMatches found:")
        for match in matches:
            highlight(f"\n🔎 {match}")
            print(Fore.WHITE + json.dumps(movie_database[match], indent=4))
    else:
        warning("No matches found.")

# Function to save movie data to a file
def save_data():
    filename = input(Fore.YELLOW + "Enter the filename to save to (example: movies.json): ")
    try:
        with open(filename, "w") as file:
            json.dump(movie_database, file, indent=4)
        success("💾 Data saved successfully.")
    except:
        error("Could not save file. Try again.")

# Function to load movie data from a file
def load_data():
    filename = input(Fore.YELLOW + "Enter the filename to load from (example: movies.json): ")

    if not os.path.exists(filename):
        error("File not found.")
        return

    try:
        with open(filename, "r") as file:
            data = json.load(file)

        global movie_database
        movie_database = data
        success("📂 Data loaded successfully.")
    except:
        error("Could not load file. Make sure it is a valid JSON file.")

# Main program loop
while True:
    title("\n==== Movie Database Management System ====\n")
    print(Fore.YELLOW + "1. Add a new movie")
    print("2. Edit an existing movie")
    print("3. Delete a movie")
    print("4. View all movies")
    print("5. Search movies")
    print("6. Save data to file")
    print("7. Load data from file")
    print("8. Exit\n")

    choice = input(Fore.YELLOW + "Enter your choice: ")

    if choice == "1":
        add_movie()
    elif choice == "2":
        edit_movie()
    elif choice == "3":
        delete_movie()
    elif choice == "4":
        view_all_movies()
    elif choice == "5":
        search_movies()
    elif choice == "6":
        save_data()
    elif choice == "7":
        load_data()
    elif choice == "8":
        title("Goodbye! 👋")
        break
    else:
        error("Invalid choice. Please try again.")
