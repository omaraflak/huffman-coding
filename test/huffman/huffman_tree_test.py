from huffman.huffman_tree import HuffmanTree

def test_create():
    data = bytes([4, 7, 7, 8, 8, 8])

    tree = HuffmanTree.create(data)

    assert tree == HuffmanTree(
        6,
        left=HuffmanTree(3, 8),
        right=HuffmanTree(
            3,
            left=HuffmanTree(1, 4),
            right=HuffmanTree(2, 7)
        )
    )

def test_encode():
    tree = HuffmanTree.create(bytes([
        252,
        147, 147,
        92, 92, 92,
        251, 251, 251, 251
    ]))

    result = tree.encode(bytes([252, 147, 92, 251]))

    assert result == '110111100'

def test_decode():
    tree = HuffmanTree.create(bytes([
        252,
        147, 147,
        92, 92, 92,
        251, 251, 251, 251
    ]))
    data = bytes([252, 147, 92, 251])
    encoded = tree.encode(data)

    decoded = tree.decode(encoded)

    assert decoded == data
