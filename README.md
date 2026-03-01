<p align="Left">
    <img src="per_scholas_logo.png" width="300">
</p>

# PA - 385.2.1 - Practice Assignment - Dictionary

## Introduction
The project is a Python program for a movie database management system. The program allows users to add, edit, and view movie information such as title, genre, director, release date, and actors. It also includes a search functionality that enables users to search for a specific movie based on its title or any other criteria.

## Lab Overview
In this lab, we will demonstrate how to use different dictionary methods. After implementing this project, learners will gain an understanding of how to use Python dictionaries effectively. They will learn the following aspects of dictionary manipulation.

## Examples

### Movie Database Management System

*sample code*

```
# Define dictionary of movies and their information
movies = {
    "The Dark Knight": {
        "year": 2008,
        "genre": "Action",
        "director": "Christopher Nolan",
        "actors": ["Christian Bale", "Heath Ledger", "Aaron Eckhart"]
    },
    "Inception": {
        "year": 2010,
        "genre": "Sci-Fi",
        "director": "Christopher Nolan",
        "actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"]
    },
    "Pulp Fiction": {
        "year": 1994,
        "genre": "Crime",
        "director": "Quentin Tarantino",
        "actors": ["John Travolta", "Samuel L. Jackson", "Uma Thurman"]
    }
}

# Print out the movies and their information using square bracket syntax and .keys and .values
for movie in movies:
    print(f"Movie: {movie}")
    for key, value in movies[movie].items():
        print(f"{key}: {value}")
    print()

# Update an element in the dictionary
movies["The Dark Knight"]["year"] = 2009

# Delete an element from the dictionary
del movies["Pulp Fiction"]

# Get a value from the dictionary using .get
genre = movies.get("Inception").get("genre")
print(f"The genre of Inception is {genre}.")

```
In this game, we define a dictionary of movies and their information. Each movie is a key in the dictionary, and its value is another dictionary containing its year, genre, director, and a list of actors. We then use square bracket syntax and the .keys and .values methods to print out each movie and its information.

We then update the year of "The Dark Knight" using square bracket syntax, delete "Pulp Fiction" using the del statement, and get the genre of "Inception" using the .get method.

***But, we'll take it to one more level***

We'll ask for input from the user to create this list as well. So, below is the complete requirement

***Requirement***

- [ ] Add a new movie: The user can add a new movie to the database by entering its title, genre, director, release date, and actors.
- [ ] Edit a movie: The user can edit any existing movie by updating its information, such as the title, genre, director, release date, or actors.
- [ ] Delete a movie: The user can delete any movie from the database.
- [ ] View all movies: The program should display a list of all the movies in the database with their corresponding information.
- [ ] Search movies: The program should allow the user to search for a specific movie based on its title or any other criteria, such as the director, genre, release date, or actors.
- [ ] Save and load data: The program should have the ability to save and load data to and from a file to ensure that movie data is not lost between program sessions.
- [ ] User interface: The program should have an easy-to-use graphical user interface that enables users to perform all the required actions with ease.
- [ ] Error handling: The program should handle any input errors gracefully, displaying appropriate messages to the user if any invalid input is entered.
- [ ] Data validation: The program should validate all input data to ensure that it is in the correct format and that no incorrect data is stored in the database.

***Please find attached mdms_dic.py for the sample game code.***

# Submission guideline:
Submit your Python file or code using the Start Assignment button in the top-right corner of the assignment page in Canvas.
