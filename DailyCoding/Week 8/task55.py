# Implement a URL shortener with the following methods:
# shorten(url), which shortens the url into a six-character
# alphanumeric string, such as zLg6wl.
# restore(short), which expands the shortened string 
# into the original url. If no such shortened string exists, return null.

def idToShortURL(id):

    map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    shortURL = ""
      
    while(id > 0):
        shortURL += map[id % 62]
        id //= 62
  
    return shortURL[len(shortURL): : -1]
  
def shortURLToId(shortURL):

    id = 0
    for i in shortURL:

        val_i = ord(i)

        if(val_i >= ord('a') and val_i <= ord('z')):
            id = id*62 + val_i - ord('a')

        elif(val_i >= ord('A') and val_i <= ord('Z')):
            id = id*62 + val_i - ord('A') + 26

        else:
            id = id*62 + val_i - ord('0') + 52

    return id
  
if __name__ == "__main__":

    id = 12345
    shortURL = idToShortURL(id)
    print("Short URL from 12345 is:", shortURL)
    print("ID from ", shortURL, "is:", shortURLToId(shortURL))