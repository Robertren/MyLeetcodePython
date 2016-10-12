class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        aCounter = 0
        bCounter = 0
        lookup = {}
        list1 = []
        testb = []
        for i in range(len(secret)):
            lookup[i] = secret[i]
            list1.append(secret[i])
        print lookup
        print list1
        for i in range(len(secret)):
            if guess[i] == lookup[i]:
                aCounter += 1
                list1[i] = "a"
        print list1
        for i in range(len(list1)):
            if list1[i] != 'a':
                testb.append(guess[i])
        if len(testb) != 0:
            for i in range(len(testb)):
                if testb[i] in list1:
                    bCounter += 1
                    list1[i] = "a"
    
        else:
            bCounter = 0
                
            
                
            
                
        return str(aCounter) +'A' + str(bCounter) +'B'
            
        