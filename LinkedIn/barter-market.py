"""
You have some comic books and some coins, you can trade a comic book + coins needed to get a fiction book.
coinsOffered is the number of coins offered if you sell a comic book.
You want to get as many fiction books as possible.

You had 10 comic books, coins you have 10, coinsNeeded: 1, coinsOffered: 1.
You can trade all your comic books for fiction books in this case, you don't need to sell any.

You have 4 comic books, coins you have: 8, coinsNeeded: 4, coinsOffered: 3
You can trade 2 comic books for fiction books. If you try to sell one comic book, your coins will go up to 11 which is not enough for 3rd fiction book - so the answer is 2.
"""

# TLE: passed 8/13
def berterMarket(comicBooks, coins, coinsNeeded, coinsOffered):
	res = 0
	while coins < coinsNeeded:# make it faster?
		coins += coinsOffered # books = coinsNeeded // coinsOffered
		comicBooks -= 1       # comicBooks -= books, coins += coinsOffered * books
		if comicBooks <= 1:
			break

	while coins >= coinsNeeded and comicBooks >= 1:
		res += 1
		coins -= coinsNeeded
		comicBooks -= 1

		while comicBooks >= 2 and coins < coinsNeeded:
			coins += coinsOffered
			comicBooks -= 1
	return res

