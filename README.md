# 第一小组2021年大作业

## 中文(Chinese)
## 功能：
- [x] 增加用户
- [x] 更新用户
- [x] 删除用户
- [x] 注册用户
- [x] 登录用户
- [ ] 列表分页

## 运行步骤
通过gitpod打开之后，在根目录运行 `bash run.bash`即可，此后您可以通过gitpod的远程浏览器之间访问应用，默认管理员用户名及密码均为`admin`


如果提示数据库未连接，可能是sleep时长过短，可能需要您手动运行如下命令以初始化数据库：
```bash 
docker exec -i mysqldb sh -c 'exec mysql -uroot -p"test"' < ./accounts.sql
```
当然，本项目也提供了非docker环境下的部署教程，参见后文。
## 功能截图

![Admin add](dash_board_app/static/admin_add.png)
![Admin delete](dash_board_app/static/admin_del.png)
![Admin edit](dash_board_app/static/admin_edit.png)

## English
This repo was updated based on previous open source project and add some new features as below：
- [x] Add new users
- [x] Update user record
- [x] Delete user record
- [ ] Pagination

*Manual for those who want to run local without docker*

### Requirements(Minimum)

Download and install Python, I am using Python 3.7.2, make sure to check the box Add Python to PATH on the installation setup screen. </p>
Download and install MySQL Community Server and MySQL Workbench, you can skip this step if you already have a MySQL server set up. </p>


**Mojor operations handled**

1). Form Design — Design a login and registration form with HTML5 and CSS3.<br>
2). Templates — Create Flask templates with HTML and Python.<br>
3). Basic Validation — Validating form data that is sent to the server (username, password, and email).<br>
4). Session Management — Initialize sessions and store retrieved database results.<br>
5). MySQL Queries — Select and insert records from/in our database table.<br>
6). Routes — Routing will allow us to point our URL's to our functions.<br>

### Requirements ,Packages used and Installation
Download and install Python, for this tutorial I'll be using Python 3.7.2, make sure to check the box Add Python to PATH on the installation setup screen
 
### Installation
          
Navigate to your current project directory for this case it will be **Login-System-with-Python-Flask-and-MySQL**. <br>
          
### 1 .Create an environment
          
Depending on your operating system,make a virtual environment to avoid messing with your machine's primary dependencies
          
**Windows**
          
```

cd Login-System-with-Python-Flask-and-MySQL
py -3 -m venv venv

```
          
**macOS/Linux**
          
```
cd Login-System-with-Python-Flask-and-MySQL
python3 -m venv venv

```

### 2 .Activate the environment
          
**Windows** 

```venv\Scripts\activate```
          
**macOS/Linux**

```. venv/bin/activate```
or
```source venv/bin/activate```

### 3 .Install the requirements

Applies for windows/macOS/Linux

```pip install -r requirements.txt```
  
### 4. Run the application 

**For linux and macOS**
Make the run file executable by running the code

```chmod 777 run```

Then start the application by executing the run file

```./run```

**On windows**
```
set FLASK_APP=main
flask run

```
          

