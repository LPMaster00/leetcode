class Solution:
    def isValid(self, s: str) -> bool:
        if (s[0] == ")" or s[0] == "}" or s[0] == "]"):
            return False

        stack = []

        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            else:
                if (not bool(stack)):
                    return False
                match s[i]:
                    case ")":
                        if stack[-1] == "(":
                            stack.pop()
                        else:
                            return False
                    case "}":
                        if stack[-1] == "{":
                            stack.pop()
                        else:
                            return False
                    case "]":
                        if stack[-1] == "[":
                            stack.pop()
                        else:
                            return False
        if (not bool(stack)):
            return True
        return False
