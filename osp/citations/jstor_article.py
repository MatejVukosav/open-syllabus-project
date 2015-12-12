

import datetime

from bs4 import BeautifulSoup


class JSTOR_Article:


    def __init__(self, path):

        """
        Parse the XML.

        Args:
            path (str): The XML manifest path.
        """

        with open(path, 'rb') as fh:
            self.xml = BeautifulSoup(fh, 'lxml')


    @property
    def article_id(self):

        """
        Query the article id.

        Returns: str
        """

        return self.xml.select_one('article-id').get_text()


    @property
    def article_title(self):

        """
        Query the article title.

        Returns: str
        """

        return self.xml.select_one('article-title').get_text()


    @property
    def journal_title(self):

        """
        Query the journal title.

        Returns: str
        """

        return self.xml.select_one('journal-title').get_text()


    @property
    def pub_date(self):

        """
        Assemble the publication date in ISO format.

        Returns: str
        """

        date = datetime.date(
            int(self.xml.select_one('pub-date year').get_text()),
            int(self.xml.select_one('pub-date month').get_text()),
            int(self.xml.select_one('pub-date day').get_text()),
        )

        return date.isoformat()
