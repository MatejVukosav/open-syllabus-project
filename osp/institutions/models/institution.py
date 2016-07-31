

import pkgutil

from osp.common import config
from osp.common.utils import read_csv, parse_domain
from osp.common.models import BaseModel

from peewee import CharField
from bs4 import BeautifulSoup


class Institution(BaseModel):


    name = CharField()
    url = CharField(unique=True)
    state = CharField(null=True)
    country = CharField()


    class Meta:
        database = config.get_table_db('institution')


    @classmethod
    def ingest_usa(cls,
        package='osp.institutions',
        path='data/usa.csv',
    ):

        """
        Insert US universities.
        """

        reader = read_csv(package, path)

        for row in reader:
            if row['e_country'] == 'USA':

                # Normalize the URL.
                url = row['web_url'].strip()

                # Clean the fields.
                name = row['biz_name'].strip()
                state = row['e_state'].strip()

                try:
                    cls.create(
                        name=name,
                        url=url,
                        state=state,
                        country='US',
                    )

                except Exception as e:
                    print(e)


    @classmethod
    def ingest_world(cls,
        package='osp.institutions',
        path='data/world.csv',
    ):

        """
        Insert world universities.
        """

        reader = read_csv(package, path)

        for row in reader:
            if row['country'] != 'US':

                # Normalize the URL.
                url = row['url'].strip()

                # Clean the fields.
                name = row['name'].strip()
                country = row['country'].strip()

                try:
                    cls.create(
                        name=name,
                        url=url,
                        state=None,
                        country=country,
                    )

                except Exception as e:
                    print(e)
