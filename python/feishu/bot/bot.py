import json
import logging
import random
from pydantic import BaseModel
import requests

from feishu.bot.bot_utils import gen_sign
from utils import log


class Text(BaseModel):
    content: str = None
    tag: str = None


class Header(BaseModel):
    title: Text
    template: str = None


class Column(BaseModel):
    tag: str
    width: str
    weight: int
    elements: list
    vertical_align: str = None


class Action(BaseModel):
    tag: str
    text: Text
    url: str
    type: str
    value: object = None


class Element(BaseModel):
    tag: str
    text_align: str = None
    content: str = None
    flex_mode: str = None
    background_style: str = None
    horizontal_spacing: str = None
    columns: list[Column] = None
    actions: list[Action] = None
    elements: list['Element'] = None


class CardLink(BaseModel):
    url: str
    android_url: str = None
    ios_url: str = None
    pc_url: str = None


class Card(BaseModel):
    elements: list[Element]
    header: Header
    card_link: CardLink = None


class Msg(BaseModel):
    msg_type: str
    card: Card


def create_markdown_element(content):
    return Element(tag="markdown", text_align="left", content=content)


def create_markdown_center_element(content):
    return Element(tag="markdown", text_align="center", content=content)


def create_text_element(content):
    return Element(tag="plain_text", content=content)


def create_note_element(content):
    return Element(tag="note", elements=[create_text_element(content)])


def create_column(align, content):
    return Column(tag="column", width="weighted", weight=1, vertical_align=align,
                  elements=[create_markdown_element(content)])


def create_center_column(align, content):
    return Column(tag="column", width="weighted", weight=1, vertical_align=align,
                  elements=[create_markdown_center_element(content)])


def hr():
    return Element(tag="hr")


class FeishuColor:
    BLUE = "blue"
    WATHET = "wathet"
    TURQUOISE = "turquoise"
    GREEN = "green"
    YELLOW = "yellow"
    ORANGE = "orange"
    RED = "red"
    CARMINE = "carmine"
    VIOLET = "violet"
    GREY = "grey"
    DEFAULT = "default"


class FeishuMsg:
    def __init__(self, title, markdown, note, link=None, header_color=FeishuColor.DEFAULT):
        self.title = title
        self.markdown = markdown
        self.note = note
        self.link = link
        self.header_color = header_color

    def to_dict(self):
        return {
            "title": self.title,
            "markdown": self.markdown,
            "note": self.note,
            "link": self.link,
            "header_color": self.header_color,
            # Since HeaderColor is not serialized in JSON, we don't include it here
        }


def format_msg(feishu_msg):
    elements = []
    md = ""
    for k, v in feishu_msg.markdown.items():
        md += f"**{k}**：{v}\n"
    elements.append(create_markdown_element(md))

    if feishu_msg.note:
        emoji = ["👍", "👏", "👌", "👊", "✌", "👋", "👆", "👇", "👈", "👉", "👎", "👓", "👔", "👕", "👖", "👗", "👘", "👙",
                 "👚", "👛", "👜", "👝", "👞", "👟", "👠", "👡", "👢", "👣", "👤", "👥", "👦", "👧", "👨", "👩", "👪", "👫",
                 "👬", "👭", "👮", "👯", "👰", "👱", "👲", "👳", "👴", "👵", "👶", "👷", "👸", "👹", "👺", "👻", "👼", "👽",
                 "👾", "👿", "💀", "💁", "💂", "💃", "💄", "💅", "💆", "💇", "💈", "💉", "💊", "💋", "💌", "💍", "💎", "💏",
                 "💐", "💑", "💒", "💓", "💔", "💕", "💖", "💗", "💘", "💙", "💚", "💛", "💜", "💝", "💞", "💟", "💠", "💡",
                 "💢", "💣", "💤", "💥", "💦", "💧", "💨", "💩", "💪", "💫", "💬", "💭", "💮", "💯", "💰", "💱", "💲", "💳",
                 "💴", "💵"]
        emoji_index = random.randint(0, len(emoji) - 1)
        elements.append(create_note_element(emoji[emoji_index] + feishu_msg.note + emoji[emoji_index]))

    return Msg(msg_type="interactive",
               card=Card(elements=elements,
                         header=Header(title=Text(content=feishu_msg.title, tag="plain_text"),
                                       template=str(feishu_msg.header_color)
                                       ),
                         card_link=CardLink(url=feishu_msg.link) if feishu_msg.link else None))


def send_feishu_msg(hook, feishu_msg, secret=None):
    try:
        if not hook:
            raise ValueError("error hook url")
        msg = format_msg(feishu_msg)
        data = msg.model_dump_json()
        feishu_json_msg: dict = json.loads(data)
        if secret is not None:
            sign = gen_sign(secret)
            feishu_json_msg.update(sign)

        response = requests.post(hook, json=feishu_json_msg, headers={"Content-Type": "application/json"})
        res = response.json()
        if response.status_code == 200 and res['statusCode'] == 200:
            data = res['data']
            log.info(data)
            return data
        else:
            log.info(f'{res["statusCode"]} => {res["comments"]}')
            return None
    except Exception as e:
        log.error("send_feishu_msg error", e)
        return None


def __test_json__():
    # 创建一个 Msg 实例
    text = Text(content="Some text", tag="plain_text")
    header = Header(title=text)
    card_link = CardLink(url="https://example.com")
    element = Element(tag="markdown", content="Some markdown content")
    card = Card(elements=[element], header=header, card_link=card_link)
    msg = Msg(msg_type="interactive", card=card)

    # 序列化
    # serialized_data = msg.json()
    serialized_data = msg.model_dump_json()
    print(serialized_data)

    # 反序列化
    data = '{"msg_type":"interactive","card":{"elements":[{"tag":"markdown","content":"Some other markdown content"}],"header":{"title":{"content":"Another text","tag":"plain_text"}},"card_link":{"url":"https://another-example.com"}}}'
    deserialized_data = Msg.parse_raw(data)
    print(deserialized_data)


if __name__ == '__main__':
    __test_json__()
