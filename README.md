# Python_Projects
This program starts by displaying (printing) the following menu, and waits for the user’s choice:
Welcome to the Bookmark Manager:

(1) Add a bookmark
(2) Statistics
(3) View bookmarks
(4) Exit Program

When the user chooses option (1), the program asks the user to enter three information: the webpage link, 
bookmark title, category (a choice between Wishlist, Work, Playlist, Miscellaneous). When the user presses 
enter, the program saves the bookmark in a text file according to the category chosen This means if the user 
chose to add a playlist link then the program will save the bookmark in a file called playlist.txt. Make sure 
to open the file as append mode instead of write mode to prevent from overwriting over saved bookmarks.

Clicking on option (2) will display the numbers of bookmarks entered for each category during the time the 
program is running. This means if you add a bookmark, exit the program, then add a bookmark of the same 
category then the count will be 1. 

Clicking on option (3) will ask the user which category to pick from, and
displays the contents of the category file. Do not worry if you get an error if you chose a category with not 
bookmarks added (no file created). Finally, choosing option (4) will quit the loop and the program.
