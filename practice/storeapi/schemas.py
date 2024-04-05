from pydantic import BaseModel, ConfigDict


class CommentIn(BaseModel):
    body: str


class Comment(CommentIn):
    model_config = ConfigDict(from_attributes=True)
    id: int
    post_id: int


class UserPostIn(BaseModel):
    body: str


class UserPost(UserPostIn):
    model_config = ConfigDict(from_attributes=True)

    id: int
    comments: list[Comment] = []


# class UserPostWithComments(BaseModel):
#     id: int
#     post: UserPost
#     comments: list[Comment] = []

#     model_config = ConfigDict(from_attributes=True)
