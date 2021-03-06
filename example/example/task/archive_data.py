# -*- coding:utf-8 -*-
from parade.core.task import SqlETLTask


class Db2Es(SqlETLTask):

    @property
    def checkpoint_conn(self):
        """
        the connection to record the checkpoint
        default value is the target connection
        :return:
        """
        return 'rdb-conn'

    @property
    def target_conn(self):
        """
        the target connection to write the result
        :return:
        """
        return 'elastic-conn'

    @property
    def etl_sql(self):
        return """
        SELECT
            movie_title, genres,
            title_year, content_rating,
            budget, num_voted_users, imdb_score
        FROM movie_data
        """

    @property
    def source_conn(self):
        return 'rdb-conn'

    @property
    def deps(self):
        return ["movie_data"]
