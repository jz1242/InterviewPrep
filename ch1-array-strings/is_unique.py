# Assuming ASCII string
def is_unique(input: str) -> bool:
    if len(input) > 128:
        return False
    char_set = [0 for i in range(0, 257)]

    for char in input:
        if char_set[ord(char)]:
            return False
        char_set[ord(char)] = True
    return True