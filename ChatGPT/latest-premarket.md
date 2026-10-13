# 2026-10-13 盘前计划／开盘后更新

> 数据截点：2026-10-13 08:20:10 PDT（11:20:10 EDT）；应用户约 08:17 PT 请求开始核实。美股常规交易已于 06:30 PT 开盘，本报告是开盘后更新，不是盘前实时行情。各品种时间不同，期货及部分指数存在约 10–15 分钟延迟；下表逐项列出实际报价时间。报告分析以该截点为止，不包含其后行情。

## 核心判断

已观察到：QQQ、SMH 跌幅大于 SPX，半导体仍拖累成长股；DIA 也低于前收。10 年及 30 年美债收益率回落，但 2 年收益率上升，不能简单描述成“收益率全线下跌”。美元回落，WTI 已从隔夜低位反弹至前收附近，不能继续套用盘前“油价下跌”的结论。

分析：当前更适合等待突破／跌破后回测确认；银行业绩分化、半导体压力与明日 CPI 构成主要变量。低位反弹并不等于趋势反转。以下情景没有预设概率，也不声称触发条件已经发生。

## 开盘后行情快照

来源为 Yahoo Finance chart 接口（链接对应本次读取的品种）；价格、前收与当日区间取同一供应商。涨跌百分比由价格和接口 previousClose 自行计算。指数单位为点，ETF／股票单位为美元，油为美元／桶，金为美元／金衡盎司。期货日内区间可能覆盖隔夜 Globex，不是现金市场开盘区间。

| 品种 | 报价 | 较供应商前收 | 报价时间 PT（10/13） | 已报日内低–高 | 来源 |
|---|---:|---:|---|---|---|
| ES 2026年12月 | 7,843.500 | -0.18% | 08:09:54 | 7,836.000–7,864.000 | [Yahoo](https://query1.finance.yahoo.com/v8/finance/chart/ES%3DF?interval=1m&range=1d) |
| NQ 2026年12月 | 30,702.750 | -0.63% | 08:09:55 | 30,591.750–30,906.000 | [Yahoo](https://query1.finance.yahoo.com/v8/finance/chart/NQ%3DF?interval=1m&range=1d) |
| YM 2026年12月 | 52,042.000 | -0.13% | 08:09:55 | 51,996.000–52,612.000 | [Yahoo](https://query1.finance.yahoo.com/v8/finance/chart/YM%3DF?interval=1m&range=1d) |
| SPX 现货指数 | 7,797.460 | -0.13% | 08:19:35 | 7,793.160–7,814.150 | [Yahoo](https://query1.finance.yahoo.com/v8/finance/chart/%5EGSPC?interval=1m&range=1d) |
| QQQ | 741.630 | -0.59% | 08:19:56 | 738.840–744.200 | [Yahoo](https://query1.finance.yahoo.com/v8/finance/chart/QQQ?interval=1m&range=1d) |
| DIA | 517.150 | -0.15% | 08:19:34 | 516.730–522.780 | [Yahoo](https://query1.finance.yahoo.com/v8/finance/chart/DIA?interval=1m&range=1d) |
| VIX 现货指数 | 15.310 | 前收口径冲突，省略 | 08:04:31 | 15.170–15.610 | [Yahoo](https://query1.finance.yahoo.com/v8/finance/chart/%5EVIX?interval=1m&range=1d) |
| DXY 美元指数 | 102.248 | -0.33% | 08:09:34 | 102.164–102.574 | [Yahoo](https://query1.finance.yahoo.com/v8/finance/chart/DX-Y.NYB?interval=1m&range=1d) |
| WTI 近月期货 | 93.850 | +0.12% | 08:09:35 | 91.700–94.000 | [Yahoo](https://query1.finance.yahoo.com/v8/finance/chart/CL%3DF?interval=1m&range=1d) |
| Brent 近月期货 | 105.770 | -0.83% | 08:09:33 | 104.360–106.270 | [Yahoo](https://query1.finance.yahoo.com/v8/finance/chart/BZ%3DF?interval=1m&range=1d) |
| 黄金近月期货 | 4,189.300 | -0.03% | 08:09:33 | 4,173.700–4,224.800 | [Yahoo](https://query1.finance.yahoo.com/v8/finance/chart/GC%3DF?interval=1m&range=1d) |
| NVDA | 224.776 | -0.68% | 08:19:56 | 223.060–226.600 | [Yahoo](https://query1.finance.yahoo.com/v8/finance/chart/NVDA?interval=1m&range=1d) |
| AMD | 586.810 | -1.25% | 08:19:54 | 570.600–593.240 | [Yahoo](https://query1.finance.yahoo.com/v8/finance/chart/AMD?interval=1m&range=1d) |
| MU | 938.205 | -5.14% | 08:19:51 | 929.030–952.621 | [Yahoo](https://query1.finance.yahoo.com/v8/finance/chart/MU?interval=1m&range=1d) |
| SMH | 580.080 | -1.85% | 08:19:55 | 574.750–584.810 | [Yahoo](https://query1.finance.yahoo.com/v8/finance/chart/SMH?interval=1m&range=1d) |

数据限制：VIX 接口前收为 14.84，公开前日评论存在不同值，因此不报告 VIX 日涨跌；15.31 仅为 08:04:31 PT 的供应商快照，未取得 Cboe 直接复核。另一行情聚合源的 QQQ／DIA 当日高低与 Yahoo 略有差异，技术位统一采用本表，不混合。油金使用滚动近月代码，本次元数据未完整确认具体交割月份，不能将其误称现货，也不可直接用于跨合约下单。ES/NQ/YM 的元数据已明确为 2026 年 12 月合约。

### 美债收益率

| 期限 | 收益率 | 较供应商前收 | 报价时间 PT | 来源 |
|---|---:|---:|---|---|
| 2 年 | 4.808% | +1.7 bp | 08:19:49 | [CNBC / Tradeweb](https://www.cnbc.com/quotes/US2Y) |
| 10 年 | 5.219% | -2.5 bp | 08:20:10 | [CNBC / Tradeweb](https://www.cnbc.com/quotes/US10Y) |
| 30 年 | 5.568% | -3.1 bp | 08:20:10 | [CNBC / Tradeweb](https://www.cnbc.com/quotes/US30Y) |

本次实际读取 [CNBC 报价接口](https://quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol?symbols=US2Y%7CUS10Y%7CUS30Y&requestMethod=itv&output=json)，其 source 为 Exchange、exchange 为 Tradeweb。bp 按收益率与 previous_day_closing 相减计算，不采用接口中可能代表债券价格的百分比字段。Yahoo 的 10 年收益率也为 5.219%，但时间为 08:04:35 PT、前收为 5.240%，不同供应商基准不可混用。

## 盘前背景回顾（已经过时，不是当前报价）

Reuters 盘前报道的明确快照为 06:54 ET／03:54 PT：ES -10 点（-0.13%）、NQ -182.25 点（-0.59%）、YM +92 点（+0.18%）。报道提到中国 CXMT 技术进展相关消息冲击芯片股，NVDA、AMD、MU 当时承压。这是消息驱动的市场解读，未独立验证有关技术的商业效果。当前价格请以上表开盘后时间戳为准。[Reuters / StreetInsider](https://www.streetinsider.com/Market%2BCheck/S%26P%2B500%2Bfutures%2Bmuted%2Bas%2Binvestors%2Bawait%2Bbig%2Bbank%2Bearnings%3B%2Bchip%2Bweakness%2Bweighs/27176483.html)

## 经济日历：已公布与待公布

| 日期／PT（ET） | 事件 | 截点时状态 |
|---|---|---|
| 10/13 07:00（10:00） | 9 月成屋销售 | 已公布：年化 399 万户、环比 +1.5%；不再当作待公布事件 |
| 10/14 05:30（08:30） | 9 月 CPI、实际收入 | 尚未公布，明日主要风险 |
| 10/15 05:30（08:30） | PPI、零售销售、初请失业金、纽约／费城制造业调查 | 尚未公布，密集数据窗口 |
| 10/16 05:30（08:30）；06:15（09:15） | 进出口价格；工业产出 | 尚未公布 |

日程核对：[BLS 10 月日历](https://www.bls.gov/schedule/2026/10_sched_list.htm)、[纽约联储日历](https://www.newyorkfed.org/research/calendars/i-oct26.html)。成屋销售实际值：[NAR](https://www.nar.realtor/research-and-statistics/housing-statistics/existing-home-sales)。未取得可靠完整的今日 Fed 官员发言时间表、NFIB／ADP 实际值及一致预期，故不填入未经证实的时间、数值或“超预期”判断。

## 财报及 AI／半导体

- **JPM 已公布**：Q3 净利润约 153 亿美元，报告口径 EPS 5.57 美元；投行业务及交易支持盈利。不可把媒体出现的调整后 EPS 5.75 与报告口径混为一谈。重点继续核对净利息收入指引、拨备及消费信贷质量。[Reuters 财报报道](https://www.investing.com/news/economy-news/jpmorgans-profit-rises-on-investment-banking-trading-strength-4946101)
- **GS 已公布**：官方首页列出 Q3 EPS 17.01 美元、年化普通股回报率 18.7%。不以盘前股价涨幅替代当前走势。[Goldman Sachs 官方业绩](https://www.goldmansachs.com/investor-relations/financials)
- **WFC／C**：今日银行财报焦点；本次未完成两家公司正式报表及一致预期逐项核对，不给出精确 EPS／营收惊喜幅度。已开盘，不再笼统写成“等待盘前公布”。
- **ASML 10/14**：官方确认 Q3 发布日期；关注订单、EUV 需求与地区结构。**TSMC 10/15 台北 14:00**（10/14 23:00 PT；10/15 02:00 ET）财报会议：关注先进制程、先进封装、毛利率及资本开支指引。[ASML 官方](https://www.investor.asml.com/quarterly-results)、[TSMC 官方日历](https://investor.tsmc.com/english/financial-calendar)
- **开盘后验证**：SMH、MU 相对 QQQ 更弱，不能仅凭 NVDA 离开日低就确认整个 AI 板块转强。观察 SMH 是否收复 584.81、NVDA 是否重回 226.32 前收附近；MU 日低 929.03 是否失守。以上是价格验证条件，并非公司基本面结论。未核实的并购传闻不作为交易依据。

## 关键技术位（截至快照，后续可能变化）

以下来自同一 Yahoo 快照。前收／日内高低是观察位，不保证构成支撑或阻力；未取得完整前日 RTH OHLC 和可靠 VWAP，因此不编造经典 Pivot、均线或 VWAP 数值。

| 品种 | 下方观察位：已报日低 | 中间参考：前收 | 上方观察位：已报日高 |
|---|---:|---:|---:|
| SPX | 7,793.16 | 7,807.24 | 7,814.15 |
| QQQ | 738.84 | 746.04 | 744.20（低于前收） |
| DIA | 516.73 | 517.91 | 522.78 |
| ES Dec26 | 7,836.00 | 7,858.00 | 7,864.00 |
| NQ Dec26 | 30,591.75 | 30,898.25 | 30,906.00 |
| YM Dec26 | 51,996 | 52,110 | 52,612 |

期货区间包含隔夜，不能称为 06:30–06:45 PT 开盘区间。ES 与 SPX 存在基差，NQ 与 QQQ、YM 与 DIA 亦不能按相同点位套用。

## 情景化交易计划（条件推演）

1. **反弹确认**：QQQ 突破 744.20 并回测守住，同时 SPX 收复 7,807.24，SMH 相对强弱改善，才考虑小仓顺势。QQQ 下一观察位为前收 746.04；SPX 上方为 7,814.15。若回测失败并重新跌回突破位，退出该情景。当前未验证 VWAP，执行前须在交易终端确认。
2. **区间震荡**：QQQ 仍在 738.84–744.20、SPX 在 7,793.16–7,814.15 内，且银行与芯片方向分化，避免区间中部追单。只在边界出现明确拒绝／收复信号时考虑交易，目标先看区间中部再看另一边；边界失守即失效。
3. **弱势延续**：QQQ 跌破 738.84 或 SPX 跌破 7,793.16，回抽不能收复，且 SMH／MU 同步走弱，才考虑防守或有风险上限的看空计划。下方无已核实历史支撑，不虚构目标；按实际入场到止损距离，以 1R／2R 分段管理。迅速收复跌破位则取消看空触发。
4. **期货确认**：ES 收复 7,858–7,864、NQ 收复 30,898–30,906 是更强修复条件；ES 失守 7,836、NQ 失守 30,591.75 是弱势确认条件。YM 先观察能否收复 52,110。必须换成终端中的对应 Dec26 合约最新报价后判断，不能用延迟快照直接下单。

风险控制：单笔最大亏损可预先限制为账户净值的 0.25%–0.5%（示例，并非适合所有人的仓位），按实际止损距离计算规模，不摊平亏损。若下一阻力／支撑前不足约 2R 空间则放弃追价。明早 CPI 可造成隔夜跳空，止损并不保证成交价；当天计划与隔夜持仓风险需分开处理。本报告提供情景研究，不提供确定收益承诺。

## 完整性说明

本报告未使用 FinanceDailyReport。所有行情均为公开供应商在上述截点前可取得的最新快照，并非同一秒同步行情；缺失的完整历史 OHLC、成交量分布、VWAP、部分财报细项与日历项目已明确标注。GitHub 上传／网站部署验证另外记录，不以任务启动或运行代替成功证据。
