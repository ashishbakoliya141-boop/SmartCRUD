from backend.services.user_services import (
    create_user_service,
    fetch_all_users,
    fetch_user_by_id,
    update_user_service,
    delete_user_service,
)

def create_user_tool(db, user):
    return create_user_service(db, user)

def get_all_users_tool(db):
    return fetch_all_users(db)

def get_user_tool(db, user_id):
    return fetch_user_by_id(db, user_id)

def update_user_tool(db, user_id, user):
    return update_user_service(db=db, user_id=user_id, user_data=user)

# def partial_update_user_tool(db, user_id, user):
#     return partial_update_user_service(db=db, user_id=user_id, user_data=user)

def delete_user_tool(db, user_id):
    return delete_user_service(db=db, user_id=user_id)