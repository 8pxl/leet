import time
from lib import *

class Solution:
    def simplifyPath(self, path: str) -> str:
        out: list[str] = []
        arr = path.split("/")
        for token in arr:
            if not token or token == ".":
                continue
            if token == "..":
                if len(out) >= 1:
                    out.pop()
            else:
                out.append(token)
        return "/" + '/'.join(out)


test = Solution()
curr = time.time()
sol = test.simplifyPath("/a/./b/../../c/"

)
print("finished in ", time.time() - curr)
print(sol)
