def countSubArrayProductLessThanK(a, n, k):
        #Code here
        # a = set(a)
        # a = list(a)
        # a.sort(reverse=True)
        # n = len(a)
        # count = 0
        # for i in range(n):
        #     prod = a[i]
        #     count += 1
        #     for j in range(i+1,n):
        #         prod = prod * a[j]
        #         if prod <= k:
        #             count += 1
        #         else:
        #             break
                
        # return count
        count = 0
        for i in range(n):
            prod = a[i]
            # count += 1
            for j in range(i+1,n+1):
                # prod = prod * a[j]
                if prod < k:
                    count += 1
                else:
                    break
                try:
                    fact*= a[j]
                except:
                    pass              
        return count