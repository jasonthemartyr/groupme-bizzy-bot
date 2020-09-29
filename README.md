## Requirements:

- [PRAW](https://praw.readthedocs.io/en/latest/) Reddit API wrapper
- [Groupy](https://groupy.readthedocs.io/en/v0.10.0/index.html) GroupMe SDK
- Python3.*
- Python packages defined in `requirements.txt`

## GroupMe Auth token

grab auth token with:

`https://dev.groupme.com/tutorials/oauth`

get group ID:

```bash
curl https://api.groupme.com/v3/groups?token=$token
```

## Reddit Auth token

- https://praw.readthedocs.io/en/latest/getting_started/authentication.html


- https://www.reddit.com/prefs/apps/
