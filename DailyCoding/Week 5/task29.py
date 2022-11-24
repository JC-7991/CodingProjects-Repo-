# implement run-length encoding and decoding

s = input()

cursor, buildup = "", ""
streak = 1

for a in s:

    if a != cursor:

        if cursor != "":
            buildup += str(streak) + cursor
        cursor = a
        streak = 1

    else:
        streak += 1

buildup += str(streak) + cursor

print(buildup)