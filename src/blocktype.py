from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"


def block_to_block_type(block: str) -> BlockType:
    if block.startswith('#'):
        return BlockType.HEADING
    elif block.startswith('```') and block.endswith('```'):
        return BlockType.CODE
    elif all(line.startswith('>') for line in block.split('\n')):
        return BlockType.QUOTE
    elif all(line.startswith('- ') for line in block.split('\n')):
        return BlockType.UNORDERED_LIST
    elif all(line.strip().startswith(f"{i+1}. ") for i, line in enumerate(block.split('\n'))):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
    

