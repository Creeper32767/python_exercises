import os
import sys
from time import sleep

path = os.path.abspath(os.path.dirname(__file__))


def chooser(choices: list):
    """
    universal method to select one element in a list.

    Args:
        choices (list): alternative elements

    Returns:
        Any: one element of the choices
    """

    print("Here are several items to choose.")
    for item in choices:
        print(f"[{choices.index(item)}] {item}")

    choice = input("[chooser] Enter the order to choose one: ")
    try:
        return choices[int(choice)]
    except IndexError:
        return None


def judge_language(sentence: str):
    """
    to tell the language of a sentence.

    Args:
        sentence (str): the sentence that you want to know its language

    Returns:
        str: the language of the sentence
    """
    
    for char in sentence:
        if 11904 <= ord(char) <= 40959:
            return "CHN"

    return "ENG"


def process_srt(file_name: str):
    with open(os.path.join(path, file_name), mode="r", encoding="utf-8") as input_file:
        with open(os.path.join(path, f"{file_name.split('.')[0]+'_processed.srt'}"), mode="w", encoding="utf-8") as output_file:
            subtitles = input_file.read().split("\n\n")
            subtitles = list(filter(lambda x: x != "", subtitles))
            total_num = len(subtitles)
            processed = 0

            # processing part
            for subtitle in subtitles:
                subtitle = subtitle.split("\n")
                if len(subtitle[2]) <= 2:
                        print(f"\n[warn] We met an problem at subtitle-{processed}! (sentences='{subtitle[2]}')")
                        user_choice = input("This line is shorter than 2 characters. Keep it or not [Y/N]: ")
                        if user_choice == "N":
                            continue

                output_file.write(f"{processed+1}\n{subtitle[1]}\n")
                subtitle = subtitle[2:]

                # make all the sentences in the same language get in one line
                for order, line in enumerate(subtitle): 
                    if order == 0:
                        output_file.write(line)
                    else:
                        if judge_language(line) == judge_language(last_sentence):
                            if judge_language(line) == "CHN":
                                output_file.write(line)
                            else:
                                output_file.write(f" {line}")
                        else:
                            output_file.write(f"\n{line}")
                        
                    # save the sentences temporary
                    last_sentence = line

                output_file.write("\n\n")

                # giving information
                processed += 1
                sys.stdout.flush()
                sys.stdout.write(f"\r[{('-'*int(processed*10/total_num)).ljust(10)}]  {processed} / {total_num}")
                sleep(0.01)


file = chooser(os.listdir(path))
process_srt(file)
input("\nFinished. Press 'Enter' to exit.")
