books = {"jacqueline wilson": ["the story of tracy beaker", "my sister jodie", "double act"],"david walliams": ["gangsta granny", "demon dentist", "billionaire boy"],"j.k rowling": ["harry potter and the chambers secret", "harry potter and the prisoner of azkaban ", "harry potter and the deathly hallows"]}

author_name = input("Enter Author's name: ")

if author_name in books:
    book_list = ", ".join(books[author_name])
    print(f"Books by {author_name}: {book_list}")
