# SwiftLink: The Rapid URL Shortener

[🇨🇳中文](README.md) | [🇺🇸English](README-en.md)

![GitHub Stars](https://img.shields.io/github/stars/sengedev/SwiftLink?style=social)
![GitHub License](https://img.shields.io/github/license/sengedev/SwiftLink)

**SwiftLink** is a high-performance short linking platform crafted using FastAPI to quickly transform long URLs into compact, easy-to-share links. Perfect for seamless sharing on social media, email, or any platform where simplicity meets efficiency.

## Key Roles

- **Fast Response**: Leverages FastAPI's asynchronous processing for near-instant link creation and redirection.
- **Personalisation**: Provides customisable short URLs or auto-generation, as well as aliases for enhanced brand identity.
- **Scalable Architecture**: Built for flexibility, allowing easy integration with additional services and future enhancements.

## Technology Stack

**Backend**: Powered by FastAPI and working with Uvicorn to provide superior performance.
**Data Storage**: Uses SQLite to store data and keep the system lightweight.

## Getting Started with Installation

1. **Clone project**.
   ``
   git clone https://github.com/sengedev/SwiftLink.git
   cd SwiftLink
   cd SwiftLink
2. **Environment setup**.
   Create a new virtual environment.
   ```
   python -m venv venv
   ```
   Activate the virtual environment.
   ```
   source venv/bin/activate
   ```
   Install dependent packages using pip: ``
   ```
   pip install -r requirements.txt
   ```
3. **Start the service**.
   ```
   python main.py
   ```
   The system disables the /docs and /redoc directories by default.

4. **Bind a domain name**:
   Please don't forget to bind a domain name after the installation is complete. Domain names are safer and more reliable than IP addresses.
   In the production environment, you can use Nginx, Apache or Caddy to bind the domain name, it is recommended to use Caddy for binding, but you can also choose the http server according to the need.
   Nginx, Apache and Caddy are three commonly used web servers, each with its own advantages and disadvantages.
- **[Nginx](https://nginx.org/)**: Nginx is a good choice if you need high concurrency performance and low memory consumption, especially for handling static content and reverse proxies.
- **[Caddy](https://caddyserver.com/)**: Caddy is a good choice if you want to simplify HTTPS configuration and need an easy-to-configure server.
- **[Apache](https://httpd.apache.org/)**: If you need rich feature and module support, as well as good compatibility, Apache may be a better fit.

## How to Use

This demo uses curl to implement a RESTful API that supports the management of users and short links. This demo use`https://your-domain.com` as the domain, you should change it to your own domain.

### User Management

1. **Create User**:

```
curl --location --request POST 'https://your-domain.com/user' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "<username>",
    "password": "<password>"
}'
```
> You should create a new user in the first time you started up. System is only allow you to create only one user. If you forget your password, please delete user in user table manually. If password is empty, system will generate a random password.

2. **Change Password**:

```
curl --location --request PUT 'https://your-domain.com/user' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "<username>",
    "password": "<password>",
    "new_password": "<new_password>"
}'
```

> If new password is empty, system will generate a random password as your new password.

### Short Link Management

- The following is reserved and setting up short links is prohibited: `favicon.ico`, `index.html`, `robots.txt`, `sitemap.xml`, `docs`, `redoc`, `user`, `shortlink`, `shortlinks`

1. **Get all Shortlinks**:

```
curl --location --request GET 'https://your-domain.com/shortlinks' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "<username>",
    "password": "<password>"
}'
```

2. **Create New Shortlink**:

```
curl --location --request POST 'https://your-domain.com/shortlink' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "<username>",
    "password": "<password>"，
    "route": "<route>",
    "url": "<http://example.com/long-route>"
}'
```   

3. **Edit a Shortlink**:

```
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

4. **Delete a Shortlink**:

```
curl --location --request DELETE 'https://your-domain.com/shortlink' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "<username>",
    "password": "<password>"，
    "route": "<route>"
}'
```

## License
This project is distributed under [Apache 2.0](LICENSE), please follow the open source License.
