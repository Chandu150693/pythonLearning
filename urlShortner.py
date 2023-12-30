import pyshorteners


def shot_my_url(url):
    short_obj = pyshorteners.Shortener()
    short_url = short_obj.tinyurl.short(url)
    return short_url


my_short_url = shot_my_url(
    "https://www.youtube.com/watch?v=i8OHyXN4Z90&list=PLVG0Zju2HPJcErpDV1DY4fRBJeTSuvIES&index=8")
print(my_short_url)
