# Task Progress Skill 中文说明

`task-progress` 是一个平台无关的 Agent Skill，用于让用户清楚知道 AI 正在做什么、已经完成什么，以及下一步是什么。

## 解决的问题

当 AI 编写代码、调查问题或执行多步骤任务时，用户经常不知道：

- 当前处于哪个阶段；
- 哪些工作已经完成；
- 当前正在处理什么；
- 是否遇到了阻塞；
- 修改了哪些文件；
- 下一步会做什么。

这个 Skill 要求 AI 用阶段清单和关键检查点持续同步进度，同时明确说明无法观测的内容，不伪造实时监控。

## 使用方式

将 `SKILL.md` 复制到 Agent 宿主支持的 Skill 目录，或者使用宿主提供的 Skill 管理器安装。它不依赖 Claude Code、Codex、Cursor、OpenAI Agents SDK 或其他特定平台。

用户可以直接询问：

```text
现在做到哪一步了？
请报告当前任务状态。
还有什么没有完成？
```

AI 应使用统一结构回答：

```text
Status: running
Current phase: Implement
Completed: 已完成接口调查并实现参数校验。
In progress: 正在运行针对性测试。
Blocked: none
Changed: src/validation.ts, tests/validation.test.ts
Next: 检查测试结果并运行构建校验。
```

## 设计边界

这是一个进度透明协议，不是进程监控器、Trace 后端或任务调度器。它不能读取宿主未暴露的后台活动，也不能保证真正的实时监控。需要外部监控时，应使用宿主提供的日志、Trace、任务控制或仪表盘。

## 本地验证

在仓库根目录运行：

```bash
python scripts/validate_skill.py
```

预期输出：

```text
skill structure is valid
```
