from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase

from lists.views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  #  1 request오브젝트 생성
        response = home_page(request)  # 2 응답을 재할당
        self.assertTrue(response.content.startswith(b'<html>'))  # 3 html테그로 시작하는지 확
        self.assertIn(b'<title>To-Do lists</title>', response.content)  # 4 문서 제목 확인
        self.assertTrue(response.content.endswith(b'</html>'))  # 5 끝이 html테그로 끝나는지 확인
