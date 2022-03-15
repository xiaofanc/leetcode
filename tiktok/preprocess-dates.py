"""
On a web form, users are asked to enter dates which come in as strings. Before storing them to the database, they need to be converted to a standard date format. Write a function to convert the dates as described.

Given a date string in the format Day Month Year, where:
* Day a string in the form '1st', '2nd', '3rd', '21st', '22nd', '23rd', "31st" and all others are the number + "th", e.g. "4th" or "12th".
* Month is the first three letters of the English language months, like "Jan" for January through "Dec" for December.
* Year is 4 digits ranging from 1900 to 2100.

Convert the date string "Day Month Year" to the date string "YYYY-MM-DD" in thr format "4 digit year - 2 digit month - 2 digit day".

1st Mar 1974 -> 1974-03-01
22nd Jan 2013 -> 2013-01-22
7th Apr 1904 -> 1904-04-07
"""
class Solution:
	def preprocessDate(self, dates):
		Month = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
		date_strings = dates.split(" ")
		day = date_strings[0][:-2]
		month = Month[date_strings[1]]
		year = date_strings[2]

		if len(day) == 1:
			day = "0" + day
		return f'{year}-{month}-{day}'

if __name__ == '__main__':
	s = Solution()
	print(s.preprocessDate("1st Mar 1974"))
	print(s.preprocessDate("22nd Jan 2013"))
	print(s.preprocessDate("7th Apr 1904"))




