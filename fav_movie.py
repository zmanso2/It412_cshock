#part 1 & 3
import os.path
movie_out = ""

if os.path.isfile("file\ fav_movie_list_out.py") and os.path.isfile("file\movie_list.csv"):
    #causing a silent fail to appear

    with open("file\movie_list.csv") as csv_file:
        for line in csv_file:
            movie_out = movie_out + line.rstrip() + " is my favorite movie!\n"
            #adding in  is my favorite movie!\n" to the movie list without creating a new file yet 
        #print(movie_out) - testing to see if code was working

    with open("file\ fav_movie_list_out.py", "w") as file_out:
        file_out.write(movie_out)
        #adding a new py output into file with "is my favorite movie!" in the output