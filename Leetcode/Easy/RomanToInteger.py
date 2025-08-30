class Solution(object):
    def romanToInt(self, s):
        dic = {'I' : 1, 'V' : 5, 'X' : 10, 'L':50, 'C':100, 'D':500, 'M':1000}
        counter = dic[s[0]]
        prev = s[0]
        for x in range(1, len(s)):
            value = True
            if prev == 'I':
                if s[x] == 'V':
                    value = False
                    counter+=3
                elif s[x] ==  'X':
                    value = False
                    counter+=8
                prev = ""
            elif prev == 'X':
                if s[x] == 'L':
                    value = False
                    counter+=30
                elif s[x] ==  'C':
                    value = False
                    counter+=80
                prev = ""
            elif prev == 'C':
                if s[x] == 'D':
                    value = False
                    counter+=300
                elif s[x] ==  'M':
                    value = False
                    counter+=800
                prev = ''
            if value: 
                counter+=dic[s[x]]
                prev = s[x]
        return counter
        