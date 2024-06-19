# SwiftLink: The Rapid URL Shortener

![GitHub Stars](https://img.shields.io/github/stars/sengedev/SwiftLink?style=social)
![GitHub License](https://img.shields.io/github/license/sengedev/SwiftLink)

**SwiftLink** is a high-performance URL shortening platform crafted with FastAPI, engineered to swiftly convert lengthy URLs into compact, share-friendly links. Ideal for seamless sharing across social media, emails, or any platform where simplicity meets efficiency.

## Key Attributes

- **Rapid Response**: Harnesses FastAPI's asynchronous processing for near-instantaneous link creation and redirection.
- **User-Friendly Interface**: Intuitive API endpoints facilitate effortless link shortening, management, and analytics retrieval.
- **Personalization**: Offers customizable short URLs or auto-generation, plus aliasing for enhanced brand identity.
- **In-depth Analytics**: Monitor link traffic with detailed analytics, including click counts, geographical distribution, and more.
- **Secure by Design**: Implements robust security measures to safeguard against misuse and ensure safe browsing experiences.
- **Scalable Architecture**: Built for flexibility, allowing easy integration with additional services and future enhancements.

## Technology Stack

- **Backend**: Powered by [FastAPI](https://fastapi.tiangolo.com/) and served with [Uvicorn](https://www.uvicorn.org/) for superior performance.
- **Data Storage**: Utilizes [SQLite](https://sqlite.org/).
- **Documentation**: Seamless API documentation with [Swagger UI](https://swagger.io/tools/swagger-ui/) integrated within FastAPI.

## Getting Started

1. **Clone the Repository**:
   ```
   git clone https://github.com/sengedev/SwiftLink.git
   ```
2. **Environment Setup**:
   Install dependencies via Poetry:
   ```
   poetry install
   ```
   Alternatively, use pip:
   ```
   pip install -r requirements.txt
   ```
3. **Launch the Server**:
   ```
   uvicorn main:app --reload
   ```
   Access `http://127.0.0.1:8000/docs` to interact with the live API documentation.

## License

Distributed under the [Apache v2.0 License](./LICENSE).
