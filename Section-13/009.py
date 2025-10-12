# self referencing models, or recursive models in pydantic
from pydantic import BaseModel
from typing import List, Optional

class Comment(BaseModel):
    id : int
    content : str
    replies : Optional[List['Comment']] = None # self referencing model, replies can be a list of comments or none

# required after defining a self referencing model - otherwise crazy amount of performance degradation
Comment.model_rebuild()

comment = Comment(
    id=1,
    content="First comment",
    replies=[
        Comment(id=2, content="Reply-1"),
        Comment(id=3, content="Reply-2", replies=[
            Comment(id=4, content="Nested Reply"),
        ]),
    ]
)

print(comment)