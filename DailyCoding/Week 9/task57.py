# Given a string s and an integer k, break up the string into 
# multiple lines such that each line has a length of k or less. 
# You must break it up so that words don't break across lines. 
# Each line has to have the maximum possible amount of words. 
# If there's no way to break the text up, then return null.
# You can assume that there are no spaces at the ends of 
# the string and that there is exactly one space between each word.

def solve(s, k):

    x = s.split()
    
    output = []
    arr = []
    lent = -1
    i = 0
    
    while i < len(x):

        w = x[i]

        if len(w) > k:
            print('\n[*] Cannot complete because of this word: "%s"' % w)
            return

        if (len(w) + lent + 1) <= k:

            lent += len(w) + 1
            arr.append(w)
            i += 1

        else:

            result = ' '.join(arr)
            output.append(result)
            arr = []
            lent = -1

    if arr:
        result = ' '.join(arr)
        output.append(result)

    return output

if __name__ == "__main__":

    str = "I don’t know why but I just enjoy doing this. Maybe it’s my way of dealing with stress or something but I just do it about once every week. Generally I’ll carry around a sack and creep around in a sort of crouch-walking position making goblin noises, then I’ll walk around my house and pick up various different “trinkets” and put them in my bag while saying stuff like “I’ll be having that” and laughing maniacally in my goblin voice (“trinkets” can include anything from shit I find on the ground to cutlery or other utensils). The other day I was talking with my neighbours and they mentioned hearing weird noises like what I wrote about and I was just internally screaming the entire conversation. I am 99 percent sure they don't know it's me but god that 1 percent chance is seriously weighing on my mind."
    X = solve(str, k = 80)
    for s in X:
        print(s)