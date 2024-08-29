from time import strftime, localtime


def average(li: list, add_points: int) -> int:
    """
    to calculate the average number of a list that all the items are numbers.

    Args:
        li (list/tuple): a group of numbers that you want to calculate its average number.
        add_points (int): default base value

    Returns:
        int: the average number
    """

    return round(sum(li)/len(li), 2) + add_points


def getlen(li: list) -> int:
    """
    to get the longest item's length in a list.

    Args:
        li (list): a group of elements, and they can be any type.

    Returns:
        int: the longest item's length in a list.
    """

    li = list(map(str, li))
    return len(max(li, key=lambda x: len(x)))


class Team(object):
    def __init__(self, li_scores: list, add_points: int):
        """
        initialization.
        """

        self.li_teams = [str(i) for i in range(1, len(li_scores)+1)]
        self.len_teams = getlen(self.li_teams)
        self.date = strftime("%Y-%m-%d", localtime())

        # calculate every team's average score
        self.li_scores_aver = list()
        self.li_ranks = list()
        for group_scores in li_scores:
            self.li_scores_aver.append(average(group_scores, add_points))
        self.len_scores = getlen(self.li_scores_aver)
        # every person's score
        self.li_scores = li_scores


    def rank(self):
        """
        get every team's rank.
        """

        li_scores_aver_sorted = list(set(self.li_scores_aver))
        li_scores_aver_sorted.sort(reverse=True)
        for team_score in self.li_scores_aver:
            # the rank starts from 1
            self.li_ranks.append(li_scores_aver_sorted.index(team_score)+1)
        self.len_ranks = getlen(self.li_ranks)

        # pre-processing
        self.li_scores_aver = list(map(str, self.li_scores_aver))
        self.li_ranks = list(map(str, self.li_ranks))


    def output(self) -> str:
        """
        make the datas easy to read.

        Returns:
            str: result including team name, its average score and its rank
        """

        self.li_merged = list(zip(self.li_teams, self.li_scores_aver, self.li_ranks))
        template_str = "第 {} 组分数为 {} 分，第 {} 名！ {}\n"
        template_rank = ("[1st]", "[2nd]", "[3rd]")

        res_str = str()
        for team, score, rank in self.li_merged:
            if int(rank) <= 3:
                # warn: to get the correct item, the index should subtract 1
                res_rank_notice = template_rank[int(rank)-1]
            else:
                res_rank_notice = ""

            res_str += template_str.format(team.ljust(self.len_teams), score.ljust(self.len_scores), rank.ljust(self.len_ranks), res_rank_notice)

        return res_str


    def interface(self, type: str) -> tuple:
        """
        defines api here.

        Args:
            type (str): explains which type of data to return

        Returns:
            tuple: informations including the date and their scores
        """

        if type == "teams":
            return self.date, self.li_merged
        elif type == "persons":
            return self.date, self.li_scores
        else:
            return None
