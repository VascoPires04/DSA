class Solution(object):
    def letterCombinations(self, digits):
        lista = [None, "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        if digits=="":return []
        elif len(digits)==1:
            return [x for x in lista[int(digits)-1]]
        elif len(digits)==2:
            final = []
            for x in lista[int(digits[0])-1]:
                string = x
                for i in lista[int(digits[1])-1]:
                    final.append(string+i)
            return final
        elif len(digits)==3:
            final = []
            for x in lista[int(digits[0])-1]:
                string = x
                for e in lista[int(digits[1])-1]:
                    for i in lista[int(digits[2])-1]:
                        final.append(x+e+i)
            return final
        else:
            final = []
            for x in lista[int(digits[0])-1]:
                string = x
                for e in lista[int(digits[1])-1]:
                    for i in lista[int(digits[2])-1]:
                        for f in lista[int(digits[3])-1]:
                            final.append(x+e+i+f)
            return final
            
                    
                    