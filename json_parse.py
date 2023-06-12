from jsonsearch import JsonSearch

#unnecessary_path = ['user_mentions', 'features', 'professional']
extra_counter = 0 # to reduce the extra userid caused by extend entities from json file

def parse(json_package):
    global id_path
    decoded_json = JsonSearch(object=json_package, mode='j')
    results = []
    #account_created_times = decoded_json.search_all_value(key='created_at')    #might be included if there is a way to bind it with user
    #descriptions = decoded_json.search_all_value(key='description')            #same with above
    follower_counts = decoded_json.search_all_value(key='followers_count')
    friends_counts = decoded_json.search_all_value(key='friends_count')
    locations = decoded_json.search_all_value(key='location')
    #names = decoded_json.search_all_value(key='name') #not necessary if you already got the userid
    user_ids = decoded_json.search_all_value(key='screen_name')
    id_path = decoded_json.search_all_path(key="screen_name")
    print(f"len of userid is {len(user_ids)}")
    
    #print(f"len of account_created_times is {len(account_created_times)}")
    #print(f"len of descriptions is {len(descriptions)}")
    print(f"len of follower_counts is {len(follower_counts)}")
    print(f"len of friends_counts is {len(friends_counts)}")
    print(f"len of locations is {len(locations)}")
    #print(f"len of names is {len(names)}")

    

    # still needs to remove duplicate and link media with user's account
        #possible solution: search json with entryID to seperate each tweet and search each media type within
        #the tweet to look for desired type of media and also record the userid linked with it.
        #OR just use enumerate function and check if the type of the media is what we need.
    
    # tweet_media_link = decoded_json.search_all_value(key='media_url_https')
    # tweet_media_type = decoded_json.search_all_value(key='type')
    # tweet_hashtag = decoded_json.search_all_value(key='hashtag')
    # tweet_text = decoded_json.search_all_value(key='text')
    
    # Infinite scroll(waiting for implement)
    # value = decoded_json.search_all_value(key='value')
    
    for idx, user_id in enumerate(user_ids):
        global extra_counter
        user_id = user_ids[idx]
        print(f"user_id is {user_id}")
        print(f"current idx is {idx}")
        print(f"current extra counter is {extra_counter}")
        current_path = id_path[idx]
        print(f"current_path is {current_path}")
        if 'user_results' not in current_path:
            extra_counter += 1
            continue
        url = f"https://www.twitter.com/{user_id}"
        #already_exit = duplicate_user_filter(user_id)   #waiting for implement
        
        #account_created_time = account_created_times[idx]
        #description = descriptions[idx]
        follower_count = follower_counts[idx-extra_counter]
        friends_count = friends_counts[idx-extra_counter]
        location = locations[idx-extra_counter]
        print(f"locaiton is {location}")
        #name = names[idx]

        result = [user_id, url, location, follower_count, friends_count]
        results.append(result)

    return results
    