def longest_chain(words):
    # Sort the words by length and lexicographical order
    words.sort(key=lambda x: (len(x), x))
    
    # Initialize a dictionary to store the length of the longest chain for each word
    chain_lengths = {}
    
    # Iterate through each word and update the chain length
    max_length = 0
    for word in words:
        chain_lengths[word] = 1
        for i in range(len(word)):
            substring = word[:i] + word[i+1:]
            if substring in chain_lengths:
                chain_lengths[word] = max(chain_lengths[word], chain_lengths[substring] + 1)
        
        max_length = max(max_length, chain_lengths[word])
    
    return max_length

# Input reading and processing
n = int(input())
words = [input().strip() for _ in range(n)]

# Output the result
result = longest_chain(words)
print(result)
