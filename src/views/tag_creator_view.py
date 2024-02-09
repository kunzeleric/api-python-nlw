from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
      Responsibility for interacting with http layer
    '''
    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        print(body)
        return HttpResponse(status_code=200, body={'hello': 'world'})
