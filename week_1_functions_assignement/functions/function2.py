def build_profile(first, last, age, career, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    user_info['Age'] = age
    user_info['Career'] = career
    return user_info
    
    
    print(**user_info)