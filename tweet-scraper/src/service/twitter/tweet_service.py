import tweepy
from ...models.twitter.user import TwitterUser
from ...models.twitter.tweet import Tweet


class TweetService:
    MAX_RESULTS_LIMIT = 100
    MAX_AVAILABLE_LIMIT = 3200

    def __init__(self, bearer_token):
        self.client = tweepy.Client(bearer_token)

    def get_users_available_tweets(self, user: TwitterUser) -> list[Tweet]:
        list_of_tweets = []
        tweet_count = user.tweet_count
        n_pages = tweet_count // self.MAX_RESULTS_LIMIT if tweet_count <= self.MAX_AVAILABLE_LIMIT else 33
        for response in tweepy.Paginator(self.client.get_users_tweets,
                                         user.user_id,
                                         max_results=self.MAX_RESULTS_LIMIT,
                                         limit=n_pages,
                                         tweet_fields="id,created_at,text,conversation_id,public_metrics"):
            for tweet in response.data:
                list_of_tweets.append(self._get_tweet_data(tweet))
        return list_of_tweets

    @staticmethod
    def _get_tweet_data(tweet: tweepy.Tweet) -> Tweet:
        return Tweet(id=tweet["id"],
                     created_at=tweet["created_at"],
                     text=tweet["text"],
                     conversation_id=tweet["conversation_id"],
                     retweet_count=tweet.data["public_metrics"]['retweet_count'],
                     reply_count=tweet.data["public_metrics"]['reply_count'],
                     like_count=tweet.data["public_metrics"]['like_count'],
                     quote_count=tweet.data["public_metrics"]['quote_count'],
                     impression_count=tweet.data["public_metrics"]['impression_count'])
