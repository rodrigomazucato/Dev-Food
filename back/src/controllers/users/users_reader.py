from src.model.repositories.interfaces.iusers_repository import IUsersRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse


class UsersReader:
    def __init__(self, users_repo: IUsersRepository):
        self.__users_repo = users_repo

    def get_all_users(self, http_request: HttpRequest) -> HttpResponse:
        users = self.__users_repo.list_users()

        if not users:
            raise Exception("No users in the list!")

        return self.__format_response(users)

    def __format_response(self, users) -> HttpResponse:
        users_data = [user.to_dict() for user in users]
        
        return HttpResponse(
            body={
                "data": {
                    "Type": "User",
                    "count": len(users),
                    "attributes": users_data,
                }
            },
            status_code=200
        )