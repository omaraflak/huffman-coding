from dataclasses import dataclass
from collections import Counter, deque
from functools import cached_property
from typing import Optional

@dataclass
class HuffmanTree:
    value: int
    data: Optional[int] = None
    left: Optional['HuffmanTree'] = None
    right: Optional['HuffmanTree'] = None

    @staticmethod
    def create(data: bytes) -> 'HuffmanTree':
        counts = sorted(Counter(data).items(), key=lambda x: x[1])
        assert len(counts) > 1
        (d1, c1), (d2, c2) = counts[:2]
        left = HuffmanTree(c1, d1)
        right = HuffmanTree(c2, d2)
        root = HuffmanTree(c1 + c2, left=left, right=right)
        for data, count in counts[2:]:
            node = HuffmanTree(count, data)
            root = HuffmanTree(node.value + root.value, left=node, right=root)
        return root

    @cached_property
    def mapping(self) -> dict[int, str]:
        bin_map: dict[int, str] = dict()
        queue = deque([(self, '')])
        while queue:
            node, prefix = queue.popleft()
            if node.data is not None:
                bin_map[node.data] = prefix
            if node.left:
                queue.append((node.left, prefix + '0'))
            if node.right:
                queue.append((node.right, prefix + '1'))
        return bin_map

    def encode(self, data: bytes) -> str:
        return ''.join([self.mapping[i] for i in data])

    def decode(self, binary: str) -> bytes:
        result: list[int] = []
        root = self
        for b in binary:
            if (b == '0' and not root.left) or (b == '1' and not root.right):
                result.append(root.data)
                root = self

            if b == '0':
                root = root.left
            if b == '1':
                root = root.right

        result.append(root.data)
        return bytes(result)
    
    def __eq__(self, other: object) -> bool:
        if type(other) is not HuffmanTree:
            return False
        
        if self.value != other.value:
            return False
        
        if self.data != other.data:
            return False
        
        return self.left == other.left and self.right == other.right
