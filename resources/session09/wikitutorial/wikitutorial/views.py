from pyramid.view import view_config
# one import
import re

# and one module constant
WIKIWORDS = re.compile(r"\b([A-Z]\w+[A-Z]+\w+)")

from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config # <- ALREADY THERE

@view_config(context='.models.Wiki')
def view_wiki(context, request):
    return HTTPFound(location=request.resource_url(context,
                                                   'FrontPage'))
# an import
from docutils.core import publish_parts

# and a method
@view_config(context='.models.Page', renderer='templates/view.pt')
def view_page(context, request):
    wiki = context.__parent__

    def check(match):
        word = match.group(1)
        if word in wiki:
            page = wiki[word]
            view_url = request.resource_url(page)
            return '<a href="%s">%s</a>' % (view_url, word)
        else:
            add_url = request.application_url + '/add_page/' + word
            return '<a href="%s">%s</a>' % (add_url, word)

    content = publish_parts(
        context.data, writer_name='html')['html_body']
    content = WIKIWORDS.sub(check, content) #<- add this line
    return #... <- this already exists

def view_page(context, request):
        #...
        content = wikiwords.sub(check, content) #<- already there
        edit_url = request.resource_url(context, 'edit_page') #<- add
        return dict(page=context,
                    content=content,
                    edit_url = edit_url)