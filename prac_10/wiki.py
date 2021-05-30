import wikipedia

user_input = 0
while user_input != "":
    try:
        user_input = input("Search:")
        page_details = wikipedia.page(user_input)
        print(page_details.title)
        print(page_details.summary)
        print(page_details.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    user_input = input("Search:")

