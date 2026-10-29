#error and exception handling
# FileNotFoundError,TypeError,IndexError,KeyError etc.

# FileNotFoundError
# try:
#     file= open ("dcnjd.txt")
# except FileNotFoundError:
#     file=open("try.txt","w")
#     file.write ("Hello")
# else:
#     content=file.read()
#     print(content)
# finally:
#     file.close()
#     print("File closed")

#raising error(it will raise error despite there is no error in code.)
h=float(input("enter your height"))
w=float(input("enter your width"))

if h > 3:
    raise ValueError("This height is not possible")

bmi=w/h **2
print(bmi)