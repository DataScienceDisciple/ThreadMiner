import pandas as pd

from ...models.twitter.tweet import Tweet
from ...models.twitter.user import TwitterUser


class ThreadUtil:
    def __init__(self, user: TwitterUser, tweets_api: list[Tweet]):
        self.user = user
        self.tweets_api = tweets_api

    def get_users_threads_from_api(self) -> list[Tweet]:
        thread_candidates = []
        for tweet in self.tweets_api:
            if not tweet.text.startswith("RT @") and not tweet.text.startswith("@"):
                thread_candidates.append(tweet)
        return thread_candidates

    @staticmethod
    def convert_tweets_to_df(tweets: list[Tweet]) -> pd.DataFrame:
        return pd.DataFrame([tweet.dict() for tweet in tweets])
