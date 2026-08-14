# Sports Club Management System

## Project Description

The Sports Club Management System is a web-based application developed using Python Flask and MongoDB. It helps manage sports club members by providing features to add, view, search, edit, update, and delete member information.

The project also includes a dashboard that displays statistics such as total members, available sports, and membership counts.

## Features

* Add new sports club members.
* View all members in a table.
* Search members by name, sport, or membership type.
* Edit member information.
* Update membership type.
* Delete members with a confirmation message.
* Dashboard showing:

  * Total Members
  * Sports Available
  * Gold Members
  * Silver Members
  * Bronze Members
* Membership types:

  * Gold
  * Silver
  * Bronze
* Displays a "No members found" message when a search returns no results.

## Technologies Used

* Python
* Flask
* MongoDB
* PyMongo
* HTML
* CSS

## Project Structure

```text
SportsClubManagement/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   └── edit.html
│
└── static/
    ├── style.css
    └── script.js
```

## Database

The project uses MongoDB.

* Database Name: `SportsClubManagement`
* Collection Name: `members`

Each member document contains:

* Name
* Age
* Sport
* Membership Type

## How to Run the Project

1. Install Python.
2. Install MongoDB and start the MongoDB server.
3. Open the project folder in VS Code.
4. Install the required packages:

```bash
pip install -r requirements.txt
```

5. Run the Flask application:

```bash
py app.py
```

6. Open the browser and visit:

```text
http://127.0.0.1:5000
```

## How to Use

1. Enter the member's name.
2. Enter the age.
3. Enter the sport.
4. Select Gold, Silver, or Bronze membership.
5. Click **Add Member**.
6. Use the search box to find members.
7. Click **Edit** to modify member details.
8. Click **Delete** to remove a member.

## Future Scope

* User login and authentication.
* Admin panel.
* Member profile photos.
* Membership fee management.
* Attendance tracking.
* Cloud database deployment.

## Conclusion

The Sports Club Management System demonstrates the implementation of CRUD operations using Flask and MongoDB along with a responsive HTML and CSS user interface. It provides a simple and effective way to manage sports club member information.
