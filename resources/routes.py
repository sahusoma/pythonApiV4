from .client import ClientsApi, ClientApi
from .auth import SignupApi, LoginApi, ValidateTokenApi


def initialize_routes(api):
    api.add_resource(ClientsApi, '/api/clients')
    api.add_resource(ClientApi, '/api/client/<id>')

    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
    api.add_resource(ValidateTokenApi, '/api/auth/validate')
