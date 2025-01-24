def process_lrc(lrc_string: str, split_string: str) -> tuple:
    """
    universal methods to process lyrics string.

    Args:
        lrc_string (str): original string typed by the user.
        split_str (str): the string used to seperate each sentences from each other.

    Returns:
        tuple[str, list[str]]: includes file name and lyrics
    """

    # seperate lyrics from filename
    tmp_li = lrc_string.split(split_string)
    filename = tmp_li[-1]
    lrc_str = tmp_li[0]

    # use "[" to split lines
    lrc_li = lrc_str.split("[")
    # the first element will be ""
    lrc_li.pop(0)
    lrc_li = list(map(lambda s: "["+s, lrc_li))

    return filename, lrc_li


split_string = input("[initialization] Enter the string you used to split: ")
o_lrc = input("[content] original lyrics string: ")
filename, content = process_lrc(o_lrc, split_string)

with open(filename, mode="w", encoding="utf-8") as file:
    for line in content:
        file.write(line+"\n")

with open(filename.split(".")[0]+"_notimesign.txt", mode="w", encoding="utf-8") as file2:
    for line in map(lambda s: s.split("]")[-1], content):
        file2.write(line+"\n")

input("Finished. Press 'Enter' to exit.")
