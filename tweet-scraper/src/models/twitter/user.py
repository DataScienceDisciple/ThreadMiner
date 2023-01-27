from pydantic import BaseModel
from typing import Optional


class TwitterUser(BaseModel):
    user_id: int
    username: str
    followers_count: Optional[int]
    following_count: Optional[int]
    tweet_count: Optional[int]
    listed_count: Optional[int]
    # TODO: last_dump: datetime.datetime
