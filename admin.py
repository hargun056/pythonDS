def input_something(prompt):
    while True:
        pr=input(prompt)
        if pr.strip():
            return pr
        else:
            print("Enter a valid value")

def input_int(prompt):
    while True:
        pr=int(input(prompt))
        if pr>=1:
            return pr
        else:
            print("Enter an integer greater than or equal to 1")




data=[ { "name": "Forrest Gump", "year": 1994, "duration": 142, "genres": ["Drama", "Romance"] },
{ "name": "Avengers: Endgame", "year": 2019, "duration": 181, "genres": ["Action",
"Adventure", "Drama"] }, { "name": "Back to the Future", "year": 1985, "duration": 114,
"genres": ["Adventure", "Comedy", "Sci-Fi"] } ]

print("---------------------------------------")
print("\t\tWelcome")
print("---------------------------------------")
print()
print()

while True:
    print("a-add")
    print("l-list")
    print("s-search")
    print("v-view")
    print("d-delete")
    print("q-quit")
    choice=input("Enter choice- ")
    if choice=='a':
        mov=input_something("Enter the movie name: ")
        mov_year=input_int("Enter the movie year: ")
        mov_dur=input_int("Enter the movie duration(minutes): ")
        mov_gen=input_something("Enter the genres(separated by commas): ")
        gen_list=mov_gen.split(',')
        
        data.append({"name":mov,"year":mov_year,"duration":mov_dur,"genres": gen_list})
        print("Movie added successfully")
        for i, j in enumerate(data):
                print(f"{i+1}. Movie Name: {j['name']}, Year: {j['year']}, Duration: {j['duration']} minutes, Genres: {j['genres']}")

    elif choice=='l':
        length=len(data)
        if length==0:
            print("No movies saved")
        else:
            for i, j in enumerate(data):
                print(f"{i+1}. Movie Name: {j['name']}, Year: {j['year']}")
    elif choice=='s':
        if len(data)==0:
            print("No movies saved")
        else:
            search = input_something("Enter the search term: ").lower()
            found = False
            for movie in data:
                if (search in movie["name"].lower() or
                    search in str(movie["year"]) or
                    search in str(movie["duration"]) or
                    any(search in genre.lower() for genre in movie["genres"])):
                
                        print("Movie found:")
                        print(f"Movie Name: {movie['name']}, Year: {movie['year']}, Duration: {movie['duration']} mins, Genres: {movie['genres']}")
                        found = True
            if not found:
                print("No movies found")
    elif choice=='v':
        if len(data)==0:
            print("No movies saved")
        else:
            ind=input_int("Enter the index number: ")
            
            if ind>len(data):
                print("Invalid index")
            else:
                print(f"Movie Name: {data[ind-1]['name']}, Year: {data[ind-1]['year']}, Duration: {data[ind-1]['duration']} minutes, Genres: {data[ind-1]['genres']}")
    elif choice=='d':
        if len(data)==0:
            print("No movies saved")
        else:
            ind=input_int("Enter the index number: ")
            if ind>len(data):
                print("Invalid index")
            else:
                data.pop(ind-1)
                print("Movie and details deleted at index number ",ind)
    elif choice=='q':
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
                  



              
