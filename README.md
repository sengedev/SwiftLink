# SwiftLink: 快速且便捷的短链接平台

[🇨🇳中文](README.md) | [🇺🇸English](README-en.md)

![GitHub Stars](https://img.shields.io/github/stars/sengedev/SwiftLink?style=social)
![GitHub License](https://img.shields.io/github/license/sengedev/SwiftLink)

**SwiftLink** 是一个使用 FastAPI 精心打造的高性能短链接平台，旨在快速将冗长的 URL 转换为紧凑、易于共享的链接。非常适合在社交媒体、博客或任何简单与效率相结合的平台上无缝共享。SwiftLink 将 URL 的精简作为首要目标。

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
   进入到server目录
   ```
   cd server
   ```
   使用pip安装依赖软件包:
   ```
   pip install -r requirements.txt
   ```
4. **启动服务**:
    ```
    uvicorn run main:app --reload host=0.0.0.0 port=8000
    ```
   系统默认禁止/docs和/redoc目录。

5. **绑定域名**：
   安装完成后请不要忘记绑定域名，因为域名相对于 IP 地址更加的安全可靠。
   在生产环境中，可以使用 Nginx、Apache 或 Caddy 绑定域名。
   建议使用 Caddy 进行绑定，但也可以根据需要选择 http 服务器。
   Nginx、Apache 和 Caddy 是三种常用的网络服务器，各有优缺点。
- **[Nginx](https://nginx.org/)**： 如果需要高并发性能和低内存消耗，特别是处理静态内容和反向代理，Nginx 是一个不错的选择。
- **[Caddy](https://caddyserver.com/)**： 如果希望简化 HTTPS 配置，并需要一个易于配置的服务器，Caddy 是一个不错的选择。
- **[Apache](https://httpd.apache.org/)**： 如果你需要丰富的功能和模块支持，以及良好的兼容性，Apache 可能更适合你。

## 如何使用

本示例使用CURL实现RESTful API，同时也支持使用PyQt编写的APP来帮助用户完成短链接的管理操作。

为了安全，本系统默认禁用/docs和/redoc目录，您可以按需开启，但是不建议开启docs和redoc。

### 基本信息
- 基础URL: `https://examp.le`
- 认证方式: HTTP Basic Auth

### 用户管理

#### 1. 用户认证

> 请求
> - 方法: `GET`
> - URL: `https://examp.le/user`

> 响应
> - 成功: `200 OK`
> - 失败: `401 Unauthorized` 或其他错误状态码

- 示例
```bash
curl -u <username>:<password> https://examp.le/user
```

#### 2. 创建用户

> 请求
> - 方法: `POST`
> - URL: `https://examp.le/user`

> 响应
> - 成功: `201 Created`
> - 失败: `400 Bad Request` 或其他错误状态码

- 示例
```bash
curl -X POST -u <username>:<password> https://examp.le/user
```

#### 3. 更改密码

> 请求
> - 方法: `PUT`
> - URL: `https://examp.le/user`
> - Headers: 
>   - `new-password`: 新密码

> 响应
> - 成功: `200 OK`
> - 失败: `400 Bad Request` 或其他错误状态码

- 示例
```bash
curl -X PUT -u <username>:<password> -H "new-password: <newpassword>" https://examp.le/user
```

### 短链接管理

#### 1. 获取短链接列表

> 请求
> - 方法: `GET`
> - URL: `https://examp.le/shortlinks`

> 响应
> - 成功: `200 OK`，返回短链接列表的JSON数据
> - 失败: `401 Unauthorized` 或其他错误状态码

- 示例
```bash
curl -u <username>:<password> https://examp.le/shortlinks
```

#### 2. 创建短链接

> 请求
> - 方法: `POST`
> - URL: `https://examp.le/shortlink`
> - 参数:
>   - `route`: 短链接路由
>   - `url`: 原始URL

> 响应
> - 成功: `200 Created`
> - 失败: `400 Bad Request` 或其他错误状态码

- 示例
```bash
curl -X POST -u <username>:<password> "https://examp.le/shortlink?route=<myroute>&url=<https://original.url>"
```

#### 3. 删除短链接

> 请求
> - 方法: `DELETE`
> - URL: `https://examp.le/shortlink`
> - 参数:
>   - `route`: 短链接路由

> 响应
> - 成功: `200 OK`
> - 失败: `400 Bad Request` 或其他错误状态码

- 示例
```bash
curl -X DELETE -u <username>:<password> "https://examp.le/shortlink?route=<myroute>"
```

#### 4. 更新短链接

> 请求
> - 方法: `PUT`
> - URL: `https://examp.le/shortlink`
> - 参数:
>   - `route`: 原短链接路由
>   - `new_route`: 新短链接路由
>   - `new_url`: 新原始URL

> 响应
> - 成功: `200 OK`
> - 失败: `400 Bad Request` 或其他错误状态码

- 示例
```bash
curl -X PUT -u <username>:<password> "https://examp.le/shortlink?route=<myroute>&new_route=<newroute>&new_url=<https://new.url>"
```

### 注意事项
- 所有请求都需要进行基本身份验证。
- 所有请求的响应都应该进行状态码检查，以确保请求成功。
- 更改密码后需要更新会话中的密码信息。

## 协议
本项目在[Apache 2.0](LICENSE)下分发，请遵守开源协议。
