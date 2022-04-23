# Huffman Coding

Compression algorithm according to Huffman Coding method.

```python
data = 'hello world, this is a message to be encoded using Huffman Coding.'.encode()
tree = HuffmanTree.create(data)
encoded = tree.encode(data) # 11111111111111010...
# len(encoded) == 496
# len(data) * 8 == 528
assert tree.decode(encoded) == data
```