import datetime
from pydantic import BaseModel


class Tweet(BaseModel):
    id: str
    created_at: datetime.datetime
    text: str
    conversation_id: int
    retweet_count: int
    reply_count: int
    like_count: int
    quote_count: int
    impression_count: int
