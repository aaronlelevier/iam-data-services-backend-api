from django.test import TestCase

from model_mommy import mommy
from django.contrib.auth.models import User as DjangoUser
from example.schema import schema


class UserTests(TestCase):

    def test_query(self):

        user = mommy.make(DjangoUser)
        query = '''
            query {
              users {
                username
              }
            }
        '''

        ret = schema.execute(query)

        assert ret.data
