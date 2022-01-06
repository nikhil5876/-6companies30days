def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        
        #code here
        # create dictionary of first sorted word
        di = dict()
        for i in words:
            # join sorted words
           s = ''.join(sorted(i))
        #   pick first word
           if di.get(s,0) == 0:
               di[s] = [i]
           else:
               di[s].append(i)
        ans = []
        for i in di:
           ans.append(di[i])
        return ans
