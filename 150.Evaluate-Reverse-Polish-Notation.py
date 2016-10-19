class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operation = {"+": operator.add, "-" : operator.sub, "*" : operator.mul, "/": operator.div }
        result = []
        for i in tokens:
            if i in operation:
                if len(result) > 1:
                    opr1 = result.pop()
                    opr2 = result.pop()
                    if opr1 * opr2 < 0 and i == "/":
                        if opr2 % opr1 != 0:
                            result.append(operation[i](opr2,opr1)+1)
                        else:
                            result.append(operation[i](opr2,opr1))
                    else:
                        result.append(operation[i](opr2,opr1))
            else:
                temp = int(i)
                result.append(temp)
        return result[0]
        