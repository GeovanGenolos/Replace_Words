from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # sort dictionary by length of the roots for shortest root replacement
        dictionary.sort(key=len)
        
        # split the sentence into words
        words = sentence.split()
        
        # iterate over each word in the sentence
        for i in range(len(words)):
            word = words[i]
            for root in dictionary:
                # check if the current word starts with the root
                if word.startswith(root):
                    # replace the word with the root
                    words[i] = root
                    break  # stop checking once the shortest root is found
        
        # join the modified words back into a sentence
        return ' '.join(words)


solution = Solution()
print(solution.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))  # Output will be "the cat was rat by the bat"
print(solution.replaceWords(["a","b","c"], "aadsfasf absbs bbab cadsfafs"))  # Output will be "a a b c"
