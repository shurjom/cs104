def remove_chars(s, letters2Remove = "aeiou"): # remove from s
    resStr = ""
    for ch in s:
        if ch not in letters2Remove:
            resStr = resStr + ch
    return resStr
print(remove_chars("hello world"))
    
