# 共享对照成本的分粒度事实分摊仓

联合实验费用、合作单位用量与跨池凭证交换，分为无外部账务连接的本地资料。

## 资料

来源记录使用 UTF-8 JSON Lines，每行有交付次序 `step`、记录类型 `kind` 和载荷 `body`。按交付次序阅读 `data/exchanges.jsonl`，字段说明见 `data/字典.md`。

## 校验原件

使用 Python 3.11。在项目根目录运行：

```sh
python3 -m unittest discover -s tests -v
```
