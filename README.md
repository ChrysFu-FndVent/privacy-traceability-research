<a id="readme-top"></a>

<p align="center">
  <img src="assets/readme/privacy-traceability-research-banner.svg" alt="Privacy Traceability Research banner" width="100%" />
</p>

# Privacy Traceability Research

Research workflow notes with a standard-library hash-chain integrity demonstration.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-15803D?style=flat)](LICENSE)
[![Release](https://img.shields.io/github/v/release/ChrysFu/privacy-traceability-research?style=flat)](https://github.com/ChrysFu/privacy-traceability-research/releases)

<div align="right"><a href="#简体中文">简体中文</a> | <a href="#english">English</a></div>

<details>
<summary>目录 / Table of Contents</summary>

- [简体中文](#简体中文)
- [English](#english)

</details>

<a id="简体中文"></a>

## 简体中文

### 项目简介

本仓库收录隐私可追溯主题的研究工作流、实验模块设计、Prompt、产品化与数据分析材料。`src/integrity_demo.py` 是一个最小哈希链完整性演示，不是未公开研究原型，也不实现完整的双链架构、密钥管理或业务验真系统。

### 仓库内容

| 内容 | 文件 |
|---|---|
| 研究问题、方案比较与评估流程 | [`workflows.md`](workflows.md) |
| 实验模块设计 | [`skills.md`](skills.md) |
| AI 辅助科研 Prompt | [`prompt-engineering.md`](prompt-engineering.md) |
| 状态机、验真流程与分析材料 | [`product-design.md`](product-design.md)、[`data-analysis.md`](data-analysis.md) |
| 哈希链完整性演示 | [`src/integrity_demo.py`](src/integrity_demo.py) |

### 研究流程

![隐私溯源研究流程图](assets/readme-architecture.svg)

仓库把研究问题、方案比较、实验模块、完整性演示和结果分析串联起来。图中流程用于组织验证工作，不表示已经实现生产级双链系统。

### 环境与安装

- Python 3.10 或更高版本
- 不需要第三方 Python 包
- Git 仅在克隆仓库时需要

```bash
git clone https://github.com/ChrysFu/privacy-traceability-research.git
cd privacy-traceability-research
python3 --version
```

项目直接使用 Python 标准库运行，因此不需要安装额外依赖。

### 使用

运行内置自检：

```bash
python3 src/integrity_demo.py --self-test
```

运行完整演示：

```bash
python3 src/integrity_demo.py
```

演示会按稳定 JSON 编码计算链式 SHA-256 哈希，并在记录载荷被修改后报告首个失效位置。

### 验证

```bash
python3 -m compileall -q src
python3 src/integrity_demo.py --self-test
```

### 下载与发布

GitHub Release 提供自动生成的源码 ZIP 和 TAR.GZ。该仓库目前不提供独立应用、容器镜像或安装程序；研究材料和演示脚本下载后即可本地使用。

### 研究与安全边界

- 演示用于理解完整性校验，不提供生产级签名、密钥管理、零知识证明或智能合约。
- 研究结论、性能和业务可行性必须通过独立实验验证。
- 不要把演示记录视为真实业务记录、隐私保证或合规证明。

### 许可证

本项目采用 [MIT License](LICENSE)。

<p align="right"><a href="#readme-top">返回顶部</a></p>

<a id="english"></a>

## English

### Overview

This repository collects research workflows, experiment-module designs, prompts, productization notes, and analysis material for privacy traceability. `src/integrity_demo.py` is a minimal hash-chain integrity demonstration, not an unpublished research prototype or a complete dual-chain, key-management, or business-verification system.

### Repository contents

| Content | File |
|---|---|
| Research questions, solution comparison, and evaluation flow | [`workflows.md`](workflows.md) |
| Experiment-module design | [`skills.md`](skills.md) |
| AI-assisted research prompts | [`prompt-engineering.md`](prompt-engineering.md) |
| State-machine, verification-flow, and analysis material | [`product-design.md`](product-design.md), [`data-analysis.md`](data-analysis.md) |
| Hash-chain integrity demonstration | [`src/integrity_demo.py`](src/integrity_demo.py) |

### Research workflow

![Privacy traceability research workflow](assets/readme-architecture.svg)

The repository connects research questions, solution comparison, experiment modules, the integrity demonstration, and result analysis. The workflow organizes validation work and does not claim that a production dual-chain system has been implemented.

### Prerequisites and installation

- Python 3.10 or later
- No third-party Python packages
- Git is only required when cloning the repository

```bash
git clone https://github.com/ChrysFu/privacy-traceability-research.git
cd privacy-traceability-research
python3 --version
```

The project runs directly on the Python standard library, so no dependency installation is required.

### Usage

Run the built-in self-test:

```bash
python3 src/integrity_demo.py --self-test
```

Run the complete demonstration:

```bash
python3 src/integrity_demo.py
```

The demonstration computes chained SHA-256 hashes over canonical JSON and reports the first invalid position after a record payload changes.

### Validation

```bash
python3 -m compileall -q src
python3 src/integrity_demo.py --self-test
```

### Downloads and releases

GitHub Releases provides automatically generated source ZIP and TAR.GZ archives. The repository does not currently publish a standalone application, container image, or installer; download the research material and demonstration script to use them locally.

### Research and safety boundary

- The demonstration explains integrity checks; it does not provide production signatures, key management, zero-knowledge proofs, or smart contracts.
- Research conclusions, performance, and business feasibility require independent experiments.
- Do not treat demonstration records as real business records, a privacy guarantee, or compliance evidence.

### License

This project is licensed under the [MIT License](LICENSE).

<p align="right"><a href="#readme-top">Back to top</a></p>
