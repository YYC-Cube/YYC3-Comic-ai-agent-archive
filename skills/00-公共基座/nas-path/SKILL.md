---
skill: nas-path
domain: 00-公共基座
owner_agent: 全体（部署脚本）
priority: P0
version: v0.1.0
status: degraded-ok
backing: none（待实现，见依赖）
---

# nas-path

## 触发条件
跨节点读写 NAS 资产前；网关代理请求路径归一

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| path | str | 是 | 任意节点风格路径 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| normalized | str | 归一为 /mnt/nas/ 标准路径 |
| is_nas | bool | 是否 NAS 路径（非 NAS 不篡改） |

## 依赖
manju-studio/scripts/init_nas_path.sh + 0379-world path_normalize 中间件

## 降级模式
无 NAS 挂载时仅做纯函数归一校验（E2E 待网关部署）

## 验收锚点
TC-G1-003/004
