# implement run-length encoding and decoding

x = input()

cursor, buildup = "", ""
streak = 1

for y in x:

    if y != cursor:

        if cursor != "":
            buildup += str(streak) + cursor
        cursor = y
        streak = 1

    else:
        streak += 1

buildup += str(streak) + cursor

print(buildup)