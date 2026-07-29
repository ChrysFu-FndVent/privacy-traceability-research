# 隐私溯源研究工具包

<div align="center">

`trust model` · `dual-chain architecture` · `privacy proof` · `evidence boundary`

![Type](https://img.shields.io/badge/Type-Research%20Toolkit-1D4ED8?style=flat-square)
![Prototype](https://img.shields.io/badge/Evidence-Single--Machine%20Prototype-7C3AED?style=flat-square)
![Security](https://img.shields.io/badge/Security-Not%20Audited-B91C1C?style=flat-square)
![Disclosure](https://img.shields.io/badge/Disclosure-Boundaries%20Explicit-0F766E?style=flat-square)

[研究流程](./workflows.md) · [实验模块](./skills.md) · [科研 Prompt](./prompt-engineering.md) · [产品化设计](./product-design.md) · [数据与限制](./data-analysis.md)

</div>

> [!WARNING]
> 本仓库发布的是**研究方法、实验模块规格和结果记录**，不是经过安全审计的区块链或零知识证明实现。仓库不包含论文实验的 Python 源码，不能直接运行或用于生产。

## 研究简介

多方溯源需要同时回答两类问题：记录怎样跨主体互信，敏感原始值怎样在不公开的前提下被验证。本工具包从参与方、信任缺口和披露规则出发，设计联盟主链与隐私侧链，再用哈希、签名、Merkle、承诺/范围证明和状态机的单机原型验证关键技术原语。

| 研究输入 | 研究输出 |
|---|---|
| 参与方、业务状态、信任假设、敏感字段、允许披露内容、实验环境 | 双链架构、权限与状态机、实验模块、性能记录、反向测试和生产差距 |

## 核心问题

- 谁可以写入、背书、查询和纠错？
- 哪些记录需要多方共享，哪些原始值不能公开？
- 验证者需要知道原值，还是只需知道“值在允许区间内”？
- 业务状态如何防止非法跳转、越权调用和历史改写？
- 单机实验能够支撑哪些主张，不能外推哪些生产结论？

## 架构亮点

### 公开验证与隐私数据分层

```mermaid
flowchart LR
    subgraph P["隐私侧链 / 受控数据域"]
        RAW["原始敏感数据"] --> COMMIT["承诺与范围证明材料"]
        RAW --> POLICY["访问策略与授权记录"]
    end

    subgraph M["联盟主链 / 多方共享域"]
        STATE["业务状态机"] --> RECORD["批次与流转记录"]
        SIGN["多方签名"] --> RECORD
        ROOT["Merkle Root / 哈希锚点"] --> RECORD
    end

    COMMIT --> VERIFY["不披露原值的条件验证"]
    VERIFY --> RECORD
    POLICY -.授权审计.-> VERIFY
    RECORD --> USER["消费者 / 监管方验真结论"]
```

### 验真路径

```mermaid
sequenceDiagram
    participant U as 验证者
    participant A as 验真接口
    participant M as 联盟主链
    participant P as 隐私证明服务
    U->>A: 提交批次或商品标识
    A->>M: 校验哈希、签名、成员关系与状态
    M-->>A: 返回共享记录验证结果
    A->>P: 验证范围证明（不请求原值）
    P-->>A: 返回 true / false 与证明状态
    A-->>U: 展示可理解的验真结论与异常原因
```

## 效果展示

### 研究任务配置

```yaml
scenario: 多方参与的定制商品生产与流转
participants: [原料方, 生产方, 质检方, 物流方, 销售方, 用户, 监管方]
trust_gaps: [记录可能被改写, 多方记录难互认]
sensitive_data: [用户原始测量数据]
allowed_disclosure: [是否在允许区间, 批次状态, 多方背书结果]
state_transitions: 原料 -> 生产 -> 质检 -> 流转 -> 销售或召回
prototype_scope: [哈希链, 签名, Merkle, 承诺与范围证明, 状态机]
excluded_claims: [生产吞吐, 端到端延迟, 安全审计结论, ROI]
```

### 可公开实验记录

| 数据 | 证据支持的含义 | 不能推导的结论 |
|---|---|---|
| **0.173 ms** | Python 单机模拟中的联盟链单笔交易验证耗时 | 分布式生产网络端到端延迟 |
| **0.583 ms** | Python 单机模拟中加入零知识证明后的验证耗时 | 完整扫码体验或生产吞吐 |
| **约 620 万元 / 2–3 年** | 引用资料中的传统跨机构对账成本与周期基线 | 区块链方案节省额或投资回收期 |

## 功能与研究模块

| 模块 | 验证目标 | 反向测试 |
|---|---|---|
| 哈希链完整性 | 历史记录修改是否可被发现 | 篡改任意记录 |
| ECDSA 多方签名 | 背书主体与内容是否一致 | 错误签名、替换消息 |
| Merkle 轻验证 | 单条记录是否属于某批次 | 伪造路径或叶子 |
| 状态机模拟 | 状态转换与角色权限是否有效 | 非法跳转、越权调用 |
| 承诺与范围证明 | 不公开原值时验证区间条件 | 错误证明、越界值 |
| 端到端基准 | 记录组合原语后的单机耗时 | 不同规模与重复运行 |

模块规格见 [skills.md](./skills.md)，状态机和消费者体验见 [product-design.md](./product-design.md)。

## 研究技术栈

| 领域 | 研究对象 |
|---|---|
| 数据完整性 | Hash chain、Merkle tree |
| 身份与背书 | ECDSA 数字签名、多方验证 |
| 隐私证明 | Commitment、范围证明、零知识思想 |
| 业务约束 | 智能合约状态机、RBAC 权限 |
| 原型环境 | Python 单机实验（源码未在本仓库发布） |
| 研究协作 | 文献矩阵、AI 三级信任、反向测试、边界审计 |
| 文档表达 | Markdown、YAML、Mermaid |

## 安装与阅读

```bash
git clone https://github.com/ChrysFu-FndVent/privacy-traceability-research.git
cd privacy-traceability-research
```

本仓库无需安装依赖，推荐按研究问题而非文件名顺序阅读：

1. 从 [workflows.md](./workflows.md) 形式化信任、完整性、隐私和效率问题。
2. 用 [product-design.md](./product-design.md) 查看 8 状态生命周期、7 类权限和 5 个接口。
3. 按 [skills.md](./skills.md) 将架构主张映射到六类实验模块。
4. 用 [data-analysis.md](./data-analysis.md) 检查实验环境、数字口径和生产差距。
5. 参考 [prompt-engineering.md](./prompt-engineering.md) 管理 AI 辅助科研的证据等级。

如需复现实验，应根据模块规格在独立环境重建代码、固定依赖版本并补充安全评审；不要把文档中的模块名当成已发布脚本路径。

## 项目结构

```text
privacy-traceability-research/
├── README.md              # 研究入口、证据边界与 FAQ
├── workflows.md           # 从业务痛点到可验证结论的研究流程
├── skills.md              # 六个 Python 实验模块的规格拆解
├── prompt-engineering.md  # AI 辅助科研的 Prompt 与信任分级
├── product-design.md      # 状态机、RBAC 与消费者验真体验
└── data-analysis.md       # 单机基准、问题基线与生产差距
```

## FAQ

<details>
<summary><strong>为什么仓库里没有 <code>.py</code> 文件？</strong></summary>

公开内容定位为研究工具包，保留实验目标、模块关系、结果与边界，不发布原实验源码。因此安装后不能直接执行 `python` 命令，README 也不会虚构不存在的入口。
</details>

<details>
<summary><strong>0.173 ms 和 0.583 ms 能代表线上性能吗？</strong></summary>

不能。它们只属于指定 Python 单机模拟路径，未包含网络、共识、存储、节点治理、接口和终端渲染时间。
</details>

<details>
<summary><strong>原始敏感数据会上链吗？</strong></summary>

设计目标是不让原始敏感值进入公开共享域，只保存必要的承诺、证明或哈希材料。具体系统仍需做数据最小化、访问控制、密钥管理和隐私影响评估。
</details>

<details>
<summary><strong>可以将这里的密码学方案直接投入生产吗？</strong></summary>

不可以。生产实现需要密码学专家复核、安全审计、密钥生命周期设计、依赖审查、攻击测试和治理方案。
</details>

## 证据与安全边界

- 性能数字必须同时记录环境、数据规模和运行方式。
- 篡改、错误签名、非法状态跳转和越权调用必须有反向测试。
- 论文主张、原型证据和生产假设必须分别标注。
- 原始敏感值不上共享链，公开材料不得反推出原值。
- 成本基线不能直接转写为方案收益或 ROI。

---

<div align="center">

[浏览其他独立 AI 产品项目](https://github.com/ChrysFu-FndVent?tab=repositories)

</div>
