import tweepy
from ...models.twitter.user import TwitterUser


class UserService:
    def __init__(self, bearer_token: str) -> None:
        self.client = tweepy.Client(bearer_token)

    def get_user(self, username: str, user_fields: str = "public_metrics") -> TwitterUser:
        user = self.client.get_user(username=username, user_fields=user_fields)
        return TwitterUser(user_id=user.data.id,
                           username=user.data.username,
                           followers_count=user.data.public_metrics["followers_count"],
                           following_count=user.data.public_metrics["following_count"],
                           tweet_count=user.data.public_metrics["tweet_count"],
                           listed_count=user.data.public_metrics["listed_count"]
                           )
