class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_1, len_2 = len(s1), len(s2)
        #假如s1字符串长度大于s2，说明s1不包含在s2中
        if len_1 > len_2:
            return False

        # 因为字符串都是a-z的字母，所以我们可以使用一个长度为26的int数组来存储每个字母出现的个数
        char_count_1 = [0 for i in range(26)]
        char_count_2 = char_count_1.copy()
        #返回a对应的ascii码值
        ascii_a = ord('a')

        for i in range(len_1):
            #加减使用Ascii码，-'a'正好对应a-z在数组中的索引，值为该字母出现的次数
            char_count_1[ord(s1[i]) - ascii_a] += 1
            char_count_2[ord(s2[i]) - ascii_a] += 1
        #//窗口大小为s1.length，索引从[0 —— s1.length-1]到[s2.length-s1.length —— s2.length-1]
        for i in range(len_1, len_2):
            if self.isEqual(char_count_1, char_count_2):
                return True
            char_count_2[ord(s2[i - len_1]) - ascii_a] -= 1
            char_count_2[ord(s2[i]) - ascii_a] += 1
        return self.isEqual(char_count_1, char_count_2)

    def isEqual(self, char_count_1, char_count_2):
        for i in range(26):
            if char_count_1 != char_count_2:



































                return False
        return True
