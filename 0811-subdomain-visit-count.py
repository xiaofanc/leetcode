from typing import List
import collections 
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = collections.Counter()
        
        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            frags = domain.split('.')
            for i in range(len(frags)):
                ans['.'.join(frags[i:])] += count
        
        return ["{} {}".format(ct,dom) for dom, ct in ans.items()]
        #return ["%d %s" % (c[k], k) for k in c]

s=Solution()
print(s.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))