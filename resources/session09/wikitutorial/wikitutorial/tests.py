import unittest

from pyramid import testing


class WikiModelTests(unittest.TestCase):

    def _getTargetClass(self):
        from wikitutorial.models import Wiki
        return Wiki

    def _makeOne(self):
        return self._getTargetClass()()

    def test_constructor(self):
        wiki = self._makeOne()
        self.assertEqual(wiki.__parent__, None)
        self.assertEqual(wiki.__name__, None)


class PageModelTests(unittest.TestCase):

    def _getTargetClass(self):
        from wikitutorial.models import Page
        return Page

    def _makeOne(self, data=u'some data'):
        return self._getTargetClass()(data=data)

    def test_constructor(self):
        instance = self._makeOne()
        self.assertEqual(instance.data, u'some data')


class AppmakerTests(unittest.TestCase):

    def _callFUT(self, zodb_root):
        from wikitutorial.models import appmaker
        return appmaker(zodb_root)

    def test_initialization(self):
        root = {}
        self._callFUT(root)
        self.assertEqual(root['app_root']['FrontPage'].data,
                         'This is the front page')

class WikiViewTests(unittest.TestCase):

    def test_redirect(self):
        from wikitutorial.views import view_wiki
        context = testing.DummyResource()
        request = testing.DummyRequest()
        response = view_wiki(context, request)
        self.assertEqual(response.location,
                         'http://example.com/FrontPage')


class PageViewTests(unittest.TestCase):
    def _callFUT(self, context, request):
        from wikitutorial.views import view_page
        return view_page(context, request)

    def test_it(self):
        wiki = testing.DummyResource()
        wiki['IDoExist'] = testing.DummyResource() #<- add this
        context = testing.DummyResource(data='Hello CruelWorld IDoExist')
        context.__parent__ = wiki
        context.__name__ = 'thepage'
        request = testing.DummyRequest()
        info = self._callFUT(context, request)
        self.assertTrue('<div class="document">' in info['content'])
        for word in context.data.split():
            self.assertTrue(word in info['content'])
        for url in (request.resource_url(wiki['IDoExist']),
                    request.resource_url(wiki, 'add_page', 'CruelWorld')):
            self.assertTrue(url in info['content'])
        self.assertEqual(info['edit_url'],
                             'http://example.com/thepage/edit_page')
