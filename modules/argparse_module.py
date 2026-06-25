def hello(name,lang):
    greetings = {
        "Eng" : "Hello",
        "Span" : "Hola",
        "Ger" : "Halo"
    }
    message = f"{greetings[lang]} {name}"
    print(message)
if __name__ == "__main__":
   
    import argparse
    parser = argparse.ArgumentParser(
        description = "Provide a personal greeting"
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help= "The name of person you want to greet"
    )

    parser.add_argument(
        "-l","--lang", metavar="Language", required=True, help= "Provide the language",
        choices=["Eng","Span","Ger"]
    )

    args = parser.parse_args()

    hello(args.name, args.lang)