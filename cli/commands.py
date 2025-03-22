from core.user_service import UserService
from core.listing_service import ListingService
from core.category_service import CategoryService
from data.db import Database
import re

db = Database()
user_service = UserService(db)
listing_service = ListingService(db)
category_service = CategoryService(db)

def process_command(cmd):

    pattern = r"'([^']*)'|([^'\s]+)"
    matches = re.findall(pattern, cmd)
    args = [match[0] if match[0] else match[1] for match in matches]

    action = args[0].upper()
    username = args[1]

    if action == "REGISTER" and len(args) == 2:
        return user_service.register_user(username)

    elif action == "CREATE_LISTING" and len(args) == 6:
        title = args[2]
        description = args[3]
        price = int(args[4])
        category = args[5]
        return listing_service.create_listing(username, title, description, price, category)

    elif action == "DELETE_LISTING" and len(args) == 3:
        listing_id = int(args[2])
        return listing_service.delete_listing(username, listing_id)

    elif action == "GET_LISTING" and len(args) == 3:
        listing_id = int(args[2])
        return listing_service.get_listing(username, listing_id)

    elif action == "GET_CATEGORY" and len(args) == 3:
        category = args[2]
        return category_service.get_category(username, category)

    elif action == "GET_TOP_CATEGORY" and len(args) == 2:
        return category_service.get_top_category(username)

    return "Error - unknown command"
