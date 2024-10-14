import bot
from utils import log


class TestFeishuMsg:
    def __init__(self):
        ## 测试morefun企业群
        ### Webhook 测试
        # self.hook = 'https://open.feishu.cn/open-apis/bot/v2/hook/d807049e-b552-440c-9663-4d20cf57a36e'
        ### 核验数据推送
        # self.hook = 'https://open.feishu.cn/open-apis/bot/v2/hook/a03e7932-afea-4016-9a48-d5d3df8c8225'
        # self.secret = 'WVQq6SALYyYtxcrwTKhXRe'
        # 公司
        ## 测试群
        ### 测试机器人
        self.hook = 'https://open.feishu.cn/open-apis/bot/v2/hook/e194583c-f213-4141-8511-c12bb8919b66'

        # # 未知飞书
        # self.hook = 'https://open.feishu.cn/open-apis/bot/v2/hook/691c4ccc-3df7-4d87-8806-82754c5bb7b1'
        self.feishu_msg = bot.FeishuMsg(
            title="飞书消息测试！",
            markdown={
                "标题": "测试，请忽略",
                "内容": "这是内容**粗体**, *斜体*, ~~删除线~~",
                # "状态": "<font color='green'>成功</font> <font color='red'>失败</font> <font color='grey'>灰色</font>",
                # "列表": "\n- 列表1\n- 列表2\n- 列表3",
                # "链接": "[飞书机器人助手](https://www.feishu.cn/hc/zh-CN/articles/236028437163-%E6%9C%BA%E5%99%A8%E4%BA%BA%E6%B6%88%E6%81%AF%E5%86%85%E5%AE%B9%E6%94%AF%E6%8C%81%E7%9A%84%E6%96%87%E6%9C%AC%E6%A0%B7%E5%BC%8F)",
                # "时间": "2021-08-12 12:00:00",
            },
            note="这是备注",
            link="#",
            header_color=bot.FeishuColor.WATHET,
        )

    def send_data(self):
        response = bot.send_feishu_msg(self.hook, self.feishu_msg)
        log.info(response)


if __name__ == '__main__':
    feishu_msg = TestFeishuMsg()
    feishu_msg.send_data()
