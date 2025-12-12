# TrySQL

A lightweight web-based SQL shell built with **Flask** and **SQLite**.  
This project provides a browser-accessible interface to run SQL queries, view results, and manage a local SQLite database.



## 🚀 Features
- Web interface for executing SQL queries
- Built with Flask (Python microframework)
- Uses SQLite as the database backend
- Simple, minimal UI for query input and result display
- Error handling for invalid queries
- Easily extensible for authentication, multiple databases, or advanced features


## 📂 Project Structure
```
```




## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/abhijit-71/TrySQL.git

   cd TrySQL

   python3 -m venv venv

   source venv/bin/activate   # On Linux/Mac

   venv\Scripts\activate      # On Windows

   pip install -r requirements.txt
   ```



## 📝 Usage
- Enter SQL queries into the text box (e.g., `SELECT * FROM users;`).
- Results will be displayed in a table format.
- Errors will be shown if the query is invalid.



## 📦 Dependencies
- Flask  
- SQLite (built-in with Python)  
- Jinja2 (bundled with Flask)  



## 🔒 Security Notes
This shell executes raw SQL queries — **do not expose it publicly without authentication**.

For production, consider:
- Adding user authentication  
- Restricting query types  
- Using parameterized queries to prevent injection  



## 🌱 Future Improvements
- User authentication and role-based access  
- Support for multiple databases  
- Query history and saved queries  
- Export results to CSV/JSON  
- Syntax highlighting in the query editor  



## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to add.

