def convert(string):
    str1 = string.replace("#", "%23")
    str2 = str1.replace(" ", "%20")
    final = str2.replace(":", "%3A")
    return(final)


