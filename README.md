# SwiftLink: 快速的短链接平台

[🇨🇳中文](README.md) | [🇺🇸English](README-en.md)

![GitHub Stars](https://img.shields.io/github/stars/sengedev/SwiftLink?style=social)
![GitHub License](https://img.shields.io/github/license/sengedev/SwiftLink)

**SwiftLink** 是一个使用 FastAPI 精心打造的高性能短链接平台，旨在快速将冗长的 URL 转换为紧凑、易于共享的链接。非常适合在社交媒体、电子邮件或任何简单与效率相结合的平台上无缝共享。

## 关键作用

- **快速响应**: 利用 FastAPI 的异步处理实现近乎即时的链接创建和重定向。
- **个性化**: 提供可自定义的短 URL 或自动生成，以及用于增强品牌标识的别名。
- **可扩展架构**: 构建灵活，可轻松集成其他服务和未来增强功能。

## 技术栈

**后端**: 由 FastAPI 提供支持，并与 Uvicorn 一起提供卓越的性能。
**数据存储**: 使用 SQLite 存储数据，保证系统的轻量。

## 开始安装

1. **克隆项目**:
   ```
   git clone https://github.com/sengedev/SwiftLink.git
   cd SwiftLink
   ```
2. **环境设置**:
   新建虚拟环境:
   ```
   python -m venv venv
   ```
   激活虚拟环境
   ```
   source venv/bin/activate
   ```
   使用pip安装依赖软件包:
   ```
   pip install -r requirements.txt
   ```
4. **启动服务**:
   ```
   python main.py
   ```
   系统默认禁止/docs和/redoc目录。

5. **绑定域名**：
   安装完成后请不要忘记绑定域名，域名比 IP 地址更安全可靠。
   在生产环境中，可以使用 Nginx、Apache 或 Caddy 绑定域名，建议使用 Caddy 进行绑定，但也可以根据需要选择 http 服务器。
   Nginx、Apache 和 Caddy 是三种常用的网络服务器，各有优缺点。
- **[Nginx](https://nginx.org/)**： 如果需要高并发性能和低内存消耗，特别是处理静态内容和反向代理，Nginx 是一个不错的选择。
- **[Caddy](https://caddyserver.com/)**： 如果希望简化 HTTPS 配置，并需要一个易于配置的服务器，Caddy 是一个不错的选择。
- **[Apache](https://httpd.apache.org/)**： 如果你需要丰富的功能和模块支持，以及良好的兼容性，Apache 可能更适合你。

## 如何使用

本示例使用CURL实现RESTful API，支持用户和短链接的管理。

### 用户管理

1. **创建用户**

```bash
curl --location --request POST 'https://your-domain.com/user' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "<username>",
    "password": "<password>"
}'
```

> 您需要在第一次启动时创建用户，系统只允许创建一个用户。如您忘记密码，您需要手动删除数据库user表中的用户信息后重新请求创建。
> 如果密码为空，系统会生成一个随机密码

2. **修改密码**
```bash
curl --location --request PUT 'https://your-domain.com/user' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "<username>",
    "password": "<password>",
    "new_password": "<new_password>"
}'
```

> 如果新密码为空则生成一个随机密码

### 短链接管理

- 以下为保留字，禁止设置为短链接：`favicon.ico`, `index.html`, `robots.txt`, `sitemap.xml`, `docs`, `redoc`, `user`, `shortlinks`, `shortlink`

1. **获取所有短链接**
```bash
curl --location --request GET 'https://your-domain.com/shortlinks' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "<username>",
    "password": "<password>"
}'
```

2. **创建短链接**
```bash
curl --location --request POST 'https://your-domain.com/shortlink' \
=--header 'Content-Type: application/json' \
--data-raw '{
    "username": "<username>",
    "password": "<password>"，
    "route": "<route>",
    "url": "<http://example.com/long-route>"
}'
```

3. **修改短链接**
```bash
curl --location --request PUT 'https://your-domain.com/shortlink' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "<username>",
    "password": "<password>"，
    "route": "<route>",
    "url": "<http://example.com/long-route>",
    "new-route": "<new-route>",
    "new-url": "<new-url>"
}'
```

4. **删除短链接**
```bash
curl --location --request DELETE 'https://your-domain.com/shortlink' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "<username>",
    "password": "<password>"，
    "route": "<route>"
}'
```

## 协议
本项目在[Apache 2.0](LICENSE)下分发，请遵守开源协议。
