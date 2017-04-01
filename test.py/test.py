# #1.
# message = "greetings from the planet zorgon"
# listOfWords = message.split()
# print listOfWords
# for eachWordidx in range(len(listOfWords)):
#     print listOfWords[eachWordidx]
# 
# #2.
# def remove_spaces(s):
#     resStr = ""
#     for ch in s:
#         if ch != " ":
#             resStr = resStr + ch
#     return resStr
# 
# print (remove_spaces("he | | oworld"))
# 
# #3.
# def remove_chars(s, letters2Remove = "aeiou"): # remove from s
#     resStr = ""
#     for ch in s:
#         if ch not in letters2Remove:
#             resStr = resStr + ch
#     return resStr
# print(remove_chars("hello world"))
#     
    
# x = "hi"
# y = 3
# print(len(x))
# print(type(x))
# z = str(y)
# print(type(z))
# l  = raw_input("Please enter your name")
# print(l+ " hi")

# for idx in ["hi","bye"]:
#     print(idx + " ok")

def s(x, lim):
    w = x
    for i in range(lim):
        w = w - i
    return w
def t(k):
    for b in range(3, 3 + k):
        print(s(2, b))
t(7)