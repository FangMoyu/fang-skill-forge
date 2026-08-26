# 贡献指南

感谢你改进 Fang Skill Forge。

## 目录约定

- 一个 Skill 对应 `skills/` 下的一个独立目录。
- 目录名只能使用小写字母、数字和连字符，并与 `SKILL.md` 中的 `name` 一致。
- 只添加当前 Skill 真正需要的 `agents/`、`references/`、`scripts/` 和 `assets/`。
- 不创建空占位目录，不复制与任务无关的通用资料。

## Skill 要求

- `SKILL.md` 必须包含有效的 YAML Frontmatter。
- `description` 应明确说明适用场景和触发条件。
- Skill 内部资源使用相对路径引用。
- 大段条件性说明放入 `references/`，入口文件保持聚焦。
- 脚本必须能够独立验证，失败时给出明确退出码。

## 安全与真实性

禁止提交：

- 本机绝对路径、个人邮箱、访问令牌、API Key、密码和私钥；
- 私人简历、面试记录、业务项目源码和生成缓存；
- 没有证据支持的个人贡献、生产运行和性能结论。

## 提交前检查

1. 检查Frontmatter、目录名和界面元数据。
2. 检查所有相对链接是否存在且没有越出Skill目录。
3. 对Python脚本执行语法检查和受控冒烟测试。
4. 扫描绝对路径、凭据和私人数据。
5. 运行 `git diff --check` 并检查最终文件清单。

提交信息使用简洁的英文 Conventional Commit 风格，例如：

```text
feat: add a new interview skill
docs: clarify installation instructions
fix: correct a broken reference link
```

