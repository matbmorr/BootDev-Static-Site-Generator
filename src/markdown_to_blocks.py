def markdown_to_blocks(markdown):
        return [block.strip() for block in markdown.strip().split('\n\n') if block.strip()]
