from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "p"
    HEADING = "h"
    CODE = "code"
    QUOTE = "blockquote"
    UNORDERED_LIST = "ul"
    ORDERED_LIST = "ol"


def block_to_block_type(block):
    heading = re.match(r"^(#{1,6}) (.*)", block)
    code = re.findall(r"^```\n.*\n```$", block)
    if heading:
        return BlockType.HEADING
    if code:
        return BlockType.CODE
    check_quote = True
    for line in block.split("\n"):
        if not re.match(r"^>", line):
            check_quote = False
            break
    if check_quote:
        return BlockType.QUOTE
    check_unordered_list = True
    for line in block.split("\n"):
        if not re.match(r"^- ", line):
            check_unordered_list = False
            break
    if check_unordered_list:
        return BlockType.UNORDERED_LIST
    check_ordered_list = True
    for line in block.split("\n"):
        if not re.match(r"^\d+\. ", line):
            check_ordered_list = False
            break
    if check_ordered_list:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH



