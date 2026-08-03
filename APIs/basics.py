if __name__ == "__main__":
    # an API is known as application programming interface 
    # think of website it has data which is shown to public 
    # that data is stored in our database 
    # now when users interact with teh website they can now access the entire database BUT WE WONT WANT THAT because then they can do DELETE TABLE Main_table (LOL)
    # so to show the data but also not provide the entire access to DB we expose specific "endpoints" that basically we can say lead to that specific data 
    # hence we use APIs to access those endpoints 

    ###################################################### USING API BY IMPORTING A LIBRARY ##################################################
    # just like many other responsibility isolation for numarical python (numpy) and data ingetion , cleaning , validation (pandas)
    # we also get ability to go to those endpoints / links by using "requests"

    import requests
    import json # will explain this later so bear with me :)

    ###################################################### BASICS OF API ########################################################
    # for any DB or any API we have specifc methods like 

    # DELTE - Duhh delete (D) ^
    # PUT - updation      (U) |
    # GET - retrival      (R) |
    # POST - Create       (C) |

    # this is basically the industry standard what we call CRUD operation 

    ################################################# RETRIVAL OF DATA ##########################################################
    ## we will be suing pokemon api which is something like this :

    '''
    https://pokeapi.co/api/v2/
    │       │       │    │
    │       │       │    └── API Version
    │       │       └────── Base Path
    │       └────────────── Domain
    └────────────────────── Protocol
    '''

    base_url = "https://pokeapi.co/api/v2/"

    def get_pokemon_info(name):
        pokemon_url = f"{base_url}/pokemon/{name}"
        pokemon_info = requests.get(pokemon_url) # this will just provide us the request status which is <200> since it will work

        if pokemon_info.status_code == 200:
            print("Data Retrived ! \n HERE IS YOU DATA: \n")
            pokemon_data = pokemon_info.json() # now we will get a structured response 
            print(json.dumps(pokemon_data, indent=4)) # just makes the data more "presentable"

        else:
            print(f"Failed to Retrive the Data {pokemon_info.status_code}\n please check the \"get_pokemon_info\" function")

    # NOTICE : since the requests.get provides us gibberish 
    # requests.get() returns a Response object, which contains the server's raw response data (headers, status codes, and bytes).
    # BASICALLY : it gives us the thing we dont need 
    # to convert all that to JSON to get actual DATA 

    # to get that we need to use the internal library called json 
        
    pokemon_name = input("Please Provide the name of pokemon to get its info: ")
    print("\n")
    get_pokemon_info(pokemon_name)


#################################################### EXTRACTING ONLY NEEDED DATA ###############################################
#   here we see that the api.json() just gave us a huge block of json 
#   we dont want that we only want say "name", "height", "weight", "type" and some other things
#   we do realize thsi that if we create a class called pokemon where it automatically extracts the needed cols then we only need to do pikachu.name 
#   since pikachu is a class of pokemon so we can have those function calls apply for pikachu as well 

    class Pokemon :
        def __init__(self,pokemon_data : dict):
            # basic informations 
            self.id = pokemon_data["id"]
            self.name = pokemon_data["name"]
            self.height = pokemon_data["height"] / 10      # dm -> meters
            self.weight = pokemon_data["weight"] / 10      # hg -> kg

            ################################ ABILITIES ################################

            # the API returns abilities as a LIST because a pokemon can have multiple abilities.
            #
            # Example:
            #
            # "abilities": [
            #     {"ability": {"name": "static"}},
            #     {"ability": {"name": "lightning-rod"}}
            # ]
            #
            # Since there can be more than one ability, we use a list comprehension
            # to iterate through every ability and extract only its name.

            self.abilities = [
                ability["ability"]["name"].title()
                for ability in pokemon_data["abilities"]
            ]
            # the list comprehension does this -> 1st the loop gets iterated and then the above expression 

            self.types = [
                pokemon_type["type"]["name"].title()
                for pokemon_type in pokemon_data["types"]
            ]

#################### NOW WE WILL APPLY THE ABOVE CLASS INSIDE OUR UPDATED FUNCITON SO WE WILL ONLY EXTRACT WHAT WE WANT 
    def get_pokemon_info_updated(name):
            pokemon_url = f"{base_url}/pokemon/{name}"
            pokemon_info = requests.get(pokemon_url) 

            if pokemon_info.status_code == 200:
                print("Data Retrived ! \n HERE IS YOU DATA: \n")
                pokemon_data = pokemon_info.json() 
                provided_pokemon = Pokemon(pokemon_data)
                print(f"Name: {provided_pokemon.name}\nWeight: {provided_pokemon.weight}\nHeight: {provided_pokemon.height}\nabilities: {provided_pokemon.abilities}\nType: {provided_pokemon.types}")

            else:
                print(f"Failed to Retrive the Data {pokemon_info.status_code}\n please check the \"get_pokemon_info\" function")


    print("\n\n\n\n\n\n\nWHAT YOU ARE GOING TO SEE IS STRAIGHT UP MAGIC WE ARE GOING TO GET RID OF THE ABOVE GARBAGE ;) \n\n")
    
    user_pokemon = input("Provide The pokemon you want the data of: ")
    print("\n\n\n")
    get_pokemon_info_updated(user_pokemon)
    
    
    
 
