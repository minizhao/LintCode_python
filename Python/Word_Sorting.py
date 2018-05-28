

#单词给定字典后排序，思路先把对应的字符重新找回来，然后用argsort
class Solution:
    """
    @param alphabet: the new alphabet
    @param words: the original string array
    @return: the string array after sorting
    """

    def str_reg(self,words):

        words_dict={}
        for idx,w in enumerate(words):
            t=''.join([str(self.alphabet[x]) for x in tuple(w)])
            words_dict[idx]=t

        return words_dict

    def wordSort(self, alphabet, words):
        if len(words)<=1:
            return words

        #与正确的字符顺序对应起来，作为词典
        self.alphabet=dict(zip(list(tuple(alphabet)),sorted(tuple(alphabet))))

        words_dict=self.str_reg(words)
        words_dict=sorted(words_dict.items(),key = lambda x:x[1])

        rst=[words[x[0]] for x in words_dict]
        return rst
