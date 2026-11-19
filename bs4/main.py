from bs4 import BeautifulSoup
# with open("website.html") as file:
#     data=file.read()
#
# soup=BeautifulSoup(data,"html.parser")#we need to specify which type of document we are using
# #print(soup.find_all(name="a"))#it will give all a tag used in html
#
# for tag in soup.find_all(name="a"):
#     #print(tag.string)
#     #or to print string is used inside tag
#     #print(tag.getText())
#     #print(tag.get("href"))#it will give link inside href
#
# heading=soup.find(name="h1",id="name")#use to print particular tag element
# print(heading)

# we can do same with css selector
# tag=soup.select_one(selector="p a")
# print(tag)


