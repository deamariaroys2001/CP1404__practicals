import wikipedia

title = input("Search:")
while title != "":
    try:
        title = input("Search:")
        print(wikipedia.summary(title))
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    title = input("Search:")
