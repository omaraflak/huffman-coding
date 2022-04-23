# Huffman Coding

Compression algorithm according to Huffman Coding method.

```python
from huffman.huffman_tree import HuffmanTree 

data = 'hello world, this is a message to be encoded using Huffman Coding.'.encode()

# Build Huffman Tree from the data
tree = HuffmanTree.create(data)

# Encoding...
encoded = tree.encode(data) # 11111111111111010...

# Difference in size before/after encoding
# len(data) * 8 == 528
# len(encoded) == 496

# Decoding...
assert tree.decode(encoded) == data
```