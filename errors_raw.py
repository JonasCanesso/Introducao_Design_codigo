# 400 -> bad request
# 422 -> unprocessable entity
class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = 'UnprocessableEntity'
        self.status_code = 422

try:
    print('estou no bloco Try.')
    raise HttpUnprocessableEntityError('Estou lançando a exception')
except Exception as exception:
    print('estou no tratamento de erro')
    print(exception.name)
    print(exception.status_code)
    print(exception.message)