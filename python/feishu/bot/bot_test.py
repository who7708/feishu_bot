import unittest
import bot


# class TestFeishuMsg(unittest.TestCase):
#     def setUp(self):
#         self.hook = 'https://open.feishu.cn/open-apis/bot/v2/hook/d807049e-b552-440c-9663-4d20cf57a36e'
#         self.feishu_msg = bot.FeishuMsg(
#             title="飞书markdown消息测试！",
#             markdown={
#                 "标题": "标题测试",
#                 "内容": "这是内容**粗体**, *斜体*, ~~删除线~~",
#                 "状态": "<font color='green'>成功</font> <font color='red'>失败</font> <font color='grey'>灰色</font>",
#                 "列表": "\n- 列表1\n- 列表2\n- 列表3",
#                 "链接": "[飞书机器人助手](https://www.feishu.cn/hc/zh-CN/articles/236028437163-%E6%9C%BA%E5%99%A8%E4%BA%BA%E6%B6%88%E6%81%AF%E5%86%85%E5%AE%B9%E6%94%AF%E6%8C%81%E7%9A%84%E6%96%87%E6%9C%AC%E6%A0%B7%E5%BC%8F)",
#                 "时间": "2021-08-12 12:00:00",
#             },
#             note="这是备注",
#             link="http://www.baidu.com",
#             header_color="wathet",
#         )
#
#     def test_send_txt(self):
#         response = bot.send_feishu_msg(self.hook, self.feishu_msg)
#         # 可以根据实际情况调整断言，比如检查响应状态码等
#         self.assertIsNotNone(response)

class TestFeishuMsg2(unittest.TestCase):
    def setUp(self):
        # self.hook = 'https://open.feishu.cn/open-apis/bot/v2/hook/d807049e-b552-440c-9663-4d20cf57a36e'
        # 未知飞书
        self.hook = 'https://open.feishu.cn/open-apis/bot/v2/hook/691c4ccc-3df7-4d87-8806-82754c5bb7b1'
        self.secret = '9D3KqlZtKhAzyVu0ITPdSe'
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

    def test_send_txt(self):
        response = bot.send_feishu_msg(self.hook, self.feishu_msg)
        # 可以根据实际情况调整断言，比如检查响应状态码等
        self.assertIsNotNone(response)


if __name__ == '__main__':
    unittest.main()
