# Write an algorithm to justify text.
# Given a sequence of words and an integer line length k,
# return a list of strings which represents each line, fully justified.

def justify_line(x, y, z):

	if len(x) == 1:
		return x[0].ljust(z)

	else:

		narrow_spaces, wider_words = divmod(z - y, len(x) - 1)
		ns = " " * narrow_spaces
		ws = " " * (narrow_spaces + 1)
		return ns.join([ws.join(x[0:wider_words + 1]), *x[wider_words + 1:]])


def justify(words, z):

	res = []
	current_length = 0
	current_words = []

	for word in words:
		for i in range(0, len(word), z):

			chunk = word[i:i + z]

			if len(chunk) + current_length + len(current_words) <= z:
				current_words.append(chunk)
				current_length += len(chunk)

			else:
				res.append(justify_line(current_words, current_length, z))
				current_words = [chunk]
				current_length = len(chunk)

	if current_words:
		res.append(justify_line(current_words, current_length, z))

	return res

if __name__ == '__main__':

	print("\n".join(justify(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16)))