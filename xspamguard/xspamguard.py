import requests as req
import json
import argparse

#########################################################
#                   Constants                           #
#########################################################
bred='\033[1;31m'
bblue='\033[1;34m'
bgreen='\033[1;32m'
yellow='\033[0;33m'
red='\033[0;31m'
blue='\033[0;34m'
green='\033[0;32m'
reset='\033[0m'
mode=""
blocklist=[]
mutelist=[]
spammerlist=[]
mutelistfetched=False
blocklistfetched=False
cookie_dict={}
spammer1={}
csrf_token=""
auth_token=""
spammerlist_url="https://raw.githubusercontent.com/rohsec/X-SpamWatch/main/spammers.json"
validator_url="https://x.com/i/api/1.1/users/email_phone_info.json"
mutelist_url = "https://twitter.com:443/i/api/graphql/iHyidEotn1CK7l0M3WgbZA/MutedAccounts?variables=%7B%22count%22%3A200%2C%22includePromotedContent%22%3Afalse%7D&features=%7B%22rweb_tipjar_consumption_enabled%22%3Atrue%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Atrue%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22communities_web_enable_tweet_community_results_fetch%22%3Atrue%2C%22c9s_tweet_anatomy_moderator_badge_enabled%22%3Atrue%2C%22articles_preview_enabled%22%3Atrue%2C%22tweetypie_unmention_optimization_enabled%22%3Atrue%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22graphql_is_translatable_rweb_tweet_is_translatable_enabled%22%3Atrue%2C%22view_counts_everywhere_api_enabled%22%3Atrue%2C%22longform_notetweets_consumption_enabled%22%3Atrue%2C%22responsive_web_twitter_article_tweet_consumption_enabled%22%3Atrue%2C%22tweet_awards_web_tipping_enabled%22%3Afalse%2C%22creator_subscriptions_quote_tweet_preview_enabled%22%3Afalse%2C%22freedom_of_speech_not_reach_fetch_enabled%22%3Atrue%2C%22standardized_nudges_misinfo%22%3Atrue%2C%22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled%22%3Atrue%2C%22rweb_video_timestamps_enabled%22%3Atrue%2C%22longform_notetweets_rich_text_read_enabled%22%3Atrue%2C%22longform_notetweets_inline_media_enabled%22%3Atrue%2C%22responsive_web_enhance_cards_enabled%22%3Afalse%7D"
mute_url = "https://x.com:443/i/api/1.1/mutes/users/create.json"
blocklist_url="https://x.com/i/api/graphql/dNoJPVzyST-SELg82IaNZg/BlockedAccountsAll?variables=%7B%22count%22%3A20%2C%22includePromotedContent%22%3Afalse%2C%22withSafetyModeUserFields%22%3Afalse%7D&features=%7B%22rweb_tipjar_consumption_enabled%22%3Atrue%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Atrue%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22communities_web_enable_tweet_community_results_fetch%22%3Atrue%2C%22c9s_tweet_anatomy_moderator_badge_enabled%22%3Atrue%2C%22articles_preview_enabled%22%3Atrue%2C%22tweetypie_unmention_optimization_enabled%22%3Atrue%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22graphql_is_translatable_rweb_tweet_is_translatable_enabled%22%3Atrue%2C%22view_counts_everywhere_api_enabled%22%3Atrue%2C%22longform_notetweets_consumption_enabled%22%3Atrue%2C%22responsive_web_twitter_article_tweet_consumption_enabled%22%3Atrue%2C%22tweet_awards_web_tipping_enabled%22%3Afalse%2C%22creator_subscriptions_quote_tweet_preview_enabled%22%3Afalse%2C%22freedom_of_speech_not_reach_fetch_enabled%22%3Atrue%2C%22standardized_nudges_misinfo%22%3Atrue%2C%22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled%22%3Atrue%2C%22rweb_video_timestamps_enabled%22%3Atrue%2C%22longform_notetweets_rich_text_read_enabled%22%3Atrue%2C%22longform_notetweets_inline_media_enabled%22%3Atrue%2C%22responsive_web_enhance_cards_enabled%22%3Afalse%7D"
block_url="https://x.com/i/api/1.1/blocks/create.json"


def logo():
    print(f"""╔════════════════════════════════════════════════════════╗
{green} _  _    ____ ___  ____ _  _    ____ _  _ ____ ____ ___  
  \/  __ [__  |__] |__| |\/|    | __ |  | |__| |__/ |  \ 
 _/\_    ___] |    |  | |  |    |__] |__| |  | |  \ |__/                                           
{yellow}     ======= {blue}X(Twitter) Mass Muter/Blocker{yellow} ======{reset}                                                                
{yellow}  Creator: {bblue}https://x.com/rohsec {yellow}[ {bred}@rohsec {yellow}]{reset}
{yellow}  Coffee: {bblue}https://ko-fi.com/rohsec{reset}                    
╚════════════════════════════════════════════════════════╝""")
def usage():
    print("Usage:\n")

def requestutils(cookiefile,token):
    global csrf_token,auth_token
    auth_token=token
    print(f"{yellow}[ {green}+ {yellow}]{blue} Extracting CSRF Token from cookie files...{yellow}({green}✔{yellow}){reset}")
    f1=open(f"{cookiefile}","r")
    cookie=f1.read()
    f1.close()
    cookies=cookie.strip().split('; ')
    for i in cookies:
        if i.startswith('ct0='):
            csrf_token=i[4:]
        key,value=i.split("=",1)
        cookie_dict[key]=value
    print(f"{yellow}[ {green}+ {yellow}]{blue} Formating Cookies to required format...{yellow}({green}✔{yellow}){reset}")
    # print(f"Cookies : {cookie_dict}")
    print(f"{yellow}[ {green}+ {yellow}]{blue} Finally, setting up required headers...{yellow}({green}✔{yellow}){reset}")

def spammerlist_fetcher():
    print(f"{yellow}[ {green}+ {yellow}]{blue} Fetching known spammers list....{yellow}({green}✔{yellow}){reset}")
    resp=req.get(spammerlist_url)
    if(resp.status_code==200):
        respjson=json.loads(resp.content)
        for i in respjson['spammers']:
            spammerlist.append(i['rest_id'])
            spammer1[i['rest_id']]=i['username']
        print(f"{yellow}[ {blue}* {yellow}]{blue} Spammers list fetched successfully !!{reset}")
        print(f"╔════════════════════════════════════════════════════════╗\n {bgreen} Spammer Count: {bred}{len(spammerlist)}{reset}\n╚════════════════════════════════════════════════════════╝")
        return True
    else:
        print(f"{yellow}[ {red}! {yellow}]{blue}Unable to fetch the known spammers list at the moment !!{reset}")
        return False

    

def cred_validator():
    print(f"{yellow}[ {green}+ {yellow}]{blue} Validating user credentials...{yellow}({green}✔{yellow}){reset}")
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://twitter.com/settings/", "Content-Type": "application/json", "X-Twitter-Auth-Type": "OAuth2Session", "X-Csrf-Token": f"{csrf_token}", "X-Twitter-Client-Language": "en", "X-Twitter-Active-User": "yes", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Authorization": f"Bearer {auth_token}", "Te": "trailers"}
    resp=req.get(validator_url,headers=headers,cookies=cookie_dict)
    if(resp.status_code==200):
        respjson=json.loads(resp.content)
        print(f"╔════════════════════════════════════════════════════════╗\n {bgreen} Active User: {bred}{respjson['emails'][0]['email']}{reset}\n╚════════════════════════════════════════════════════════╝")
        print(f"{yellow}[ {blue}* {yellow}]{blue} User validated successfully !!{reset}")
        return True
    else:
        print(f"{yellow}[ {red}! {yellow}]{blue} Invalid User !! Make sure the supplied credentials are valid{reset}")
        return False


def blocklist_fetcher():
    global blocklistfetched
    print(f"{yellow}[ {green}+ {yellow}]{blue} Fetching your active block list....{yellow}({green}✔{yellow}){reset}")
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://twitter.com/settings/", "Content-Type": "application/json", "X-Twitter-Auth-Type": "OAuth2Session", "X-Csrf-Token": f"{csrf_token}", "X-Twitter-Client-Language": "en", "X-Twitter-Active-User": "yes", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Authorization": f"Bearer {auth_token}", "Te": "trailers"}
    resp=req.get(blocklist_url, headers=headers, cookies=cookie_dict)
    if(resp.status_code==200):
        respjson=json.loads(resp.content)
        for i in respjson['data']['viewer']['timeline']['timeline']['instructions'][3]['entries']:
            if(i['entryId'].startswith('user')):
                blocked_user=i['content']['itemContent']['user_results']['result']['rest_id']
                blocklist.append(blocked_user)
        # print(f"\n\nDebug :::: \n {blocklist} \n::::\n\n")
        print(f"╔════════════════════════════════════════════════════════╗\n {bgreen} Current Block count: {bred}{len(blocklist)}{reset}\n╚════════════════════════════════════════════════════════╝")
        blocklistfetched=True
        print(f"{yellow}[ {blue}* {yellow}]{blue} Already blocked users successfully fetched !!{reset}")
    else:
        print(f"{yellow}[ {red}! {yellow}]{blue} There was an issue when fetching your currently blocked users. Please try after sometime.{reset}")


def blocker(csrf_token):
    success=0
    print(f"{yellow}[ {green}+ {yellow}]{blue} Starting Mass Block Operation...{yellow}({green}✔{yellow}){reset}")
    print("╔════════════════════════════════════════════════════════╗")
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://twitter.com/settings/", "Content-Type": "application/x-www-form-urlencoded", "X-Twitter-Auth-Type": "OAuth2Session", "X-Csrf-Token": f"{csrf_token}", "X-Twitter-Client-Language": "en", "X-Twitter-Active-User": "yes", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Authorization": f"Bearer {auth_token}", "Te": "trailers"}
    for i in spammerlist:
        if(str(i) not in blocklist):
            burp0_data = {"user_id": f"{i}"}
            resp=req.post(block_url, headers=headers, cookies=cookie_dict, data=burp0_data)
            if(resp.status_code==200):
                success=success+1
                print(f"{green}  User {red}{spammer1[i]}{green} blocked successfully{reset}")
            else:
                print(f"{red}  Unable to block {yellow}{spammer1[i]}{red}{reset}")
        else:
            print(f"{green}  User {red}{spammer1[i]}{green} is already blocked (skipping){reset}")
    print("╚════════════════════════════════════════════════════════╝")
    print(f"{yellow}[ {blue}* {yellow}]{blue} Blocker Function Finished !!{reset}")
    print(f"{yellow}[ {blue}* {yellow}]{blue} A total of {bred}{success}{blue} engagement spammers blocked{reset}")
    print("════════════════════════════════════════════════════════")

def mutelist_fetcher():
    global mutelistfetched
    print(f"{yellow}[ {green}+ {yellow}]{blue} Fetching your active mute list....{yellow}({green}✔{yellow}){reset}")
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://twitter.com/settings/", "Content-Type": "application/json", "X-Twitter-Auth-Type": "OAuth2Session", "X-Csrf-Token": f"{csrf_token}", "X-Twitter-Client-Language": "en", "X-Twitter-Active-User": "yes", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Authorization": f"Bearer {auth_token}", "Te": "trailers"}
    resp=req.get(mutelist_url, headers=headers, cookies=cookie_dict)
    if(resp.status_code==200):
        respjson=json.loads(resp.content)
        for i in respjson['data']['viewer']['muting_timeline']['timeline']['instructions'][3]['entries']:
            if(i['entryId'].startswith('user')):
                muted_user=i['content']['itemContent']['user_results']['result']['rest_id']
                mutelist.append(muted_user)
        print(f"╔════════════════════════════════════════════════════════╗\n {bgreen} Current Mute count: {bred}{len(mutelist)}{reset}\n╚════════════════════════════════════════════════════════╝")
        mutelistfetched=True
        print(f"{yellow}[ {blue}* {yellow}]{blue} Already muted users successfully fetched !!{reset}")
        
    else:
        print(f"{yellow}[ {red}! {yellow}]{blue} There was an issue when fetching your currently muted users. Please try after sometime.{reset}")


def muter(csrf_token):
    success=0
    print(f"{yellow}[ {green}+ {yellow}]{blue} Starting Mass Mute Operation...{yellow}({green}✔{yellow}){reset}")
    print("╔════════════════════════════════════════════════════════╗")
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://twitter.com/settings/", "Content-Type": "application/x-www-form-urlencoded", "X-Twitter-Auth-Type": "OAuth2Session", "X-Csrf-Token": f"{csrf_token}", "X-Twitter-Client-Language": "en", "X-Twitter-Active-User": "yes", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Authorization": f"Bearer {auth_token}", "Te": "trailers"}
    for i in spammerlist:
        if(i not in mutelist):
            burp0_data = {"user_id": f"{i}"}
            resp=req.post(mute_url, headers=headers, cookies=cookie_dict, data=burp0_data)
            if(resp.status_code==200):
                success=success+1
                print(f"{green}  User {red}{spammer1[i]}{green} muted successfully{reset}")
            else:
                print(f"{red}  Unable to mute {yellow}{spammer1[i]}{red}{reset}")
        else:
            print(f"{green}  User {red}{spammer1[i]}{green} is already muted (skipping){reset}")
    print("╚════════════════════════════════════════════════════════╝")
    print(f"{yellow}[ {blue}* {yellow}]{blue} Muter Function Finished !!{reset}")
    print(f"{yellow}[ {blue}* {yellow}]{blue} A total of {bred}{success}{blue} engagement spammers muted{reset}")
    print("════════════════════════════════════════════════════════")

def core(cookiefile,token,mode):
    requestutils(cookiefile,token)
    userValidated=cred_validator()
    if(userValidated):
        spammerlist_fetched=spammerlist_fetcher()
        if(spammerlist_fetched):
            if(mode=="mute"):
                mutelist_fetcher()
                if(mutelistfetched):
                    muter(csrf_token)
                else:
                    print(f"{yellow}[ {red}! {yellow}]{blue} Already Muted User List not available, please try again after sometime !!{reset}")
            else:
                blocklist_fetcher()
                if(blocklistfetched):
                    blocker(csrf_token)
                else:
                    print(f"{yellow}[ {red}! {yellow}]{blue} Already Blocked User List not available, please try again after sometime !!{reset}")
        else:
            print(f"{yellow}[ {red}! {yellow}]{blue} There was an issue fetching the known spammers list, please try again after sometime !!{reset}")
    else:
        print(f"{yellow}[ {red}! {yellow}]{blue} Invalid User!! Provide proper credentials !!{reset}")


    
        

################## Main Function #################################
def main():
    logo()
    parser=argparse.ArgumentParser(description="X(Twitter) Mass Spam Blocker")
    parser.add_argument('-m',"--mode",default="mute",help="Spam Fight Mode (default: mute)",choices=["mute","block"])
    parser.add_argument('-c', "--cookie", help="File containing valid cookies", required=True,dest="c")
    parser.add_argument('-t', "--token",help="Your Auth Bearer token",required=True)
    args = parser.parse_args()
    core(args.c,args.token,args.mode)


############## SCRIPT START ######################3
# if __name__ == "__main__":
#     main()
