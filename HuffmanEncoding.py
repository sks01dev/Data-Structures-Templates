class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

nodes = []

# creates the initial nodes with chars from word & their freq 
def count_frequencies(word):
    mpp = {}
    
    for char in word:
        if char not in mpp:
            freq = word.count(char)
            mpp[char] = freq
            nodes.append(Node(char, freq))


def build_huffman_tree():
    while len(nodes) > 1:
        # Based on freq, sort ascendingly
        nodes.sort(key = lambda x : x.freq)
        # Get the top 2 least freq
        leftNode = nodes.pop(0)
        rightNode = nodes.pop(0)
        # create a new merged node from left an right
        merged = Node(freq = leftNode.freq + rightNode.freq)
        merged.left = leftNode
        merged.right = rightNode
        # add the merged node after popping both top 2 from the list
        nodes.append(merged)
    # return the root node
    return nodes[0]

# fn which stores code for each char in {}
def generate_huffman_code(node, codes, current_code):
    if node is None:
        return
    # if this node has char add it to dict with its curr_code(passed)
    if node.char is not None:
        codes[node.char] = current_code
    # recursively call the left and right halves to get the codes dict filled up
    generate_huffman_code(node.left, codes, current_code + '0') # left->0
    generate_huffman_code(node.right, codes, current_code + '1')

    
def huffman_encoding(word):
    global nodes
    nodes = []
    # this will update the nodes list with the nodes with char and its freq
    count_frequencies(word)
    # This will return the root node of the tree
    root = build_huffman_tree()
    # this will give you the dict of codes for each char in the input word
    codes_ = {}
    codes_= generate_huffman_code(root, codes_, '')
    return codes_

word = "AABACDACA"
code_dict = huffman_encoding(word)
encoded_word = ''.join(code_dict[c] for c in word)

print("Word: ", word)
print("Huffman Code: ", encoded_word)
print("Encodings for each word: ", code_dict)



    

