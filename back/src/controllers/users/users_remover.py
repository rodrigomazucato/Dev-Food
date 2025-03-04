from src.model.repositories.interfaces.iusers_repository import IUsersRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse


class UsersRemover:
    def __init__(self, users_repo: IUsersRepository):
        self.__users_repo = users_repo


    def delete_user(self, http_request: HttpRequest) -> HttpResponse:
        user_id = int(http_request.params["id"])

        if not self.__check_user(user_id):
            return HttpResponse(
                body={"error": "User not found!"},
                status_code=404
            )

        return self.__delete_user(user_id)


    def __check_user(self, user_id: int) -> bool:
        user = self.__users_repo.get_user_by_id(user_id)
        return user is not None


    def __delete_user(self, user_id: int) -> HttpResponse:
        try:
            self.__users_repo.delete_user(user_id)
            return self.__format_response(user_id)
        
        except Exception as e:
            return HttpResponse(
                body={"error": str(e)},
                status_code=500
            )


    def __format_response(self, user_id: int) -> HttpResponse:
        return HttpResponse(
            body={
                "data": {
                    "Type": "User",
                    "count": 1,
                    "attributes": user_id,
                    "response": "User removed!"
                }
            },
            status_code=200
        )