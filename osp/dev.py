

from osp.citations.hlom.ranking import Ranking


def print_rank(query):
    for t in query:
        print(
            t['rank'],
            t['record'].count,
            t['record'].marc.title(),
            t['record'].marc.author()
        )


def all_ranks(page_num=1, page_len=100):

    """
    Get unfiltered rankings.
    """

    r = Ranking()
    print_rank(r.rank(page_num, page_len))


def institution_ranks(iid, page_num=1, page_len=100):

    """
    Get text rankings for an institution.

    Args:
        iid (int): The institution id.
    """

    r = Ranking()
    r.filter_institution(iid)
    print_rank(r.rank(page_num, page_len))


def state_ranks(state, page_num=1, page_len=100):

    """
    Get text rankings for a state.

    Args:
        state (str): The state abbreviation.
    """

    r = Ranking()
    r.filter_state(state)
    print_rank(r.rank(page_num, page_len))


def keyword_ranks(query, page_num=1, page_len=100, tsv_limit=1000):

    """
    Get text rankings for a keyword query.

    Args:
        query (str): A free text query.
    """

    r = Ranking()
    r.filter_keywords(query)
    print_rank(r.rank(page_num, page_len))
