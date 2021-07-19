#
# @lc app=leetcode.cn id=1169 lang=python3
#
# [1169] 查询无效交易
#

# @lc code=start
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = set()
        trans_dic = {}
        for transaction in transactions:
            temp = transaction.split(',')
            if temp[0] not in trans_dic:
                trans_dic[temp[0]] = [[int(temp[1]), int(temp[2]), temp[-1]]]
            else:
                trans_dic[temp[0]].append([int(temp[1]), int(temp[2]), temp[-1]])
        for k in trans_dic.keys():
            temp_list = sorted(trans_dic[k], key=lambda x : x[0])
            quene = []
            for _, v in enumerate(temp_list):
                while quene and v[0] - quene[0][0] > 60:
                    quene.pop(0)
                quene.append(v)

                for i in quene:
                    if i[-1] != v[-1]:
                        res.add(k + ',' + ','.join(list(map(str, v))))
                        res.add(k + ',' + ','.join(list(map(str, i))))
                if v[1] > 1000:
                    res.add(k + ',' + ','.join(list(map(str, v))))
        result = []
        for a in res:
            for b in transactions:
                if a == b:
                    result.append(a)
        return result

        
# @lc code=end

