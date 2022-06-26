from enum import Enum
from typing import Optional, List


class ContentLicense(Enum):
    CC_BY_SA_40 = "CC BY-SA 4.0"


class UserType(Enum):
    REGISTERED = "registered"


class Owner:
    account_id: int
    reputation: int
    user_id: int
    user_type: UserType
    profile_image: str
    display_name: str
    link: str
    accept_rate: Optional[int]

    def __init__(self, account_id: int, reputation: int, user_id: int, user_type: UserType, profile_image: str, display_name: str, link: str, accept_rate: Optional[int]) -> None:
        self.account_id = account_id
        self.reputation = reputation
        self.user_id = user_id
        self.user_type = user_type
        self.profile_image = profile_image
        self.display_name = display_name
        self.link = link
        self.accept_rate = accept_rate


class ExternalLink:
    type: str
    link: str

    def __init__(self, type: str, link: str) -> None:
        self.type = type
        self.link = link


class PostedByCollective:
    tags: List[str]
    external_links: List[ExternalLink]
    description: str
    link: str
    name: str
    slug: str

    def __init__(self, tags: List[str], external_links: List[ExternalLink], description: str, link: str, name: str, slug: str) -> None:
        self.tags = tags
        self.external_links = external_links
        self.description = description
        self.link = link
        self.name = name
        self.slug = slug


class Answer:
    owner: Owner
    is_accepted: bool
    score: int
    last_activity_date: int
    creation_date: int
    answer_id: int
    question_id: int
    content_license: ContentLicense
    last_edit_date: Optional[int]
    posted_by_collectives: Optional[List[PostedByCollective]]

    def __init__(self, owner: Owner, is_accepted: bool, score: int, last_activity_date: int, creation_date: int, answer_id: int, question_id: int, content_license: ContentLicense, last_edit_date: Optional[int], posted_by_collectives: Optional[List[PostedByCollective]]) -> None:
        self.owner = owner
        self.is_accepted = is_accepted
        self.score = score
        self.last_activity_date = last_activity_date
        self.creation_date = creation_date
        self.answer_id = answer_id
        self.question_id = question_id
        self.content_license = content_license
        self.last_edit_date = last_edit_date
        self.posted_by_collectives = posted_by_collectives


class Result:
    Answers: List[Answer]
    has_more: bool
    quota_max: int
    quota_remaining: int

    def __init__(self, Answers: List[Answer], has_more: bool, quota_max: int, quota_remaining: int) -> None:
        self.Answers = Answers
        self.has_more = has_more
        self.quota_max = quota_max
        self.quota_remaining = quota_remaining
