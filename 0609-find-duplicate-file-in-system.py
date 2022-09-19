"""
Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
Output: [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
"""
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dct = defaultdict(list)
        for path in paths:
            record = path.split(" ")
            p = record[0]
            for file in record[1:]:
                f = file.split("(")
                filename = f[0]
                content = f[1][:-1]
                concatF = p+'/'+filename
                dct[content].append(concatF)
        res = []
        for value in dct.values():
            if len(value) > 1:
                res.append(value)
        return res


            