import praw, requests, re, tempfile

from groupy import Client
from groupy import attachments

def client_obj(token):
    return Client.from_token(token)

def group_obj(client_obj, group_id):
    groups = client_obj.groups
    return groups.get(group_id) #get id with curl

def get_messages(group_obj): #this returns a list for messages, use a for loop to iterate over them
    output = []
    for message in group_obj.messages.list_all():
        output.append(message.text)
    return output

def send_message(group_obj, message): #this returns a list for messages, use a for loop to iterate over them
    new_message = group_obj.post(text=message)
    return new_message

def upload_image(client_obj,group_obj, filename, message):
    with open(filename, 'rb') as f:
        image = client_obj.images.from_file(f)
        # image = client.images.upload(f)
        upload = group_obj.post(text=message,attachments=[image])
        return upload

def reddit_client(client_id, client_secret, password, user_agent, username):
    reddit = praw.Reddit(client_id=client_id,
                        client_secret=client_secret,
                        password=password,
                        user_agent=user_agent,
                        username=username)
    return reddit

def get_subreddit_posts(reddit_obj, subreddit, post_count):
    output = {}
    subreddit = reddit_obj.subreddit(subreddit)
    hot_python = subreddit.hot(limit=post_count)

    for submission in hot_python:
        if not submission.stickied:
            if '.gifv' not in submission.url: # filter out gifs (groupme upload does not like them)
                output[submission.title] = submission.url
    return output # returned output will be off if an image link is not found and if it contains .gifv

def main():

    dirpath = tempfile.mkdtemp()

    ##groupme stuff:
    token = 'MY_TOKEN'
    group_id = 'MY_GROUP_ID'
    client = client_obj(token)
    group = group_obj(client, group_id)

    ##reddit stuff:
    reddit = reddit_client(client_id="MY_CLIENT_ID",
                           client_secret="MY_CLIENT_SECRET",
                           password="MY_PASSWORD",
                           user_agent="testscript by u/MY_USERNAME",
                           username="MY_USERNAME"
                          )

    subreddit_posts = get_subreddit_posts(reddit, 'IllegallySmolCats', 3) # subreddit and number of posts to return go here

    ##iterate over subreddit_posts dictionary:
    for title, image_url in subreddit_posts.items():
        file_name = image_url.split('/')[-1]
        file_path = f'{dirpath}/{file_name}'
        pic_request = requests.get(image_url)
        if pic_request.status_code == 200:
            file = open(file_path, 'wb')
            file.write(pic_request.content)
            print(upload_image(client, group, file.name, title)) #upload files
main()
