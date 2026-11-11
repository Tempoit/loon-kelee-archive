# 可莉 Loon 插件中心 · 全量源码归档

**来源**：[hub.kelee.one](https://hub.kelee.one)（作者 可莉🅥）  
**归档时间**：2026-11-12 00:50  
**规模**：275 个插件 · 102 个远程脚本/资源

## 这是什么

把 `hub.kelee.one` 插件中心里的**全部插件原文**抓下来归档，并做了两件事：

1. **规范化重写**：去 BOM、CRLF→LF、去行尾空白、压缩多余空行、统一以换行结尾 —— 文本等于重新写了一遍，原站以后加密/混淆也不影响这里的可读源码。
2. **依赖本地化**：插件里原本指向 `https://kelee.one/Resource/...` 的 198 处脚本/JQ/mock 资源全部改写为本仓库地址，**断网到上游也能离线安装使用**。

> 只改链接和空白，规则语义零改动（已用逐行 diff 校验 275 个文件全部一致）。

## 目录结构

```
plugins/     275 个 .lpx 插件（已规范化 + 链接本地化）
resources/   102 个被插件引用的 JS / jq / zip 资源
index.json   全量索引（名称、描述、标签、段落、规则数、sha256）
tools/       抓取与重写脚本（可自行刷新）
```

## 安装方式

Loon → 配置 → 插件 → 右上角 `+` → 添加外部插件，填入：

```
https://raw.githubusercontent.com/Yjwj205/loon-kelee-archive/main/plugins/<文件名>.lpx
```

只给原始 raw 链接（不用任何镜像 CDN）。

## 插件索引


### 去广告（254）

| 插件 | 说明 | 规则 | 脚本 | 文件 |
|---|---|---|---|---|
| 12306去广告 | 过滤12306应用内广告及开屏广告 | 0 | 1 | [12306_remove_ads.lpx](plugins/12306_remove_ads.lpx) |
| 123云盘去广告 | 移除开屏广告、应用内横幅广告。 | 0 | 0 | [123NetWorkDisk_remove_ads.lpx](plugins/123NetWorkDisk_remove_ads.lpx) |
| 两步路户外助手去广告 | 移除开屏广告、弹窗广告，精简我的页面。 | 0 | 0 | [2bulu_remove_ads.lpx](plugins/2bulu_remove_ads.lpx) |
| 360摄像机去广告 | 移除开屏广告、首页推广、底栏商城入口及我的页面推广。 | 2 | 0 | [360SmartCamera_remove_ads.lpx](plugins/360SmartCamera_remove_ads.lpx) |
| 36氪去广告 | 移除开屏广告、首页右上角运营位、信息流广告、文末广告，移除相关文章推荐、大家都在看及皮肤配置，精简搜索页… | 2 | 0 | [36Kr_remove_ads.lpx](plugins/36Kr_remove_ads.lpx) |
| 前程无忧去广告 | 移除开屏广告、弹窗、信息流推广、职位页面推广和各类横幅推广。 | 0 | 0 | [51Job_remove_ads.lpx](plugins/51Job_remove_ads.lpx) |
| 555电影去广告 | 移除开屏广告和各类横幅广告，支持iPadOS。 | 0 | 0 | [555DY_remove_ads.lpx](plugins/555DY_remove_ads.lpx) |
| 5EPlay去广告 | 移除开屏广告、弹窗广告、活动角标、商城。 | 0 | 0 | [5EPlay_remove_ads.lpx](plugins/5EPlay_remove_ads.lpx) |
| 健康160去广告 | 移除开屏广告、应用内悬浮窗、弹窗广告、横幅广告，精简我的页面。 | 0 | 0 | [91160_remove_ads.lpx](plugins/91160_remove_ads.lpx) |
| 爱企查去广告 | 移除开屏广告、应用内弹窗、首页轮播图、悬浮部件、信息流和搜索填充词。 | 0 | 0 | [Aiinquiry_remove_ads.lpx](plugins/Aiinquiry_remove_ads.lpx) |
| 海雀去广告 | 移除开屏广告、横幅广告、弹窗广告，拦截商城和资讯页面。 | 0 | 0 | [AlcidaeVideo_remove_ads.lpx](plugins/AlcidaeVideo_remove_ads.lpx) |
| 阿里云盘去广告 | 移除首页广告横幅、弹窗和顶部奖励。 | 0 | 2 | [AliYunDrive_remove_ads.lpx](plugins/AliYunDrive_remove_ads.lpx) |
| 高德地图去广告 | 移除开屏广告、首页推荐、搜索推荐、打车广告、地点推荐及广告，精简我的页面。 | 0 | 2 | [Amap_remove_ads.lpx](plugins/Amap_remove_ads.lpx) |
| 汽车之家去广告 | 移除开屏广告、各类广告横幅、各类信息流广告、各类弹窗推广、各类浮窗、我的页面广告。 | 0 | 6 | [AutoHome_remove_ads.lpx](plugins/AutoHome_remove_ads.lpx) |
| 排班日历去广告 | 移除开屏广告、横幅广告。 | 0 | 0 | [AxWorkSchedule_remove_ads.lpx](plugins/AxWorkSchedule_remove_ads.lpx) |
| 宝宝树孕育去广告 | 过滤宝宝树孕育广告 | 1 | 3 | [BabyTree_remove_ads.lpx](plugins/BabyTree_remove_ads.lpx) |
| 百度输入法去广告 | 过滤百度输入法广告，替换个人主页随机图。 | 0 | 1 | [Baidu_input_method_remove_ads.lpx](plugins/Baidu_input_method_remove_ads.lpx) |
| 百度地图去广告 | 移除开屏广告、出行页面推广、周边页面推广、打车页面推广，精简我的页面。此插件需要IPA签名方可使用，Ap… | 0 | 0 | [BaiduMap_remove_ads.lpx](plugins/BaiduMap_remove_ads.lpx) |
| 百度网盘去广告 | 移除开屏广告、首页卡片广告、传输页面广告、各类弹窗，精简侧拉抽屉和我的页面。 | 0 | 0 | [BaiduNetDisk_remove_ads.lpx](plugins/BaiduNetDisk_remove_ads.lpx) |
| 一刻相册去广告 | 移除开屏广告、横幅广告和弹窗推广。 | 0 | 0 | [BaiduPhoto_remove_ads.lpx](plugins/BaiduPhoto_remove_ads.lpx) |
| 百度网页去广告 | 移除百度搜索移动端网页的首页广告信息流 | 0 | 1 | [BaiduSearchWebpage_remove_ads.lpx](plugins/BaiduSearchWebpage_remove_ads.lpx) |
| 百度翻译去广告 | 移除开屏广告、横幅广告，精简我的页面。 | 0 | 0 | [BaiduTranslate_remove_ads.lpx](plugins/BaiduTranslate_remove_ads.lpx) |
| 百度文库去广告 | 移除开屏广告、横幅广告、弹窗广告、信息流推广、搜索发现、热门搜索、资料库搜索推荐，精简我的页面。 | 0 | 0 | [BaiduWenku_remove_ads.lpx](plugins/BaiduWenku_remove_ads.lpx) |
| 贝壳找房去广告 | 移除开屏广告、弹窗广告、悬浮广告、信息流推广、我家页面的装修推荐。移除我的页面的专属推荐、游戏入口、钱包… | 0 | 0 | [Beike_remove_ads.lpx](plugins/Beike_remove_ads.lpx) |
| 哔哩哔哩去广告 | 过滤哔哩哔哩广告、移除青少年模式弹窗和交互式弹幕、移除无用功能和链接跟踪参数，增加空降助手以便跳过视频中… | 5 | 12 | [Bilibili_remove_ads.lpx](plugins/Bilibili_remove_ads.lpx) |
| 哔哩哔哩漫画去广告 | 移除开屏广告、应用内悬浮窗、各类横幅广告、你可能喜欢、小说推荐、首页弹窗，精简首页标签、底栏活动按钮和我… | 0 | 2 | [BiliComic_remove_ads.lpx](plugins/BiliComic_remove_ads.lpx) |
| 比特球云盘去广告 | 移除开屏广告和各类横幅推广。 | 0 | 0 | [BitqiuPan_remove_ads.lpx](plugins/BitqiuPan_remove_ads.lpx) |
| 比心去广告 | 移除弹窗广告、悬浮广告、横幅广告、轮播图广告，精简搜索页及我的页面。 | 0 | 4 | [Bixin_remove_ads.lpx](plugins/Bixin_remove_ads.lpx) |
| HTTPDNS拦截器 | 此插件是所有去广告插件的依赖，拦截常见的HTTPDNS服务，以确保这些请求都能够在Loon的DNS框架下… | 93 | 0 | [Block_HTTPDNS.lpx](plugins/Block_HTTPDNS.lpx) |
| 广告平台拦截器 | 此插件是所有去广告插件的依赖，只针对广告平台处理。你依然需要安装其他去广告插件来搭配使用，并确保此插件始… | 339 | 0 | [BlockAdvertisers.lpx](plugins/BlockAdvertisers.lpx) |
| 波点音乐去广告 | 精简应用配置，禁用P2P传输。移除开屏广告、横幅推广、悬浮广告、歌曲广告、商城入口、搜索推广、评论区推广… | 0 | 0 | [BodianMusic_remove_ads.lpx](plugins/BodianMusic_remove_ads.lpx) |
| 薄荷健康去广告 | 移除记录页大家都在看、移除各类弹窗，移除广场横幅推广，精简代谢中心页面。 | 0 | 1 | [BooHee_remove_ads.lpx](plugins/BooHee_remove_ads.lpx) |
| 菜鸟去广告 | 过滤菜鸟广告 | 0 | 0 | [Cainiao_remove_ads.lpx](plugins/Cainiao_remove_ads.lpx) |
| 财新去广告 | 过滤财新广告 | 0 | 6 | [CaixinMedia_remove_ads.lpx](plugins/CaixinMedia_remove_ads.lpx) |
| 猫耳FM去广告 | 移除开屏广告、青少年模式弹窗、首页顶部入口，替换底栏的直播入口为发现入口。 | 0 | 0 | [CatEarFM_remove_ads.lpx](plugins/CatEarFM_remove_ads.lpx) |
| CC直播去广告 | 移除信息流推广和横幅，精简顶部标签。 | 0 | 0 | [CCLive_remove_ads.lpx](plugins/CCLive_remove_ads.lpx) |
| 测测去广告 | 移除开屏广告、活动皮肤、各类弹窗及横幅、金刚位红点文字，精简首页标签及搜索页面。 | 0 | 1 | [Cece_remove_ads.lpx](plugins/Cece_remove_ads.lpx) |
| 学习通去广告 | 移除开屏广告、横幅推广，精简校园补给站频道。 | 0 | 0 | [ChaoXingStudy_remove_ads.lpx](plugins/ChaoXingStudy_remove_ads.lpx) |
| 看家王去广告 | 移除开屏广告、横幅广告。 | 0 | 0 | [ChatCam_remove_ads.lpx](plugins/ChatCam_remove_ads.lpx) |
| 车来了去广告 | 清洗配置，移除开屏广告、首页金刚位、文章推荐，精简我的页面。 | 1 | 7 | [Chelaile_remove_ads.lpx](plugins/Chelaile_remove_ads.lpx) |
| 成分喵去广告 | 移除首页推广活动、广告组件请求、移除被查商品购买链接、搜索发现。 | 0 | 0 | [ChengFenMiao_remove_ads.lpx](plugins/ChengFenMiao_remove_ads.lpx) |
| 触站去广告 | 移除开屏广告、弹窗广告、各页面横幅推广，移除首页悬浮挂件。 | 0 | 0 | [Chuzhan_remove_ads.lpx](plugins/Chuzhan_remove_ads.lpx) |
| 彩云天气去广告 | 移除首页推广、弹窗、悬浮窗、底栏天气助手和工具箱入口，移除我的页面广告横幅。 | 3 | 1 | [ColorfulClouds_remove_ads.lpx](plugins/ColorfulClouds_remove_ads.lpx) |
| 酷安去广告 | 过滤酷安广告 | 0 | 0 | [CoolApk_remove_ads.lpx](plugins/CoolApk_remove_ads.lpx) |
| 小宇宙去广告 | 移除开屏广告、搜索框推荐词和AI总结。 | 0 | 0 | [CosmosPodcast_remove_ads.lpx](plugins/CosmosPodcast_remove_ads.lpx) |
| 天天跳绳去广告 | 移除开屏广告、横幅广告、弹窗广告、活动推广，精简首页标签和搜索页面。 | 0 | 0 | [CrazyRope_remove_ads.lpx](plugins/CrazyRope_remove_ads.lpx) |
| 南网在线去广告 | 移除首页推广，精简搜索页和我的页面。 | 0 | 0 | [CSG_remove_ads.lpx](plugins/CSG_remove_ads.lpx) |
| 推栏去广告 | 过滤推栏广告 | 0 | 0 | [Daily_remove_ads.lpx](plugins/Daily_remove_ads.lpx) |
| 大麦去广告 | 移除开屏广告、轮播图广告和弹窗广告，移除搜索填充词和专属推荐。 | 0 | 0 | [Damai_remove_ads.lpx](plugins/Damai_remove_ads.lpx) |
| 大姨妈月经期助手去广告 | 移除信息流广告，精简首页金刚位及我的页面。 | 0 | 0 | [Dayima_remove_ads.lpx](plugins/Dayima_remove_ads.lpx) |
| 得物去广告 | 移除开屏广告、弹窗、搜索词填充、热搜榜、猜你想搜、推荐关注、推荐信息流，精简消息中心和我的页面。 | 0 | 0 | [Dewu_remove_ads.lpx](plugins/Dewu_remove_ads.lpx) |
| 滴答出行去广告 | 移除开屏广告、弹窗广告、横幅广告，精简底栏和我的页面。 | 0 | 0 | [DidaPincheTaxi_remove_ads.lpx](plugins/DidaPincheTaxi_remove_ads.lpx) |
| 滴滴去广告 | 移除开屏广告、弹窗广告、横幅推广，精简我的页面。 | 3 | 0 | [DiDi_remove_ads.lpx](plugins/DiDi_remove_ads.lpx) |
| 数字心动去广告 | 移除开屏广告、首页顶部标签、轮播图、悬浮挂件、热门搜索、信息流广告。 | 0 | 0 | [DigitalHeartbeat_remove_ads.lpx](plugins/DigitalHeartbeat_remove_ads.lpx) |
| 叮咚买菜去广告 | 移除开屏广告、弹窗推广、搜索推荐、信息流广告、悬浮广告、各页面购物推荐、精简我的页面，移除底栏和各页面A… | 3 | 0 | [DingdongMaicai_remove_ads.lpx](plugins/DingdongMaicai_remove_ads.lpx) |
| DJ多多去广告 | 移除开屏广告及歌单广告 | 0 | 1 | [DjDuoDuo_remove_ads.lpx](plugins/DjDuoDuo_remove_ads.lpx) |
| Dlabel云标签去广告 | 移除开屏广告及首页横幅。 | 0 | 0 | [Dlabel_remove_ads.lpx](plugins/Dlabel_remove_ads.lpx) |
| 豆瓣去广告 | 移除开屏广告、各页面信息流广告、首页横幅、搜索填充词。此插件需要IPA签名方可使用，App Store用… | 0 | 0 | [DouBan_remove_ads.lpx](plugins/DouBan_remove_ads.lpx) |
| 豆瓣阅读去广告 | 移除开屏广告、弹窗广告、热门搜索、热搜榜。 | 0 | 0 | [DoubanRead_remove_ads.lpx](plugins/DoubanRead_remove_ads.lpx) |
| 斗鱼去广告 | 移除开屏、首页视频流、首页轮播图广告，移除直播间悬浮窗。 | 4 | 1 | [Douyu_remove_ads.lpx](plugins/Douyu_remove_ads.lpx) |
| 番茄小说去广告 | 移除番茄小说开屏广告、移除文章底部和章末广告、移除听书页面广告、移除悬浮部件和底栏多余的福利标签。 | 34 | 0 | [DragonRead_remove_ads.lpx](plugins/DragonRead_remove_ads.lpx) |
| DREAME去广告 | 移除开屏广告、首页大图推广、横幅推广，精简底栏，阻止桌面图标替换。仅支持2.5.1版。 | 0 | 1 | [DREAME_remove_ads.lpx](plugins/DREAME_remove_ads.lpx) |
| 配音秀去广告 | 移除开屏广告、弹窗、横幅、各类关注推荐。 | 0 | 1 | [DubbingShow_remove_ads.lpx](plugins/DubbingShow_remove_ads.lpx) |
| 堆糖去广告 | 移除开屏广告、信息流广告、热搜排行榜广告、我的页面横幅广告，移除关注推荐，精简底部导航栏。 | 0 | 0 | [DuiTang_remove_ads.lpx](plugins/DuiTang_remove_ads.lpx) |
| 哈罗去广告 | 移除开屏广告及歌单广告 | 0 | 1 | [EasyBike_remove_ads.lpx](plugins/EasyBike_remove_ads.lpx) |
| e充电去广告 | 移除开屏广告、活动及发现页面，精简我的页面。 | 1 | 0 | [EasyCharge_remove_ads.lpx](plugins/EasyCharge_remove_ads.lpx) |
| ECOVACS HOME去广告 | 移除横幅推广，精简底栏。 | 0 | 0 | [EcovacsHome_remove_ads.lpx](plugins/EcovacsHome_remove_ads.lpx) |
| 中华万年历去广告 | 移除开屏广告、弹窗、信息流推广，精简我的页面。 | 1 | 0 | [EtouchEcalendar_remove_ads.lpx](plugins/EtouchEcalendar_remove_ads.lpx) |
| 丰巢去广告 | 移除弹窗，精简首页和生活服务。此插件需要IPA签名方可使用，App Store用户请勿使用此插件，务必点… | 0 | 0 | [FC_Box_remove_ads.lpx](plugins/FC_Box_remove_ads.lpx) |
| 粉笔去广告 | 移除开屏广告、弹窗广告、悬浮广告、热门搜索，移除底栏皮肤，精简我的页面。 | 0 | 1 | [FenBi_remove_ads.lpx](plugins/FenBi_remove_ads.lpx) |
| 摩天轮去广告 | 移除开屏广告、弹窗，精简底栏。 | 0 | 0 | [FerrisWheel_remove_ads.lpx](plugins/FerrisWheel_remove_ads.lpx) |
| 华尔街见闻去广告 | 移除开屏广告、文末广告、信息流广告，精简底栏。 | 0 | 0 | [FinanceNews_remove_ads.lpx](plugins/FinanceNews_remove_ads.lpx) |
| 闲鱼去广告 | 移除开屏广告、商品信息流广告、关注推荐、搜索栏填充词、首页签到入口及悬浮广告，精简我的页面。 | 0 | 0 | [FleaMarket_remove_ads.lpx](plugins/FleaMarket_remove_ads.lpx) |
| 飞客去广告 | 移除开屏广告、首页广告、板块广告、帖内广告和我的页面广告。 | 0 | 2 | [FlyerTea_remove_ads.lpx](plugins/FlyerTea_remove_ads.lpx) |
| Foodie去广告 | 移除开屏广告和弹窗广告 | 3 | 0 | [Foodie_remove_ads.lpx](plugins/Foodie_remove_ads.lpx) |
| 稿定设计去广告 | 移除稿定设计开屏广告、首页轮播图和弹窗，移除功能入口角标。 | 0 | 0 | [GaoDing_remove_ads.lpx](plugins/GaoDing_remove_ads.lpx) |
| Google搜索重定向 | 将Google搜索重定向至.com域名，如遇频繁跳转请禁用本插件。 | 0 | 0 | [Google.lpx](plugins/Google.lpx) |
| 盖得排行去广告 | 精简首页、移除分类横幅推广、单单返猜你喜欢和编辑精选，移除我的页面推广。 | 0 | 0 | [GuideRank_remove_ads.lpx](plugins/GuideRank_remove_ads.lpx) |
| 华住会去广告 | 移除弹窗、横幅，精简首页。 | 0 | 0 | [HantingHotels_remove_ads.lpx](plugins/HantingHotels_remove_ads.lpx) |
| 小睡眠去广告 | 移除开屏广告、信息流广告、弹窗广告、轮播图广告、侧边栏横幅广告，精简搜索页面。 | 0 | 0 | [HeartideBrainWave_remove_ads.lpx](plugins/HeartideBrainWave_remove_ads.lpx) |
| 喜马拉雅去广告 | 移除开屏广告、播放器广告、各类推荐内容，精简频道和我的页面。 | 5 | 1 | [Himalaya_remove_ads.lpx](plugins/Himalaya_remove_ads.lpx) |
| 香港抖音去广告 | 精简左右侧边栏、移除底栏切换，其余内容后续再完善。 | 6 | 0 | [HKDouYin_remove_ads.lpx](plugins/HKDouYin_remove_ads.lpx) |
| Hong Kong Toolbar去广告 | 移除开屏互动广告、直播前贴片广告及视频广告 | 0 | 0 | [HongKongToolbar_remove_ads.lpx](plugins/HongKongToolbar_remove_ads.lpx) |
| 虎扑去广告 | 移除虎扑开屏广告、首页顶部推广、我的页面多余模块及各类横幅推广。 | 0 | 4 | [HUPU_remove_ads.lpx](plugins/HUPU_remove_ads.lpx) |
| 虎嗅去广告 | 移除广告配置、信息流直播预约横幅、相关文章推荐、48小时热文推荐，精简搜索页面。 | 1 | 0 | [Huxiu_remove_ads.lpx](plugins/Huxiu_remove_ads.lpx) |
| 凤凰新闻去广告 | 移除皮肤、开屏广告、信息流广告、文末广告、视频流广告、评论区广告，移除信息流订阅号文章、文末推荐阅读，精… | 0 | 0 | [ifengNews_remove_ads.lpx](plugins/ifengNews_remove_ads.lpx) |
| 小象超市去广告 | 移除开屏广告、应用内弹窗、猜你想买、横幅推广和悬浮窗。 | 0 | 1 | [iMaiCai_remove_ads.lpx](plugins/iMaiCai_remove_ads.lpx) |
| 爱奇艺去广告 | 移除开屏广告、焦点图广告、瀑布流广告、搜索页面广告、移除青少年弹窗，精简底栏和我的页面。 | 2 | 0 | [iQiYi_Video_remove_ads.lpx](plugins/iQiYi_Video_remove_ads.lpx) |
| 掌阅去广告 | 移除开屏广告、悬浮广告、弹窗广告、朗读音色广告及我的页面广告，移除各页面的横幅轮播图。 | 1 | 0 | [iReader_remove_ads.lpx](plugins/iReader_remove_ads.lpx) |
| 天气预报去广告 | 移除开屏广告、弹窗广告、横幅广告、悬浮挂件，精简我的页面。 | 2 | 1 | [iReaderCityWeather_remove_ads.lpx](plugins/iReaderCityWeather_remove_ads.lpx) |
| 得间小说去广告 | 移除开屏广告、章末广告，移除扉页广告提示、听书界面广告提示、搜索栏填充词。 | 2 | 0 | [iReaderDejian_remove_ads.lpx](plugins/iReaderDejian_remove_ads.lpx) |
| IT之家去广告 | 过滤IT之家信息流广告和文末广告，自定义移除置顶和轮播图，自定义移除项需在插件配置。 | 0 | 1 | [IThome_remove_ads.lpx](plugins/IThome_remove_ads.lpx) |
| 最美壁纸去广告 | 移除悬浮广告、横幅广告、轮播图广告，精简我的页面。 | 0 | 3 | [iWallBiZhi_remove_ads.lpx](plugins/iWallBiZhi_remove_ads.lpx) |
| 京东去广告 | 移除京东开屏广告，精简我的页面产品推广。 | 1 | 1 | [JD_remove_ads.lpx](plugins/JD_remove_ads.lpx) |
| 京东外卖去广告 | 移除首页推广、点评页面非美食内容、购物车及我的页面推荐、搜索发现、搜索榜单，精简我的页面。 | 0 | 0 | [JDWaimai_remove_ads.lpx](plugins/JDWaimai_remove_ads.lpx) |
| 驾考宝典去广告 | 移除开屏广告、横幅广告、悬浮窗广告、社区帖子广告，精简我的页面。 | 0 | 0 | [JiaKaoBaoDian_remove_ads.lpx](plugins/JiaKaoBaoDian_remove_ads.lpx) |
| 驾校一点通去广告 | 移除开屏广告、各页面广告横幅、弹窗广告，移除社区广告。 | 0 | 0 | [JiaXiaoDrive_remove_ads.lpx](plugins/JiaXiaoDrive_remove_ads.lpx) |
| 金十数据去广告 | 移除开屏广告、侧滑页面广告、消息广告、浮窗广告、横幅广告、信息流广告、弹窗广告。 | 0 | 0 | [Jin10Data_remove_ads.lpx](plugins/Jin10Data_remove_ads.lpx) |
| Jump去广告 | 移除Jump开屏广告 | 7 | 0 | [Jump_remove_ads.lpx](plugins/Jump_remove_ads.lpx) |
| 帆书去广告 | 移除弹窗和会员任务，精简首页、听书页面、课程菜单和我的页面。 | 0 | 9 | [KebidaDushu_remove_ads.lpx](plugins/KebidaDushu_remove_ads.lpx) |
| Keep去广告 | 移除开屏广告、搜索推荐和弹窗广告，精简底栏和首页标签。移除关注推荐、文章相关推荐和信息流中的课程推广。 | 1 | 0 | [Keep_remove_ads.lpx](plugins/Keep_remove_ads.lpx) |
| 酷狗铃声去广告 | 移除开屏广告，移除歌曲列表、播放器、搜索界面广告，移除悬浮广告和弹窗广告。 | 0 | 0 | [KGRing_remove_ads.lpx](plugins/KGRing_remove_ads.lpx) |
| 随手记去广告 | 移除开屏广告、神象云账本内部广告、我的页面广告，移除社区入口。 | 0 | 0 | [KingdeeMyMoney_remove_ads.lpx](plugins/KingdeeMyMoney_remove_ads.lpx) |
| KOOK去广告 | 移除开屏广告、房间横幅推广、促销活动、精简发现页面频道及我的页面，移除底栏商城入口。 | 0 | 0 | [KOOK_remove_ads.lpx](plugins/KOOK_remove_ads.lpx) |
| 快递100去广告 | 移除横幅广告、弹窗广告，精简首页。 | 0 | 0 | [KuaiDi100_remove_ads.lpx](plugins/KuaiDi100_remove_ads.lpx) |
| 快对去广告 | 移除开屏广告、横幅推广，精简我的页面。 | 1 | 0 | [KuaiDuiZuoYe_remove_ads.lpx](plugins/KuaiDuiZuoYe_remove_ads.lpx) |
| 快看漫画去广告 | 移除开屏广告、悬浮窗、漫画广告、社区广告、各类弹窗，精简顶部标签、我的页面。 | 3 | 4 | [KuaiKanComic_remove_ads.lpx](plugins/KuaiKanComic_remove_ads.lpx) |
| 快手去广告 | 移除开屏广告、视频流广告、底栏皮肤、右下角悬浮推广，精简我的页面。 | 0 | 0 | [KuaiShou_remove_ads.lpx](plugins/KuaiShou_remove_ads.lpx) |
| 酷狗音乐去广告 | 移除开屏广告、应用各类弹窗、各类横幅广告、评论区广告和播放器界面广告。 | 9 | 0 | [KuGou_remove_ads.lpx](plugins/KuGou_remove_ads.lpx) |
| 酷狗概念版去广告 | 移除广告服务模块、播放器广告，精简乐库及搜索页面。 | 0 | 0 | [KuGouYouth_remove_ads.lpx](plugins/KuGouYouth_remove_ads.lpx) |
| 库街区去广告 | 移除开屏广告、弹窗广告、搜索页面的热搜及话题热榜。 | 0 | 0 | [KuroBBS_remove_ads.lpx](plugins/KuroBBS_remove_ads.lpx) |
| 酷我音乐去广告 | 移除开屏广告、各类弹窗、悬浮窗、各类横幅广告、信息流广告、歌词评论区广告和播放器界面广告，精简侧边栏。 | 0 | 0 | [Kuwo_remove_ads.lpx](plugins/Kuwo_remove_ads.lpx) |
| 快影去广告 | 移除开屏广告、信息流推广、横幅推广，移除悬浮部件。 | 0 | 0 | [KwaiVideoeditor_remove_ads.lpx](plugins/KwaiVideoeditor_remove_ads.lpx) |
| Line去广告 | 移除Line各类广告 | 0 | 0 | [Line_remove_ads.lpx](plugins/Line_remove_ads.lpx) |
| 纷玩岛去广告 | 移除开屏广告、弹窗广告、信息横幅推广、票夹页面横幅广告。 | 0 | 0 | [LiveLab_remove_ads.lpx](plugins/LiveLab_remove_ads.lpx) |
| 掌上英雄联盟去广告 | 移除开屏广告、弹窗推广、搜索热搜、搜索热榜、底栏推广图标。 | 0 | 0 | [LOL_Bible_remove_ads.lpx](plugins/LOL_Bible_remove_ads.lpx) |
| 瑞幸咖啡去广告 | 移除开屏广告、弹窗和各类横幅推广。 | 0 | 0 | [LuckinCoffee_remove_ads.lpx](plugins/LuckinCoffee_remove_ads.lpx) |
| 联掌门户去广告 | 移除开屏广告、弹窗，移除首页、服务和发现页面无用内容。 | 0 | 0 | [LZMH_remove_ads.lpx](plugins/LZMH_remove_ads.lpx) |
| 马蜂窝去广告 | 移除首页信息流广告、商城横幅推广、我的页面弹窗。 | 1 | 0 | [MaFengWo_remove_ads.lpx](plugins/MaFengWo_remove_ads.lpx) |
| 网易邮箱大师去广告 | 移除网易邮箱大师开屏广告、签到任务提醒，精简侧拉抽屉和我的页面。 | 0 | 0 | [MailMaster_remove_ads.lpx](plugins/MailMaster_remove_ads.lpx) |
| 脉脉去广告 | 移除开屏广告、信息流广告、横幅推广、相关帖子推荐。 | 0 | 1 | [MaiMai_remove_ads.lpx](plugins/MaiMai_remove_ads.lpx) |
| 芒果TV去广告 | 移除开屏广告、信息流广告、播放页广告，精简我的页面。 | 13 | 0 | [MangoTV_remove_ads.lpx](plugins/MangoTV_remove_ads.lpx) |
| 马克水印相机去广告 | 移除开屏广告，拍摄首页悬浮挂件，侧边栏横幅广告。 | 0 | 0 | [marki_remove_ads.lpx](plugins/marki_remove_ads.lpx) |
| 美柚去广告 | 移除开屏广告、弹窗推广和信息流推广，移除青少年模式弹窗和我的页面推广。 | 2 | 0 | [MeetYou_remove_ads.lpx](plugins/MeetYou_remove_ads.lpx) |
| 每日赛车去广告 | 移除开屏广告、信息流广告。 | 0 | 0 | [MeiRiSaiChe_remove_ads.lpx](plugins/MeiRiSaiChe_remove_ads.lpx) |
| 美食杰去广告 | 移除开屏广告和信息流广告。 | 0 | 0 | [MeiShiJie_remove_ads.lpx](plugins/MeiShiJie_remove_ads.lpx) |
| 美图秀秀去广告 | 移除开屏广告、横幅推广，精简我的页面。 | 1 | 0 | [MeiTu_remove_ads.lpx](plugins/MeiTu_remove_ads.lpx) |
| 美颜相机去广告 | 移除开屏广告、应用内弹窗，精简首页和我的页面。 | 1 | 1 | [MeituMYXJ_remove_ads.lpx](plugins/MeituMYXJ_remove_ads.lpx) |
| 美丽修行去广告 | 移除开屏广告、首页广告、发现页广告、美修盒页面广告、下拉广告、弹窗广告、搜索推广、版本更新弹窗及我的页面… | 0 | 0 | [Meizhixiuxing_remove_ads.lpx](plugins/Meizhixiuxing_remove_ads.lpx) |
| 小喵看书去广告 | 移除小喵看书章末广告 | 0 | 0 | [MiaoRead_remove_ads.lpx](plugins/MiaoRead_remove_ads.lpx) |
| 米游社去广告 | 移除开屏广告、搜索栏热搜及资讯、青少年模式弹窗。 | 0 | 0 | [miHoYoBBS_remove_ads.lpx](plugins/miHoYoBBS_remove_ads.lpx) |
| 漫客栈去广告 | 移除开屏广告、漫画广告、小说章末广告，精简我的页面。 | 0 | 1 | [MKZ_remove_ads.lpx](plugins/MKZ_remove_ads.lpx) |
| 中国移动云盘去广告 | 移除中国移动云盘开屏广告及应用内广告，首页的多余卡片可滑到最底部自定义隐藏掉，插件对此不做处理。 | 0 | 2 | [mobileClouds_remove_ads.lpx](plugins/mobileClouds_remove_ads.lpx) |
| 萌娘百科去广告 | 移除开屏广告、弹窗、首页横幅。 | 0 | 0 | [MoeGirlWiki_remove_ads.lpx](plugins/MoeGirlWiki_remove_ads.lpx) |
| 墨迹天气去广告 | 移除天气页面横幅、工具栏，移除时景关注页面推荐，精简我的页面。 | 0 | 0 | [MojiWeather_remove_ads.lpx](plugins/MojiWeather_remove_ads.lpx) |
| 摩托范去广告 | 移除开屏广告、弹窗广告、横幅广告、文末广告及相关文章推荐、广告下发，移除我的页面商品推荐，精简搜索页面。 | 0 | 4 | [MotorFans_remove_ads.lpx](plugins/MotorFans_remove_ads.lpx) |
| 盒马去广告 | 移除开屏广告、首页信息流广告及推广、弹窗广告、悬浮挂件、商品及购物车推荐，精简底栏及我的页面。 | 0 | 0 | [MrHema_remove_ads.lpx](plugins/MrHema_remove_ads.lpx) |
| 超级课程表去广告 | 移除开屏广告、首页头图、悬浮挂件。 | 1 | 0 | [MyFriday_remove_ads.lpx](plugins/MyFriday_remove_ads.lpx) |
| 云鲸智能去广告 | 移除开屏广告、横幅推广，禁用商城。 | 0 | 0 | [NarwelRobots_remove_ads.lpx](plugins/NarwelRobots_remove_ads.lpx) |
| 网易云音乐去广告 | 过滤网易云音乐广告，并允许自定义界面。 | 6 | 8 | [NeteaseCloudMusic_remove_ads.lpx](plugins/NeteaseCloudMusic_remove_ads.lpx) |
| 网易大神去广告 | 移除开屏广告，精简大量冗余的配置文件，精简我的页面。 | 0 | 1 | [NetEaseGodlike_remove_ads.lpx](plugins/NetEaseGodlike_remove_ads.lpx) |
| 网易新闻去广告 | 移除开屏广告、置顶新闻、热搜列表和搜索栏填充词。 | 0 | 3 | [NeteaseNews_remove_ads.lpx](plugins/NeteaseNews_remove_ads.lpx) |
| OKOK去广告 | 移除开屏广告、横幅广告，精简首页，拦截优惠购页面。 | 0 | 0 | [OKOK_remove_ads.lpx](plugins/OKOK_remove_ads.lpx) |
| 行者户外去广告 | 移除弹窗广告、发现页面横幅推广的推广金刚位，移除我的页面横幅推广。 | 0 | 0 | [OnTheWay_remove_ads.lpx](plugins/OnTheWay_remove_ads.lpx) |
| 向日葵去广告 | 移除开屏广告、广告横幅。 | 0 | 0 | [OraySunlogin_remove_ads.lpx](plugins/OraySunlogin_remove_ads.lpx) |
| 胖乖生活去广告 | 移除开屏广告、横幅轮播图、网格广告、信息流广告、浮窗广告，精简我的页面。 | 0 | 0 | [PangguaiLife_remove_ads.lpx](plugins/PangguaiLife_remove_ads.lpx) |
| 完美世界电竞去广告 | 移除开屏广告，精简搜索页。 | 0 | 0 | [PerfectWorldEsport_remove_ads.lpx](plugins/PerfectWorldEsport_remove_ads.lpx) |
| 中国人保去广告 | 移除中国人保开屏广告和应用内广告 | 0 | 2 | [PICC_Insurance_remove_ads.lpx](plugins/PICC_Insurance_remove_ads.lpx) |
| PICOOC去广告 | 移除开屏广告、悬浮广告，拦截发现页，精简我的页面。 | 0 | 0 | [PICOOC_remove_ads.lpx](plugins/PICOOC_remove_ads.lpx) |
| 拼多多去广告 | 移除开屏广告、底栏多多视频、会场入口、聊天页面精选推荐及推广，精简首页和个人中心。 | 17 | 1 | [PinDuoDuo_remove_ads.lpx](plugins/PinDuoDuo_remove_ads.lpx) |
| Pinterest去广告 | 移除瀑布流、更多探索内容中的广告 | 0 | 0 | [Pinterest_remove_ads.lpx](plugins/Pinterest_remove_ads.lpx) |
| 皮皮虾去广告 | 移除开屏广告、评论区广告、视频流广告，精简我的页面。 | 0 | 0 | [PiPiXia_remove_ads.lpx](plugins/PiPiXia_remove_ads.lpx) |
| 朴朴超市去广告 | 移除超市去开屏广告，移除首页顶部轮播图和图标广告、启动小弹图广告、首页右下角悬浮动画、搜索热搜榜、搜索建… | 0 | 6 | [PuPuMall_remove_ads.lpx](plugins/PuPuMall_remove_ads.lpx) |
| 亲宝宝去广告 | 移除开屏广告、弹窗广告、广告下发、用户行为上报，精简搜索页、育儿页和我的页面，拦截商城页面。 | 1 | 2 | [Qbb_remove_ads.lpx](plugins/Qbb_remove_ads.lpx) |
| 起点读书去广告 | 移除起点读书开屏广告、每日导读、各类弹窗、文末广告、搜索填充词，精简我的页面。 | 0 | 0 | [QiDian_remove_ads.lpx](plugins/QiDian_remove_ads.lpx) |
| 启信宝去广告 | 移除开屏广告、应用内弹窗、首页轮播图、悬浮部件和个性化推荐信息流。 | 0 | 0 | [QiXinBao_remove_ads.lpx](plugins/QiXinBao_remove_ads.lpx) |
| QQ链接解锁 | 解除QQ内访问非白名单之外的地址提示停止访问该页面的限制，并移除跟踪参数，使用前需要清除QQ的缓存数据。 | 0 | 0 | [QQ_Redirect.lpx](plugins/QQ_Redirect.lpx) |
| 全民K歌去广告 | 移除开屏广告、歌房页面弹窗广告、消息页广告和我的页面广告。 | 33 | 0 | [QQKSong_remove_ads.lpx](plugins/QQKSong_remove_ads.lpx) |
| QQ音乐去广告 | 过滤QQ音乐广告 | 11 | 0 | [QQMusic_remove_ads.lpx](plugins/QQMusic_remove_ads.lpx) |
| 蜻蜓FM去广告 | 移除开屏广告、信息流广告、各类相关内容推荐，精简我的页面。 | 2 | 0 | [QtingFM_remove_ads.lpx](plugins/QtingFM_remove_ads.lpx) |
| 夸克去广告 | 移除阅读广告、各页面弹窗及横幅，精简我的页面。 | 0 | 0 | [QuarkBrowser_remove_ads.lpx](plugins/QuarkBrowser_remove_ads.lpx) |
| 夸克扫描王去广告 | 移除弹窗广告、横幅广告，精简我的页面。 | 0 | 0 | [QuarkScanking_remove_ads.lpx](plugins/QuarkScanking_remove_ads.lpx) |
| 快捷搜索 | 为Safari提供快速切换搜索引擎的能力，在插件列表中点击此插件上的链接查看使用方法。 | 0 | 0 | [QuickSearch.lpx](plugins/QuickSearch.lpx) |
| Reddit去广告 | 过滤应用内推广，阻止NSFW提示。 | 0 | 1 | [Reddit_remove_ads.lpx](plugins/Reddit_remove_ads.lpx) |
| 小红书去广告 | 过滤信息流推广，移除图片及视频水印，如有异常，请先清除缓存再尝试。 | 1 | 12 | [RedPaper_remove_ads.lpx](plugins/RedPaper_remove_ads.lpx) |
| ReelShort去广告 | 移除开屏广告、为你推荐及各类弹窗，移除搜索栏填充词。 | 0 | 0 | [ReelShort_remove_ads.lpx](plugins/ReelShort_remove_ads.lpx) |
| 可莉广告过滤器 | 可莉自用的广告过滤器 | 18 | 1 | [Remove_ads_by_keli.lpx](plugins/Remove_ads_by_keli.lpx) |
| 风鸟去广告 | 移除首页信息流和轮播图 | 0 | 1 | [RiskBird_remove_ads.lpx](plugins/RiskBird_remove_ads.lpx) |
| Roborock去广告 | 移除横幅、活动推广、机器人图标，精简服务中心。 | 0 | 0 | [Roborock_remove_ads.lpx](plugins/Roborock_remove_ads.lpx) |
| 萝卜快跑去广告 | 移除开屏广告、弹窗广告、横幅广告、新用户活动皮肤，保留优惠活动。 | 0 | 0 | [RoboTaxi_remove_ads.lpx](plugins/RoboTaxi_remove_ads.lpx) |
| RQrun去广告 | 移除开屏广告 | 0 | 0 | [RQrun_remove_ads.lpx](plugins/RQrun_remove_ads.lpx) |
| 360智慧生活去广告 | 移除开屏广告、首页推广横幅、商城入口及我的页面推广。 | 1 | 0 | [SafetyHome_remove_ads.lpx](plugins/SafetyHome_remove_ads.lpx) |
| 剑网三无界去广告 | 移除热门推送活动，并解决无法在Loon运行时更新和登录的问题。 | 0 | 0 | [SeasunJX3_remove_ads.lpx](plugins/SeasunJX3_remove_ads.lpx) |
| 七猫小说去广告 | 移除大部分七猫小说广告，但受限于七猫小说自身对MitM和VPN状态的检测，部分页面广告无法移除。 | 3 | 0 | [SevenCat_remove_ads.lpx](plugins/SevenCat_remove_ads.lpx) |
| 顺丰速运去广告 | 移除开屏广告、首页下拉抽屉、首页推广、应用内悬浮窗、横幅广告，移除主题，精简我的页面。 | 0 | 1 | [SF-Express_remove_ads.lpx](plugins/SF-Express_remove_ads.lpx) |
| 闪动校园去广告 | 精简首页和底部导航 | 0 | 0 | [ShandongSchool_remove_ads.lpx](plugins/ShandongSchool_remove_ads.lpx) |
| 小店掌柜去广告 | 移除开屏广告、活动推广和页面跳转。 | 0 | 0 | [ShopKeeperAdmin_remove_ads.lpx](plugins/ShopKeeperAdmin_remove_ads.lpx) |
| 口袋壁纸去广告 | 移除悬浮广告，精简我的页面。 | 0 | 1 | [ShoujiDesk_remove_ads.lpx](plugins/ShoujiDesk_remove_ads.lpx) |
| 收银通商户端去广告 | 移除开屏广告和首页推广 | 0 | 0 | [ShouYinTongMerchant_remove_ads.lpx](plugins/ShouYinTongMerchant_remove_ads.lpx) |
| 书旗小说去广告 | 移除书城横幅广告、听书广告、阅读广告、章末推荐、福利入口、悬浮窗、推荐搜索词，精简我的页面。 | 1 | 1 | [ShuQiCenterReader_remove_ads.lpx](plugins/ShuQiCenterReader_remove_ads.lpx) |
| 新浪财经去广告 | 移除开屏广告、弹窗广告、横幅广告、信息流广告，精简我的页面。 | 0 | 0 | [SinaStock_remove_ads.lpx](plugins/SinaStock_remove_ads.lpx) |
| 创维智慧云去广告 | 移除开屏广告、横幅广告。 | 0 | 0 | [SkyworthDigitalPicamera_remove_ads.lpx](plugins/SkyworthDigitalPicamera_remove_ads.lpx) |
| 慧生活798去广告 | 移除开屏广告、横幅广告，精简底栏。 | 0 | 0 | [SmartLife_remove_ads.lpx](plugins/SmartLife_remove_ads.lpx) |
| 什么值得买去广告 | 移除开屏广告、信息流广告、各类横幅广告、搜索页广告、文章内广告，移除活动皮肤、精简我的页面。 | 1 | 1 | [smzdm_remove_ads.lpx](plugins/smzdm_remove_ads.lpx) |
| 蜗牛睡眠去广告 | 移除音乐页面横幅、日报告解决方案商品推广，移除我的页面服务推广。 | 1 | 0 | [SnailSleep_remove_ads.lpx](plugins/SnailSleep_remove_ads.lpx) |
| 雪球去广告 | 移除开屏广告、各类横幅广告、信息流广告、帖内广告、新用户定向广告、各类弹窗、股票精选推荐、基金精选推荐、… | 0 | 0 | [Snowball_remove_ads.lpx](plugins/Snowball_remove_ads.lpx) |
| B612咔叽去广告 | 移除开屏广告、弹窗及拍摄页面底部横幅广告。 | 3 | 0 | [SnowCamera_remove_ads.lpx](plugins/SnowCamera_remove_ads.lpx) |
| 汽水音乐去广告 | 移除开屏广告、弹窗广告、播放器推广、歌曲详情界面视频推广、播放页面的歌曲视频，精简首页和我的页面。 | 0 | 1 | [SodaMusic_remove_ads.lpx](plugins/SodaMusic_remove_ads.lpx) |
| Sofascore去广告 | 移除横幅及信息流广告 | 0 | 1 | [Sofascore_remove_ads.lpx](plugins/Sofascore_remove_ads.lpx) |
| Soul去广告 | 移除开屏广告、移除话题页面热Soul话题、移除评论区礼物榜、移除更新提示、移除青少年弹窗、移除我的页面推… | 4 | 1 | [Soul_remove_ads.lpx](plugins/Soul_remove_ads.lpx) |
| Spotify去广告 | 移除播放广告，恢复歌手和专辑列表的正常展示。修改插件自定义配置项需要重新登陆方可生效。 | 1 | 1 | [Spotify_remove_ads.lpx](plugins/Spotify_remove_ads.lpx) |
| 智慧苏州去广告 | 移除开屏广告、横幅，移除信息流推广。 | 0 | 2 | [SuZhouCitizenCard_remove_ads.lpx](plugins/SuZhouCitizenCard_remove_ads.lpx) |
| 淘宝去广告 | 过滤淘宝开屏广告 | 6 | 2 | [Taobao_remove_ads.lpx](plugins/Taobao_remove_ads.lpx) |
| 飞猪旅行去广告 | 移除开屏广告、精简我的页面。 | 0 | 0 | [TaobaoTravel_remove_ads.lpx](plugins/TaobaoTravel_remove_ads.lpx) |
| 淘票票去广告 | 移除开屏广告、悬浮广告、轮播图广告和弹窗广告，移除搜索填充词和为你推荐。 | 0 | 0 | [Taopiaopiao_remove_ads.lpx](plugins/Taopiaopiao_remove_ads.lpx) |
| 他趣去广告 | 移除各类弹窗、横幅，精简我的页面。 | 0 | 0 | [Taqu_remove_ads.lpx](plugins/Taqu_remove_ads.lpx) |
| 多屏互动去广告 | 移除开屏广告、横幅推广、搜索填充词，移除广告下发。 | 0 | 0 | [TCLnScreen_remove_ads.lpx](plugins/TCLnScreen_remove_ads.lpx) |
| Telegram重定向 | 适用于安装了多个不同Telegram客户端的用户，用于在指定客户端中打开公开或私有群组及频道的Teleg… | 0 | 0 | [TelegramRedirect.lpx](plugins/TelegramRedirect.lpx) |
| 腾讯视频去广告 | 过滤腾讯视频客户端广告，如遇失效，则需要重新安装腾讯视频客户端。由于此插件不再维护，客户端版本高于8.9… | 15 | 1 | [Tencent_Video_remove_ads.lpx](plugins/Tencent_Video_remove_ads.lpx) |
| TeraBox去广告 | 移除开屏广告、应用内悬浮窗、弹窗广告及横幅广告。 | 1 | 0 | [TeraBox_remove_ads.lpx](plugins/TeraBox_remove_ads.lpx) |
| 天气通去广告 | 移除开屏广告、横幅广告、弹窗广告，精简底栏及我的页面。 | 0 | 0 | [TianQiTong_remove_ads.lpx](plugins/TianQiTong_remove_ads.lpx) |
| 百度贴吧去广告 | 移除开屏广告、信息流广告和帖内广告，精简侧拉抽屉及我的页面。 | 1 | 2 | [Tieba_remove_ads.lpx](plugins/Tieba_remove_ads.lpx) |
| 天猫校园去广告 | 移除广告配置、开屏广告、弹窗广告、AI助手、促销模块，精简我的页面。 | 0 | 0 | [TmallCampus_remove_ads.lpx](plugins/TmallCampus_remove_ads.lpx) |
| TubeMax去广告 | 过滤TubeMax广告 | 8 | 0 | [TubeMax_remove_ads.lpx](plugins/TubeMax_remove_ads.lpx) |
| 图怪兽去广告 | 移除开屏广告、弹窗广告、各页面横幅推广。 | 0 | 0 | [TuGuaiShou_remove_ads.lpx](plugins/TuGuaiShou_remove_ads.lpx) |
| Tumblr去广告 | 移除信息流广告 | 0 | 0 | [Tumblr_remove_ads.lpx](plugins/Tumblr_remove_ads.lpx) |
| 乐播投屏去广告 | 移除开屏广告、首页横幅推广、全网全网热投榜，移除我的页面横幅推广。 | 0 | 1 | [TV_Assistant_remove_ads.lpx](plugins/TV_Assistant_remove_ads.lpx) |
| 腾讯文档去广告 | 移除开屏广告、首页横幅推广。 | 0 | 0 | [TXDocs_remove_ads.lpx](plugins/TXDocs_remove_ads.lpx) |
| Uki去广告 | 移除开屏广告、应用内悬浮窗，各类横幅、信息流广告、搜索填充词、我的页面广告。 | 0 | 4 | [Uki_remove_ads.lpx](plugins/Uki_remove_ads.lpx) |
| 航旅纵横去广告 | 过滤航旅纵横广告 | 1 | 1 | [Umetrip_remove_ads.lpx](plugins/Umetrip_remove_ads.lpx) |
| 掌上无畏契约去广告 | 移除开屏广告、弹窗推广、搜索热搜、搜索热榜。 | 0 | 0 | [ValorantBible_remove_ads.lpx](plugins/ValorantBible_remove_ads.lpx) |
| 萤石云视频去广告 | 移除开屏广告、首页推广、我的页面推广。 | 0 | 0 | [VideoGo_remove_ads.lpx](plugins/VideoGo_remove_ads.lpx) |
| 挖财记账去广告 | 移除开屏广告、横幅广告，顶部推广、活动配置。 | 0 | 1 | [Wacai_remove_ads.lpx](plugins/Wacai_remove_ads.lpx) |
| 挖财记账去广告 | 移除弹窗广告、推广语横幅和右下角悬浮广告。 | 0 | 0 | [WaCaiJiZhang_remove_ads.lpx](plugins/WaCaiJiZhang_remove_ads.lpx) |
| WakeUp课程表去广告 | 移除横幅广告、弹窗广告，精简我的页面。 | 0 | 0 | [WakeupSchedule_remove_ads.lpx](plugins/WakeupSchedule_remove_ads.lpx) |
| 沃尔玛去广告 | 移除操作引导、商品详情页用户调研、搜索填充词和搜索发现，精简我的页面。 | 0 | 0 | [Walmart_remove_ads.lpx](plugins/Walmart_remove_ads.lpx) |
| 中国天气去广告 | 移除开屏广告、弹窗广告、横幅广告，移除焦点视频、精简我的页面。 | 0 | 0 | [WeatherChina_remove_ads.lpx](plugins/WeatherChina_remove_ads.lpx) |
| 微博轻享版去广告 | 移除开屏广告、时间线广告及评论区广告，移除发现页面横幅推广、最常访问、主页访客及热门视频，移除搜索填充词… | 0 | 0 | [Weibo_intl_remove_ads.lpx](plugins/Weibo_intl_remove_ads.lpx) |
| 微博去广告 | 过滤微博广告及去除各部分推广模块 | 2 | 20 | [Weibo_remove_ads.lpx](plugins/Weibo_remove_ads.lpx) |
| 微店去广告 | 移除开屏广告、弹窗广告、猜你喜欢、猜你想搜、关注推荐，精简搜索页和我的页面。 | 0 | 2 | [Weidian_remove_ads.lpx](plugins/Weidian_remove_ads.lpx) |
| 微脉圈去广告 | 移除开屏广告、聊天页横幅提示及发现页面的横幅广告。 | 0 | 0 | [Weimai_remove_ads.lpx](plugins/Weimai_remove_ads.lpx) |
| 微信公众号去广告 | 过滤微信公众号广告 | 1 | 0 | [Weixin_Official_Accounts_remove_ads.lpx](plugins/Weixin_Official_Accounts_remove_ads.lpx) |
| 微信小程序去广告 | 收录常用小程序的去广告，作者署名在插件内。 | 6 | 12 | [WexinMiniPrograms_Remove_ads.lpx](plugins/WexinMiniPrograms_Remove_ads.lpx) |
| 威锋去广告 | 移除开屏广告、信息流广告、文末广告、首页轮播图推广。 | 0 | 0 | [WPForum_remove_ads.lpx](plugins/WPForum_remove_ads.lpx) |
| 金山文档去广告 | 移除首页横幅推广、表单收集页面推广和我的页面推广。 | 0 | 0 | [WPS_Documents_remove_ads.lpx](plugins/WPS_Documents_remove_ads.lpx) |
| 无他相机去广告 | 移除开屏广告、拍摄页面广告、右小角广告，精简底栏。 | 0 | 0 | [WutaCamera_remove_ads.lpx](plugins/WutaCamera_remove_ads.lpx) |
| 磁力宅播放器去广告 | 移除开屏广告、弹窗和文件列表广告。 | 0 | 0 | [XFuse_remove_ads.lpx](plugins/XFuse_remove_ads.lpx) |
| 下厨房去广告 | 移除开屏广告、页面推广及横幅，精简首页标签。 | 0 | 0 | [XiaChuFang_remove_ads.lpx](plugins/XiaChuFang_remove_ads.lpx) |
| 小白智慧打印去广告 | 移除开屏广告、首页推广金刚位、热门内容推荐、横幅广告、搜索填充词、搜索发现，精简我的页面。账户页面错误是… | 2 | 0 | [XiaobaiPrint_remove_ads.lpx](plugins/XiaobaiPrint_remove_ads.lpx) |
| 小蚕霸王餐去广告 | 移除开屏广告、首页横幅推广、红包推广、更新弹窗。 | 0 | 0 | [XiaoCan_remove_ads.lpx](plugins/XiaoCan_remove_ads.lpx) |
| 小黑盒去广告 | 移除开屏广告和热点板块信息流广告 | 0 | 0 | [XiaoHeiHe_remove_ads.lpx](plugins/XiaoHeiHe_remove_ads.lpx) |
| 小桔充电去广告 | 移除横幅广告、弹窗广告，精简我的页面。 | 0 | 0 | [XiaojukejiCharge_remove_ads.lpx](plugins/XiaojukejiCharge_remove_ads.lpx) |
| 小米音箱去广告 | 移除开屏广告、应用内横幅广告及弹窗广告。 | 0 | 0 | [XiaomiSpeaker_remove_ads.lpx](plugins/XiaomiSpeaker_remove_ads.lpx) |
| 迅雷去广告 | 移除开屏广告、首页横幅广告、左上角广告入口，精简我的页面。 | 0 | 0 | [XunLei_remove_ads.lpx](plugins/XunLei_remove_ads.lpx) |
| 医考帮去广告 | 移除横幅推广、弹窗、首页悬浮挂件。 | 0 | 0 | [YiKaoBang_remove_ads.lpx](plugins/YiKaoBang_remove_ads.lpx) |
| 易校园去广告 | 移除开屏广告、横幅广告、弹窗广告、悬浮广告、文末广告、消息广告、校园头条，精简首页金刚位和我的页面。 | 0 | 0 | [YiSchool_remove_ads.lpx](plugins/YiSchool_remove_ads.lpx) |
| 一甜相机去广告 | 移除开屏广告、悬浮广告及图片选择器横幅广告。 | 0 | 0 | [Yitian_remove_ads.lpx](plugins/Yitian_remove_ads.lpx) |
| 网易有道词典去广告 | 移除开屏广告、弹窗广告、右上角推广。 | 0 | 0 | [YoudaoDict_remove_ads.lpx](plugins/YoudaoDict_remove_ads.lpx) |
| 有道云笔记去广告 | 移除开屏广告、弹窗广告及横幅广告。 | 0 | 0 | [YoudaoNote_remove_ads.lpx](plugins/YoudaoNote_remove_ads.lpx) |
| 有道翻译官去广告 | 移除开屏广告、横幅推广，精简首页。 | 0 | 0 | [YoudaoTrans_remove_ads.lpx](plugins/YoudaoTrans_remove_ads.lpx) |
| 优酷视频去广告 | 移除开屏广告、视频广告、信息流广告。其余广告由于请求已加密，故无法移除。 | 21 | 0 | [YouKu_Video_remove_ads.lpx](plugins/YouKu_Video_remove_ads.lpx) |
| YouTube去广告 | 移除YouTube视频、瀑布流、搜索和Shorts中的广告，移除底栏的Shorts按钮和上传按钮，增加画… | 0 | 3 | [YouTube_remove_ads.lpx](plugins/YouTube_remove_ads.lpx) |
| 省钱快报去广告 | 移除开屏广告、横幅广告、商品推荐，精简我的页面。 | 0 | 0 | [YueDanBa_remove_ads.lpx](plugins/YueDanBa_remove_ads.lpx) |
| 阅友去广告 | 移除开屏广告、弹窗广告和阅读页面广告，移除底栏福利按钮。 | 1 | 0 | [Yueyou_remove_ads.lpx](plugins/Yueyou_remove_ads.lpx) |
| 好轻去广告 | 移除开屏广告、弹窗广告、横幅推广、商品推广，精简我的页面。 | 0 | 0 | [YunmaiScale_remove_ads.lpx](plugins/YunmaiScale_remove_ads.lpx) |
| YY去广告 | 移除开屏广告、应用内弹窗，精简底栏和我的页面。 | 3 | 0 | [YY_Voice_remove_ads.lpx](plugins/YY_Voice_remove_ads.lpx) |
| YY语音去广告 | 移除开屏广告、应用内弹窗、任务推广、频道横幅推广，精简广场顶部标签。 | 0 | 0 | [YYVoiceTool_remove_ads.lpx](plugins/YYVoiceTool_remove_ads.lpx) |
| ZAKER去广告 | 移除开屏广告、置顶轮播图广告和文末广告。 | 0 | 0 | [ZAKER_remove_ads.lpx](plugins/ZAKER_remove_ads.lpx) |
| 直播吧去广告 | 移除信息流广告、横幅广告、弹窗广告、皮肤配置、悬浮挂件、热门搜索，移除青少年模式，精简我的页面。 | 0 | 0 | [Zhibo8_remove_ads.lpx](plugins/Zhibo8_remove_ads.lpx) |
| 知乎去广告 | 移除HTTPDNS和QUIC传输配置，移除开屏广告、信息流广告、回答页广告，移除回答页下的相关回答、专栏… | 0 | 0 | [Zhihu_remove_ads.lpx](plugins/Zhihu_remove_ads.lpx) |
| 智联招聘去广告 | 移除开屏广告、弹窗、职位页面推广和各类横幅推广。此插件需要IPA签名方可使用，App Store用户请勿… | 1 | 0 | [ZhiLianZhaoPin_remove_ads.lpx](plugins/ZhiLianZhaoPin_remove_ads.lpx) |
| 转转去广告 | 移除开屏广告、应用内悬浮窗、信息流推广、商品推荐、首页弹窗，精简我的页面。 | 0 | 3 | [ZhuanZhuan_remove_ads.lpx](plugins/ZhuanZhuan_remove_ads.lpx) |
| 纵横小说去广告 | 移除纵横小说开屏广告和弹窗 | 0 | 0 | [ZongHeng_remove_ads.lpx](plugins/ZongHeng_remove_ads.lpx) |
| 最右去广告 | 移除开屏广告、信息流广告和广告轮播图。 | 2 | 0 | [ZuiYou_remove_ads.lpx](plugins/ZuiYou_remove_ads.lpx) |

### 功能增强（9）

| 插件 | 说明 | 规则 | 脚本 | 文件 |
|---|---|---|---|---|
| Apple天气增强 | 解锁Apple天气的全部功能、替换空气质量数据源、添加下一小时降水数据、添加天气数据。 | 0 | 2 | [AppleWeatherEnhancer.lpx](plugins/AppleWeatherEnhancer.lpx) |
| Fileball网盘挂载 | 支持挂载阿里云盘、夸克网盘和PikPak网盘，点击下方署名查看使用方法。 | 0 | 1 | [Fileball_mount.lpx](plugins/Fileball_mount.lpx) |
| IPA工具箱助手 | 这是IPA工具箱的辅助插件，用于下载IPA包和应用降级。IPA工具箱是运行在Scripting应用中的脚… | 0 | 2 | [IPATool.lpx](plugins/IPATool.lpx) |
| 京东比价 | 首次使用需安装慢慢买应用，之后点击进入[我的]页面以捕获Cookie，捕获成功后方可在商品详情页面查看比… | 0 | 2 | [JD_Price.lpx](plugins/JD_Price.lpx) |
| Spotify歌词增强 | 将Spotify的外语歌词翻译为简体中文，并提供双语翻译支持。 | 0 | 7 | [Spotify_lyrics_translation.lpx](plugins/Spotify_lyrics_translation.lpx) |
| TestFlight地区解锁 | 解除TestFlight的区域限制，支持tvOS。 | 0 | 0 | [TestFlightRegionUnlock.lpx](plugins/TestFlightRegionUnlock.lpx) |
| VVebo时间线修复 | 修复失效的用户时间线和我的页面。使用此插件前需要禁用微博去广告插件，避免插件冲突导致失效。 | 0 | 5 | [VVebo_repair.lpx](plugins/VVebo_repair.lpx) |
| 微信外部链接解锁 | 解锁微信外部链接访问限制，跳过中间界面。支付宝链接、被封禁链接进行通知弹窗跳转，在微信中用快照显示被封禁… | 0 | 1 | [Weixin_external_links_unlock.lpx](plugins/Weixin_external_links_unlock.lpx) |
| YouTube双语翻译 | 字幕增强及双语翻译，支持Youtube Music歌词翻译。此插件需要置于YouTube去广告插件之下，… | 0 | 12 | [YouTubeSubtitlesTranslation.lpx](plugins/YouTubeSubtitlesTranslation.lpx) |

### 节点检测（3）

| 插件 | 说明 | 规则 | 脚本 | 文件 |
|---|---|---|---|---|
| 节点检测工具 | 适用于Loon的节点检测工具，可进行地理位置、节点解锁、入口落地等查询。请在所有节点页面选择一个节点长按… | 0 | 3 | [Node_detection_tool.lpx](plugins/Node_detection_tool.lpx) |
| 代理链路检测 | 查看目标节点的代理走向，在插件列表中点击此插件上的链接查看使用方法。 | 0 | 1 | [NodeLinkCheck.lpx](plugins/NodeLinkCheck.lpx) |
| WARP节点查询 | 显示WARP节点的详细信息，请在所有节点页面选择一个节点长按，出现菜单后进行测试。 | 0 | 1 | [WARP_Node_Query.lpx](plugins/WARP_Node_Query.lpx) |

### 签到（2）

| 插件 | 说明 | 规则 | 脚本 | 文件 |
|---|---|---|---|---|
| Follow每日签到 | Follow每日签到，需要进入此插件的主页链接，阅读使用说明操作。 | 0 | 1 | [FollowRSS_checkin.lpx](plugins/FollowRSS_checkin.lpx) |
| WPS每日签到 | WPS每日签到并兑换会员，需要进入此插件的主页链接，阅读使用说明操作。 | 0 | 2 | [WPS_checkin.lpx](plugins/WPS_checkin.lpx) |

### 配置管理（1）

| 插件 | 说明 | 规则 | 脚本 | 文件 |
|---|---|---|---|---|
| 1.1.1.1配置管理 | 提取1.1.1.1应用的配置并生成Loon可用的节点配置，点击下面署名前往配置1.1.1.1的BoxJs… | 0 | 4 | [1.1.1.1.lpx](plugins/1.1.1.1.lpx) |

### 定时任务（1）

| 插件 | 说明 | 规则 | 脚本 | 文件 |
|---|---|---|---|---|
| 自动加入TestFlight | 自动监控TestFlight名额，一旦有新的名额即刻加入。 | 0 | 3 | [Auto_Join_TF.lpx](plugins/Auto_Join_TF.lpx) |

### 数据管理（1）

| 插件 | 说明 | 规则 | 脚本 | 文件 |
|---|---|---|---|---|
| BoxJs | JavaScript数据管理器，用于管理脚本储存的数据。使用前请在本插件的详情页面为[PROXY]项分配… | 0 | 1 | [BoxJs.lpx](plugins/BoxJs.lpx) |

### DNS（1）

| 插件 | 说明 | 规则 | 脚本 | 文件 |
|---|---|---|---|---|
| DNS防泄露 | 专为小白设计的DNS防泄露 | 0 | 0 | [Prevent_DNS_Leaks.lpx](plugins/Prevent_DNS_Leaks.lpx) |

### 资源转换（1）

| 插件 | 说明 | 规则 | 脚本 | 文件 |
|---|---|---|---|---|
| Script-Hub | 将其他工具的Rewrite、Rule和JavaScript资源转换为Loon能识别的格式，使用前请在本插… | 0 | 4 | [Script-Hub.lpx](plugins/Script-Hub.lpx) |

### 订阅管理（1）

| 插件 | 说明 | 规则 | 脚本 | 文件 |
|---|---|---|---|---|
| Sub-Store | 高级订阅管理工具，定时任务默认为每天23点55分，可在插件设置中自定义。使用前请在本插件的详情页面为[P… | 0 | 3 | [Sub-Store.lpx](plugins/Sub-Store.lpx) |

### 未分类（1）

| 插件 | 说明 | 规则 | 脚本 | 文件 |
|---|---|---|---|---|
| 知识星球去水印 | 移除内容的水印编号 | 0 | 0 | [UnnooQuan_remove_watermark.lpx](plugins/UnnooQuan_remove_watermark.lpx) |

## 统计

- 插件总数：**275**
- 规则总数（REJECT）：**730**
- 引用脚本的插件：**86**
- 归档资源：**102** 个，12.6 MB

## 定制版（custom/）

`plugins/` 是纯净归档，本地改动一律放 `custom/`，重新抓取上游也不会覆盖。


### Block_HTTPDNS.lpx

- 改动：放行微信 HTTPDNS：移除 dns.weixin.qq.com / dns.weixin.qq.com.cn 拦截，流量按现有分流策略处理
- 移除规则：`DOMAIN, dns.weixin.qq.com, REJECT`
- 移除规则：`DOMAIN, dns.weixin.qq.com.cn, REJECT`
- 安装：`https://raw.githubusercontent.com/Yjwj205/loon-kelee-archive/main/custom/Block_HTTPDNS.lpx`


## 刷新

```bash
cd tools && python3 fetch.py && python3 fetch_res.py && python3 rewrite.py && python3 build_index.py && python3 local_patch.py
```

## 说明

- 插件版权归原作者 **可莉🅥**（[luestr/ProxyResource](https://github.com/luestr/ProxyResource)）所有，本仓库仅为个人备份/学习用途，未做商业化。
- 若原作者认为不妥，提 issue 或联系本人，会立即删除。
- 上游若更新规则，本仓库不会自动同步；需要时跑 `tools/` 下的脚本重新抓。
