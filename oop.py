# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def say_hello(self):
#         print("Hello, my name is", self.name)


# p1 = Person("Ali", 25)

# p1.say_hello()

# print(p1.age)

# class Book:
#     def __init__(self, page):
#         self.pages = page


# book = Book(250)

# print(book.pages)







# A small library of letters
letters = {
    'A': ["  *  ", " * * ", "*****", "*   *", "*   *"],
    'B': ["****", "*   *", "****", "*   *", "****"]
}

name = input("Enter your name: ")
first_char = name[0].upper()

# Check if we have the letter in our "library"
if first_char in letters:
    for row in letters[first_char]:
        print(row)
else:
    print("Sorry, I don't have a drawing for that letter yet.")
