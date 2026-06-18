# 🚀 DB Admin Portal
 
A Role-Based Database Administration Portal built using **Python, Streamlit, SQLAlchemy ORM, and MySQL**.
 
The application enables administrators and authorized users to manage database tables, perform CRUD operations, control user permissions, maintain audit logs, and analyze data using an AI-powered SQL assistant.
 
---
 
## 📌 Features
 
### 🔐 Authentication & Authorization
- Secure Login System
- Password Hashing using bcrypt
- Session Management
- Role-Based Access Control (RBAC)
 
### 👥 User Roles
 
#### Admin
- Full system access
- Manage users
- Manage permissions
- Insert, Update, Delete records
- View audit logs
 
#### Editor
- View data
- Insert records
- Update records
- Access based on assigned permissions
 
#### Viewer
- Read-only access
- View tables and records
 
---
 
## 🗄 Database Features
 
### Dynamic Table Reflection
- Automatically detects database schema
- No hardcoded table definitions
- Dynamic form generation
 
### CRUD Operations
- Create Records
- Read Records
- Update Records
- Delete Records
 
### Supported Data Types
- Integer
- Float
- String
- Date
- DateTime
- Boolean / TINYINT(1)
 
---
 
## 📊 Data Viewer
 
- Dynamic table selection
- Data browsing
- Search and filtering support
- Pandas integration
 
---
 
## 🔑 Permission Management
 
Admins can manage table-level permissions:
 
- SELECT
- INSERT
- UPDATE
- DELETE
 
Permissions are stored and enforced throughout the application.
 
---
 
## 📝 Audit Logging
 
Tracks important system activities:
 
- User Login
- Record Insert
- Record Update
- Record Delete
 
All activities are stored in the audit log table.
 
---
 
## 🤖 AI Data Analyst (In Progress)
 
Natural Language to SQL functionality using OpenRouter API.
 
### Example Queries
 
```text
Show top 5 highest salary employees
 
Average salary by department
 
Highest paid employee
 
How many active users exist?
 
Show employees earning more than 50000
```
 
### AI Workflow
 
```text
User Question
      ↓
Database Schema
      ↓
OpenRouter LLM
      ↓
Generated SQL
      ↓
SQL Validation
      ↓
Query Execution
      ↓
Result Display
      ↓
AI Explanation
```
 
### Security Layer
 
Only SELECT queries are allowed.
 
Blocked SQL Commands:
 
```sql
INSERT
UPDATE
DELETE
DROP
ALTER
TRUNCATE
CREATE
```
 
This ensures AI can analyze data but cannot modify it.
 
---
 
## 🛠 Tech Stack
 
| Technology | Usage |
|------------|--------|
| Python 3.11 | Backend |
| Streamlit | Web Interface |
| SQLAlchemy ORM | Database Layer |
| MySQL 8.0 | Database |
| Pandas | Data Processing |
| bcrypt | Password Hashing |
| Requests | API Calls |
| OpenRouter API | AI Assistant |
| OpenPyXL | Excel Export |
 
---
 
## 📂 Project Structure
 
```text
DB_Admin_Portal/
│
├── app.py
│
├── auth/
│   ├── login.py
│   ├── permissions.py
│   └── session.py
│
├── database/
│   ├── connection.py
│   ├── reflection.py
│   ├── models.py
│   ├── session.py
│   └── base.py
│
├── crud/
│   ├── create.py
│   ├── read.py
│   ├── update.py
│   └── delete.py
│
├── views/
│   ├── dashboard.py
│   ├── tables_page.py
│   ├── data_viewer.py
│   ├── insert_page.py
│   ├── update_page.py
│   ├── delete_page.py
│   ├── users_page.py
│   ├── permissions_page.py
│   ├── logs_page.py
│   └── ai_chat_page.py
│
├── ai/
│   ├── openrouter_client.py
│   ├── sql_generator.py
│   └── sql_validator.py
│
├── services/
│   ├── logging_service.py
│   ├── export_service.py
│   ├── bulk_service.py
│   └── table_service.py
│
├── tests/
├── requirements.txt
├── .env.example
└── README.md
```
 
---
 
## ⚙ Installation
 
### Clone Repository
 
```bash
git clone https://github.com/your-username/DB_Admin_Portal.git
cd DB_Admin_Portal
```
 
### Create Virtual Environment
 
```bash
python -m venv venv
```
 
### Activate Environment
 
Windows:
 
```bash
venv\Scripts\activate
```
 
Linux/Mac:
 
```bash
source venv/bin/activate
```
 
### Install Dependencies
 
```bash
pip install -r requirements.txt
```
 
### Configure Environment Variables
 
Create `.env`
 
```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=db_admin_portal
DB_USER=root
DB_PASSWORD=your_password
 
OPENROUTER_API_KEY=your_api_key
```
 
### Run Application
 
```bash
streamlit run app.py
```
 
---
 
## ✅ Current Progress
 
| Module | Status |
|----------|---------|
| Authentication | ✅ Completed |
| Role Management | ✅ Completed |
| Database Reflection | ✅ Completed |
| Data Viewer | ✅ Completed |
| Insert Module | ✅ Completed |
| Update Module | ✅ Completed |
| Delete Module | ✅ Completed |
| User Management | ✅ Completed |
| Permission Management | ✅ Completed |
| Audit Logging | ✅ Completed |
| AI SQL Generation | ✅ Completed |
| SQL Validation | ✅ Completed |
| AI Result Explanation | 🚧 In Progress |
| Export Module | 🚧 In Progress |
| Bulk Operations | 🚧 In Progress |
 
---
 
## 🎯 Future Enhancements
 
- Excel Export
- CSV Export
- Bulk Insert
- Bulk Update
- Bulk Delete
- Data Visualization Dashboard
- Query History
- Saved Reports
- Backup & Restore
- AI Insights Dashboard
 
---
 
## 👨‍💻 Team
 
**Project:** DB Admin Portal  
**Technology:** Python + Streamlit + SQLAlchemy + MySQL  
**Team Size:** 8 Members  
**Team Lead:** Mohammad Kashif Siddiqui
 
---
⭐ If you found this project useful, don't forget to star the repository.
 
