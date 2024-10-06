class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        def check():
            i, j = 1, 1
            while j < len(sep2) and sep1[i] == sep2[j]:
                i += 1
                j += 1
            # print(i, j)
            if j == len(sep2):
                return True
            while i < len(sep1) and sep1[i] != sep2[j]:
                i += 1
            # print(i, j)
            if i == len(sep1):
                return False
            while i < len(sep1) and j < len(sep2) and sep1[i] == sep2[j]:
                i += 1
                j += 1
            # print(i, j)
            if i == len(sep1) and j == len(sep2):
                return True
            return False
        
        sep1 = sentence1.split()
        sep2 = sentence2.split()

        if len(sep1) == len(sep2):
            for i in range(len(sep1)):
                if sep1[i] != sep2[i]:
                   return False
            return True 
        
        if len(sep1) < len(sep2):
            sep1, sep2 = sep2, sep1

        if len(sep2) == 1:
            flag = False
            for i in list(filter(lambda x: sep1[x] == sep2[0], range(len(sep1)))):
                if i in (0, len(sep1) - 1):
                    flag = True
            return flag
        

        if sep1[0] != sep2[0] and sep1[len(sep1)-1] != sep2[len(sep2)-1]:
            return False
        

        if sep1[0] == sep2[0] and check(): # 앞이 일치할 때
            return True

        if sep1[len(sep1) - 1] == sep2[len(sep2) - 1]: # 뒤에가 일치하면 뒤집기
            sep1 = sep1[::-1]
            sep2 = sep2[::-1]
            return check()
            

       
        # switch = True
        # switch_cnt = 0
        # i, j = 0, 0
        # while True:
        #     while i < len(sep1) and j < len(sep2):
        #         if switch and sep1[i] == sep2[j]:
        #             i += 1
        #             j += 1
        #         elif not switch and sep1[i] != sep2[j]:
        #             i += 1
        #         else: 
        #             break
        #     if i >= len(sep1) or j >= len(sep2):
        #         break
        #     switch = not switch
        #     switch_cnt += 1
        # print(switch_cnt)
        
        # return True if (i == len(sep1) and j == len(sep2) and switch_cnt == 2) or (switch_cnt == 0) else False
