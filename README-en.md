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
4. **Start the service**.
   ```
   python main.py
   ```
   The system disables the /docs and /redoc directories by default.

5. **Bind a domain name**:
   Please don't forget to bind a domain name after the installation is complete. Domain names are safer and more reliable than IP addresses.
   In the production environment, you can use Nginx, Apache or Caddy to bind the domain name, it is recommended to use Caddy for binding, but you can also choose the http server according to the need.
   Nginx, Apache and Caddy are three commonly used web servers, each with its own advantages and disadvantages.
- **[Nginx](https://nginx.org/)**: Nginx is a good choice if you need high concurrency performance and low memory consumption, especially for handling static content and reverse proxies.
- **[Caddy](https://caddyserver.com/)**: Caddy is a good choice if you want to simplify HTTPS configuration and need an easy-to-configure server.
- **[Apache](https://httpd.apache.org/)**: If you need rich feature and module support, as well as good compatibility, Apache may be a better fit.
   
## License
This project is distributed under [Apache 2.0](LICENSE), please follow the open source License.
