import json
import random
from pydantic import BaseModel


class Msg:
    def __init__(self, msg_type, card):
        self.msg_type = msg_type
        self.card = card

    def to_dict(self):
        return {
            "msg_type": self.msg_type,
            "card": self.card,
        }


class Text:
    def __init__(self, content=None, tag=None):
        self.content = content
        self.tag = tag

    def to_dict(self):
        return {
            "content": self.content,
            "tag": self.tag,
        }


class Header:
    def __init__(self, title, template=None):
        self.title = title
        self.template = template

    def to_dict(self):
        return {
            "title": self.title,
            "template": self.template,
        }


class Card:
    def __init__(self, elements, header, card_link=None):
        self.elements = elements
        self.header = header
        self.card_link = card_link

    def to_dict(self):
        return {
            "elements": self.elements,
            "header": self.header,
            "card_link": self.card_link,
        }


class CardLink:
    def __init__(self, url, android_url=None, ios_url=None, pc_url=None):
        self.url = url
        self.android_url = android_url
        self.ios_url = ios_url
        self.pc_url = pc_url

    def to_dict(self):
        return {
            "url": self.url,
            "android_url": self.android_url,
            "ios_url": self.ios_url,
            "pc_url": self.pc_url,
        }


class Column:
    def __init__(self, tag, width, weight, elements, vertical_align=None):
        self.tag = tag
        self.width = width
        self.weight = weight
        self.elements = elements
        self.vertical_align = vertical_align

    def to_dict(self):
        return {
            "tag": self.tag,
            "width": self.width,
            "elements": self.elements,
            "vertical_align": self.vertical_align,
        }


class Action:
    def __init__(self, tag, text, url, typ, value):
        self.tag = tag
        self.text = text
        self.url = url
        self.type = typ
        self.value = value

    def to_dict(self):
        return {
            "tag": self.tag,
            "width": self.text,
            "url": self.url,
            "typ": self.type,
            "value": self.value,
        }


class Element:
    def __init__(self, tag, text_align=None, content=None, flex_mode=None, background_style=None,
                 horizontal_spacing=None, columns=None, actions=None, elements=None):
        self.tag = tag
        self.text_align = text_align
        self.content = content
        self.flex_mode = flex_mode
        self.background_style = background_style
        self.horizontal_spacing = horizontal_spacing
        self.columns = columns
        self.actions = actions
        self.elements = elements

    def to_dict(self):
        return {
            "tag": self.tag,
            "text_align": self.text_align,
            "content": self.content,
            "flex_mode": self.flex_mode,
            "background_style": self.background_style,
            "horizontal_spacing": self.horizontal_spacing,
            "columns": self.columns,
            "actions": self.actions,
            "elements": self.elements,
        }


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


def format_msg(f):
    elements = []
    md = ""
    for k, v in f.markdown.items():
        md += f"**{k}**：{v}\n"
    elements.append(create_markdown_element(md))

    if f.note:
        emoji = ["👍", "👏", "👌", "👊", "✌", "👋", "👆", "👇", "👈", "👉", "👎", "👓", "👔", "👕", "👖", "👗", "👘", "👙",
                 "👚", "👛", "👜", "👝", "👞", "👟", "👠", "👡", "👢", "👣", "👤", "👥", "👦", "👧", "👨", "👩", "👪", "👫",
                 "👬", "👭", "👮", "👯", "👰", "👱", "👲", "👳", "👴", "👵", "👶", "👷", "👸", "👹", "👺", "👻", "👼", "👽",
                 "👾", "👿", "💀", "💁", "💂", "💃", "💄", "💅", "💆", "💇", "💈", "💉", "💊", "💋", "💌", "💍", "💎", "💏",
                 "💐", "💑", "💒", "💓", "💔", "💕", "💖", "💗", "💘", "💙", "💚", "💛", "💜", "💝", "💞", "💟", "💠", "💡",
                 "💢", "💣", "💤", "💥", "💦", "💧", "💨", "💩", "💪", "💫", "💬", "💭", "💮", "💯", "💰", "💱", "💲", "💳",
                 "💴", "💵"]
        emoji_index = random.randint(0, len(emoji) - 1)
        elements.append(create_note_element(emoji[emoji_index] + f.note + emoji[emoji_index]))

    return Msg(msg_type="interactive",
               card=Card(elements=elements,
                         header=Header(title=Text(content=f.title, tag="plain_text"),
                                       template=str(f.header_color)
                                       ),
                         card_link=CardLink(url=f.link) if f.link else None))


def send_feishu_msg(hook, f):
    if not hook:
        raise ValueError("error hook url")

    msg = format_msg(f)
    data = json.dumps(msg.to_dict())

    import requests
    response = requests.post(hook, data=data, headers={"Content-Type": "application/json"})
    return response
