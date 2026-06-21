import connect
from models import Author, Quote

def main():
    while True:
        user_input = input("Enter a command: ")
        command, value = parse_input(user_input)

        if command is None:
            print("Invalid input!")
        elif command == "exit":
            print("Goodbye!")
            break
        elif command == "name":
            search_by_name(value)
        elif command == "tag":
            search_by_tag(value)
        elif command == "tags":
            search_by_tags(value)
        else:
            print("Unknown command!")

def parse_input(user_input):
    user_input = user_input.strip()
    if not user_input:
        return None, None

    if user_input.lower() == "exit":
        return "exit", None

    if ":" not in user_input:
        return None, None

    command, value = user_input.split(":", 1)
    command = command.strip()
    value = value.strip()

    if not command or not value:
        return None, None

    return command, value

def search_by_name(author_name):
    author_obj = Author.objects(fullname=author_name).first()
    if not author_obj:
        print("Author not found")
        return
    quotes = Quote.objects(author=author_obj)
    if not quotes:
        print("No quotes found")
        return
    for quote in quotes:
        print(quote.quote)

def search_by_tag(tag_name):
    quotes = Quote.objects(tags=tag_name)
    if not quotes:
        print("No quotes found")
        return
    for quote in quotes:
        print(quote.quote)

def search_by_tags(tags_value):
    tag_list = [tag.strip() for tag in tags_value.split(",")]
    quotes = Quote.objects(tags__in=tag_list)
    if not quotes:
        print("No quotes found")
        return
    for quote in quotes:
        print(quote.quote)

if __name__ == "__main__":
    main()