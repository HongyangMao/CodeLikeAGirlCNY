# movies: Difficulty level: Advanced

# Goal #1: Create a program that will print out a list of movie titles and a set of ratings defined below into a particular format.
movie_titles = ['Spectre', 'The Gift', 'The Martian', 'Crimson Peak', 'The Last Witch Hunter']
parental_rating = ['PG-13','R', 'PG-13','R','PG-13']
bechdel_rating = ['No Record','No Record',3,3,'No Record']
imdb_rating = [7.4,7.2,8.2,7.0,6.1]
genre = ['Action / Adventure / Thriller', 'Action / Adventure / Fantasy','Mystery / Thriller','Adventure / Comedy / Drama',' Drama / Fantasy / Horror','Action / Adventure / Fantasy']
# Print each movie's information
for i in range(5):
    print '{0}, {1}, {2}, {3}, {4}'.format(movie_titles[i], parental_rating[i], bechdel_rating[i],imdb_rating[i],genre[i])


# Goal #2: Create an output file stores the information of the movies
# create an outfile
outfile = open("movies.csv","w")
# insert the header row
outfile.write("Moview Titles, Parental Rating, Bechdel Rating, IMDB Rating, Genre\n")
# output each of the rows
for i in range(5):
    outfile.write ('{0}, {1}, {2}, {3}, {4}\n'.format(movie_titles[i], parental_rating[i], bechdel_rating[i],imdb_rating[i],genre[i]))
# close output
outfile.close()
