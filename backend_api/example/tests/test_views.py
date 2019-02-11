import json
from django.test import TestCase
from django.contrib.auth.models import User as DjangoUser
from model_mommy import mommy


class ViewTests(TestCase):

    def test_get_users(self):
        user = mommy.make(DjangoUser)
        body = {'query' : '''
            query {
              users {
                id,
                username
              }
            }
        '''
        }

        resp = self.client.post('/api', json.dumps(body),
                                 content_type='application/json')

        assert resp.status_code == 200
        data = json.loads(resp.content.decode())
        assert len(data['data']['users']) == 1
        assert data['data']['users'][0] == {
            'id': str(user.id),
            'username': user.username
        }
