import pyshorteners
link = input("Enter the Link: ")

shortener = pyshorteners.shortener()
x = shortener.tinyurl.short(link)
print(x)
