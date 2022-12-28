# Write an algorithm to justify text.
# Given a sequence of words and an integer line length k,
# return a list of strings which represents each line, fully justified.

def justify_lines(x, y, z):

    narrow_spaces, wider_words = divmod(z - y, len(x) - 1)
    ns = " " * narrow_spaces
    ws = " " * (narrow_spaces + 1)
    return ns.join([ws.join(x[0: wider_words + 1]), * x[wider_words + 1:]])


def justify(words, z):

	res = []
	cur_length = 0
	cur_words = []

	for word in words:
		for i in range(0, len(word), z):

			chunk = word[i: i + z]

			if len(chunk) + cur_length + len(cur_words) <= z:
				cur_words.append(chunk)
				cur_length += len(chunk)

			else:
				res.append(justify_lines(cur_words, cur_length, z))
				cur_words = [chunk]
				cur_length = len(chunk)

	if cur_words:
		res.append(justify_lines(cur_words, cur_length, z))

	return res

if __name__ == '__main__':

	print("\n".join(justify(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16)), "\n")
	print("\n".join(justify(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 14)), "\n")
	print("\n".join(justify(["sonic", "heroes", "is", "the", "best", "game", "ever", "made"], 16)), "\n")
	print("\n".join(justify(["sonic", "heroes", "is", "the", "best", "game", "ever", "made"], 20)), "\n")