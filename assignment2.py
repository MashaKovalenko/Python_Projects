# while user selects "4":
#     show the menu
#     ask for choice
#     if "1": ask for link and title, save to the file 
#     if "2": statistics
#     if "3": view bookmark and show the file
#     if "4": exit

wishlist_count = 0
work_count = 0
playlist_count = 0
misc_count = 0
line = ""

while True:
    print("Welcome to the Bookmark Manager")
    print("(1) Add a bookmark")
    print("(2) Statistics")
    print("(3) View bookmarks")
    print("(4) Exit Program")

    choice = input("")
    print()

    if choice == "1":
        link = input("Enter the bookmark's link: ")
        title = input("Enter the bookmark's title: ")
        category_choice = input("Enter category, 1 for Wishlist, 2 for Work, 3 for Playlist, 4 for Miscellaneous: ")

        if category_choice == "1":
            f1 = open("wishlist.txt", "a")
            line = title + " " + link + "\n"
            f1.write(line)
            f1.close()
            wishlist_count += 1
            print()

        elif category_choice == "2":
            f2 = open("work.txt", "a")
            line = title + " " + link + "\n"
            f2.write(line)
            f2.close()
            work_count += 1
            print()

        elif category_choice == "3":
            f3 = open("playlist.txt", "a")
            line = title + " " + link + "\n"
            f3.write(line)
            f3.close()
            playlist_count += 1
            print()

        elif category_choice == "4":
            f4 = open("miscellaneous.txt", "a")
            line = title + " " + link + "\n"
            f4.write(line)
            f4.close()
            misc_count += 1
            print()

        else:
            print("Invalid choice. Please try again.")
            print()

    elif choice == "2":
        print(wishlist_count, "wishlist")
        print(work_count, "work")
        print(playlist_count, "playlist")
        print(misc_count, "miscellaneous")
        print()

    elif choice == "3":
        category_choice = input("Enter category, 1 for Wishlist, 2 for Work, 3 for Playlist, 4 for Miscellaneous: ")

        if category_choice == "1":
            try:
                f1 = open("wishlist.txt", "r")
                for line in f1:
                    print(line.strip())
                f1.close()
            except FileNotFoundError:
                print("There is no information in this bookmark yet")
            print()

        elif category_choice == "2":
            try:
                f2 = open("work.txt", "r")
                for line in f2:
                    print(line.strip())
                f2.close()
            except FileNotFoundError:
                print("There is no information in this bookmark yet")
            print()

        elif category_choice == "3":
            try:
                f3 = open("playlist.txt", "r")
                for line in f3:
                    print(line.strip())
                f3.close()
            except FileNotFoundError:
                print("There is no information in this bookmark yet")
            print()

        elif category_choice == "4":
            try:
                f4 = open("miscellaneous.txt", "r")
                for line in f4:
                    print(line.strip())
                f4.close()
            except FileNotFoundError:
                print("There is no information in this bookmark yet")
            print()

        else:
            print("Invalid choice. Please try again.")
            print()

    elif choice == "4":
        break

    else:
        print("Invalid choice. Please try again.")
        print()
