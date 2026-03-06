class TrieNode:
    def __init__(self):
        # Dictionary to store children nodes - key is the character, value is the TrieNode
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # Time complexity: O(n), where n is the length of the word
    # Space complexity: O(n), in the worst case when all characters are unique
    def insert(self, word: str) -> None:
        cur = self.root
        # This is hard to visualize, but we are basically nesting dictionaries 
        # within dictionaries for each character in the word
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.endOfWord = True

    # Time complexity: O(n), where n is the length of the word
    # Space complexity: O(1), as we are not using any extra space
    def search(self, word: str) -> bool:
        
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.endOfWord

    # Time complexity: O(1), because there are only 26 characters at a maximum 
        # to check at each node only if that node already existed.
    # Space complexity: O(1), as we are not using any extra space
    def startsWith(self, prefix: str) -> bool:
        
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)