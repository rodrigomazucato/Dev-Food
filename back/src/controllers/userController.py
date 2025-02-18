from models.user import User, users

def create_user(data):
    print(f'Formato do data: {data}')
    new_user = User(
        id=len(users) + 1, 
        name=data['name'], 
        email=data['email'], 
        password = data['password']
        )
    users.append(new_user)
    return { "message": "User created successfully", "id": new_user.id}, 201

def get_users():
    return {"users":[{"id":u.id, "name":u.name, "email": u.email} for u in users ]}, 200

def get_user_id(id):
    for i in users:
        if i["id"] == id:
            return i
        return "Error: User not found..."