import requests

cookies = {
    'SL_G_WPT_TO': 'eo',
    'SL_GWPT_Show_Hide_tmp': '1',
    'SL_wptGlobTipTmp': '1',
    '_twitter_sess': 'BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCImzlKCIAToMY3NyZl9p%250AZCIlYzlmMzk3M2VmODM1NjgyNzNmNGI5NmM2ZTY1MzQ4OWY6B2lkIiUzZDNi%250AYTA5YTUyZjY3ZmE3YTg2MTAzZWJhOWRmOTY5ZQ%253D%253D--5747575e4718c3499a6e59d7fe2f92d4ced4d23f',
    'guest_id': 'v1%3A168632127987848740',
    'g_state': '{"i_l":0}',
    'kdt': 'x2Pg6FgRbQiaD5jyyqZlxkXnYTVwFRfZJmi20WGN',
    'auth_token': '21d2a34e709f8ab9748642044e527fe7e53c660d',
    'ct0': 'f314b1a42cfb097c5f40ef8e85692dba0160b06f05336baa9ee6ae7a669f2b1b87e884c01d5a719addd72275acf9340ed01d1c8bf3eb3a04cb20fcc267b89d3ada0fd846f2047253ce5541a6763acd30',
    'guest_id_ads': 'v1%3A168632127987848740',
    'guest_id_marketing': 'v1%3A168632127987848740',
    'lang': 'en',
    'twid': 'u%3D1667178445812498432',
    'personalization_id': '"v1_JKjny9QfpQsvRX17/V4EZA=="',
}

headers = {
    'authority': 'twitter.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'content-type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'SL_G_WPT_TO=eo; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCImzlKCIAToMY3NyZl9p%250AZCIlYzlmMzk3M2VmODM1NjgyNzNmNGI5NmM2ZTY1MzQ4OWY6B2lkIiUzZDNi%250AYTA5YTUyZjY3ZmE3YTg2MTAzZWJhOWRmOTY5ZQ%253D%253D--5747575e4718c3499a6e59d7fe2f92d4ced4d23f; guest_id=v1%3A168632127987848740; g_state={"i_l":0}; kdt=x2Pg6FgRbQiaD5jyyqZlxkXnYTVwFRfZJmi20WGN; auth_token=21d2a34e709f8ab9748642044e527fe7e53c660d; ct0=f314b1a42cfb097c5f40ef8e85692dba0160b06f05336baa9ee6ae7a669f2b1b87e884c01d5a719addd72275acf9340ed01d1c8bf3eb3a04cb20fcc267b89d3ada0fd846f2047253ce5541a6763acd30; guest_id_ads=v1%3A168632127987848740; guest_id_marketing=v1%3A168632127987848740; lang=en; twid=u%3D1667178445812498432; personalization_id="v1_JKjny9QfpQsvRX17/V4EZA=="',
    'referer': 'https://twitter.com/search?q=BITCOIN&src=typed_query&f=top',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'x-client-uuid': '08ed7dbe-0d2c-4fb4-91d7-412e4ea2c97d',
    'x-csrf-token': 'f314b1a42cfb097c5f40ef8e85692dba0160b06f05336baa9ee6ae7a669f2b1b87e884c01d5a719addd72275acf9340ed01d1c8bf3eb3a04cb20fcc267b89d3ada0fd846f2047253ce5541a6763acd30',
    'x-twitter-active-user': 'yes',
    'x-twitter-auth-type': 'OAuth2Session',
    'x-twitter-client-language': 'en',
}

params = {
    'variables': '{"rawQuery":"BITCOIN","count":20,"querySource":"typed_query","product":"Top"}',
    'features': '{"rweb_lists_timeline_redesign_enabled":true,"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":false,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":false,"responsive_web_enhance_cards_enabled":false}',
}

response = requests.get('https://twitter.com/i/api/graphql/IOJ89SDQ9IrZ2t7hSD4Fdg/SearchTimeline?variables=%7B%22rawQuery%22%3A%22BITCOIN%22%2C%22count%22%3A20%2C%22querySource%22%3A%22typed_query%22%2C%22product%22%3A%22Top%22%7D&features=%7B%22rweb_lists_timeline_redesign_enabled%22%3Atrue%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22tweetypie_unmention_optimization_enabled%22%3Atrue%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22graphql_is_translatable_rweb_tweet_is_translatable_enabled%22%3Atrue%2C%22view_counts_everywhere_api_enabled%22%3Atrue%2C%22longform_notetweets_consumption_enabled%22%3Atrue%2C%22tweet_awards_web_tipping_enabled%22%3Afalse%2C%22freedom_of_speech_not_reach_fetch_enabled%22%3Atrue%2C%22standardized_nudges_misinfo%22%3Atrue%2C%22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled%22%3Afalse%2C%22longform_notetweets_rich_text_read_enabled%22%3Atrue%2C%22longform_notetweets_inline_media_enabled%22%3Afalse%2C%22responsive_web_enhance_cards_enabled%22%3Afalse%7D', params=params, cookies=cookies, headers=headers)

print(response.status_code)
json_package = response.json()