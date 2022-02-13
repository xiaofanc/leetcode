"""
One could split the initial integer 1234567890 on the groups containing not more than three digits 1.234.567.890. That results in representation 1 Billion 234 Million 567 Thousand 890 and reduces the initial problem to how to convert 3-digit integer to English word. One could split further 234 -> 2 Hundred 34 into two sub-problems : convert 1-digit integer and convert 2-digit integer. The first one is trivial. The second one could be reduced to the first one for all 2-digit integers but the ones from 10 to 19 which should be considered separately.

"""
class Solution:
    def numberToWords(self, num: int) -> str:
        def one(num):
            one = {
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'
            }
            return one.get(num)
        
        def ten(num):
            ten = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
            return ten.get(num)
        
        def lessthan20(num):
            switcher = {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen'
            }
            return switcher.get(num)
        
        def two(num):
            if not num:
                return ''
            elif num < 10:
                return one(num)
            elif num < 20:
                return lessthan20(num)
            else:
                tenner = num // 10
                rest = num - tenner * 10
                if not rest:
                    return ten(tenner) 
                else:
                    return ten(tenner) + " " + one(rest)
        
        def three(num):
            hundred = num // 100
            rest = num - hundred * 100
            if hundred and not rest:
                return one(hundred) + " Hundred"
            elif not hundred and rest:
                return two(rest)
            elif hundred and rest:
                return one(hundred) + " Hundred " + two(rest)
        
        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num -  billion * 1000000000 - million * 1000000) // 1000
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000
        # print("billion", billion)
        # print("million", million)
        # print("thousand", thousand)
        # print("rest", rest)
        
        if not num:
            return "Zero"
        
        result = ''
        if billion:
            result += three(billion) + " Billion"
        if million:
            result += " " if result else "" # if billion exists add space before adding million str
            result += three(million) + " Million" 
        if thousand:
            result += " " if result else ""
            result += three(thousand) + " Thousand"
        if rest:
            result += " " if result else ""
            # print("three(rest)", three(rest))
            result += three(rest)
        
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.numberToWords(1000))  # "One Thousand"
    print(s.numberToWords(14578))  "Fourteen Thousand Five Hundred Seventy Eight"

        