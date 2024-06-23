Here is the translated document:

---

# SwiftLink: A Fast URL Shortening Platform

[🇨🇳中文](README.md) | [🇺🇸English](README-en.md)

![GitHub Stars](https://img.shields.io/github/stars/sengedev/SwiftLink?style=social)
![GitHub License](https://img.shields.io/github/license/sengedev/SwiftLink)

**SwiftLink** is a high-performance URL shortening platform meticulously crafted using FastAPI, designed to quickly convert lengthy URLs into compact, easy-to-share links. Ideal for seamless sharing on social media, blogs, or any platform where simplicity and efficiency converge. SwiftLink prioritizes URL shortening.

## Key Features

- **Fast Response**: Achieves near-instantaneous link creation and redirection utilizing FastAPI's asynchronous processing.
- **Customization**: Offers customizable short URLs or auto-generation, along with aliases for enhanced brand identity.
- **Scalable Architecture**: Built to be flexible, allowing easy integration of other services and future enhancements.

## Tech Stack

**Backend**: Powered by FastAPI, providing excellent performance with Uvicorn.
**Data Storage**: Uses SQLite for data storage, ensuring a lightweight system.

## Installation

1. **Clone the Project**:
   ```
   git clone https://github.com/sengedev/SwiftLink.git
   cd SwiftLink
   ```
2. **Environment Setup**:
   Create a virtual environment:
   ```
   python -m venv venv
   ```
   Activate the virtual environment:
   ```
   source venv/bin/activate
   ```
   Install required packages using pip:
   ```
   pip install -r requirements.txt
   ```
4. **Start the Service**:
   ```
   python main.py
   ```
   By default, the /docs and /redoc directories are disabled.

5. **Domain Binding**:
   After installation, don’t forget to bind a domain, as it is safer and more reliable than using an IP address. In a production environment, you can use Nginx, Apache, or Caddy to bind the domain. Caddy is recommended, but you can choose the HTTP server based on your needs. Nginx, Apache, and Caddy are three common web servers, each with its own advantages and disadvantages.
- **[Nginx](https://nginx.org/)**: If you need high concurrency performance and low memory consumption, especially for handling static content and reverse proxy, Nginx is a good choice.
- **[Caddy](https://caddyserver.com/)**: If you want to simplify HTTPS configuration and need an easy-to-configure server, Caddy is a good choice.
- **[Apache](https://httpd.apache.org/)**: If you need rich functionality and module support, as well as good compatibility, Apache might be more suitable.

## Usage

This example uses CURL to implement the RESTful API and also supports an APP written in PyQt to help users manage short links.

For security, the system disables the /docs and /redoc directories by default. You can enable them as needed, but it is not recommended.

### Basic Information
- Base URL: `https://examp.le`
- Authentication: HTTP Basic Auth

### User Management

#### 1. User Authentication

> Request
> - Method: `GET`
> - URL: `https://examp.le/user`

> Response
> - Success: `200 OK`
> - Failure: `401 Unauthorized` or other error codes

- Example
```bash
curl -u <username>:<password> https://examp.le/user
```

#### 2. Create User

> Request
> - Method: `POST`
> - URL: `https://examp.le/user`

> Response
> - Success: `201 Created`
> - Failure: `400 Bad Request` or other error codes

- Example
```bash
curl -X POST -u <username>:<password> https://examp.le/user
```

#### 3. Change Password

> Request
> - Method: `PUT`
> - URL: `https://examp.le/user`
> - Headers:
>   - `new-password`: New password

> Response
> - Success: `200 OK`
> - Failure: `400 Bad Request` or other error codes

- Example
```bash
curl -X PUT -u <username>:<password> -H "new-password: <newpassword>" https://examp.le/user
```

### URL Shortening Management

#### 1. Get Short Link List

> Request
> - Method: `GET`
> - URL: `https://examp.le/shortlinks`

> Response
> - Success: `200 OK`, returns JSON data of the short link list
> - Failure: `401 Unauthorized` or other error codes

- Example
```bash
curl -u <username>:<password> https://examp.le/shortlinks
```

#### 2. Create Short Link

> Request
> - Method: `POST`
> - URL: `https://examp.le/shortlink`
> - Parameters:
>   - `route`: Short link route
>   - `url`: Original URL

> Response
> - Success: `200 Created`
> - Failure: `400 Bad Request` or other error codes

- Example
```bash
curl -X POST -u <username>:<password> "https://examp.le/shortlink?route=<myroute>&url=<https://original.url>"
```

#### 3. Delete Short Link

> Request
> - Method: `DELETE`
> - URL: `https://examp.le/shortlink`
> - Parameters:
>   - `route`: Short link route

> Response
> - Success: `200 OK`
> - Failure: `400 Bad Request` or other error codes

- Example
```bash
curl -X DELETE -u <username>:<password> "https://examp.le/shortlink?route=<myroute>"
```

#### 4. Update Short Link

> Request
> - Method: `PUT`
> - URL: `https://examp.le/shortlink`
> - Parameters:
>   - `route`: Original short link route
>   - `new_route`: New short link route
>   - `new_url`: New original URL

> Response
> - Success: `200 OK`
> - Failure: `400 Bad Request` or other error codes

- Example
```bash
curl -X PUT -u <username>:<password> "https://examp.le/shortlink?route=<myroute>&new_route=<newroute>&new_url=<https://new.url>"
```

### Notes
- All requests require basic authentication.
- All request responses should check the status code to ensure the request was successful.
- After changing the password, update the password information in the session.

## License
This project is distributed under the [Apache 2.0](LICENSE) license, please comply with the open-source license.

---