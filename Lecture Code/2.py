def remove_spaces(s):
    resStr = ""
    for ch in s:
        if ch != " ":
            resStr = resStr + ch
    return resStr

print (remove_spaces("he | | oworld"))
