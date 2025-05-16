# Inventory Location Web App

A Flask-based internal web application designed to help Pro Moto Billet’s packaging and shipping departments quickly locate parts by part number, improving order fulfillment speed and accuracy. Built with Python, Flask, SQLite, HTML, CSS, and JavaScript, the app is now in production use.

---

## What It Is

This is a web application that allows warehouse and shipping personnel to:

- Search for part numbers and instantly retrieve their storage location(s)
- View location data including aisle, section, and shelf
- See multiple storage locations for a single item, if applicable
- Update, move, or remove part location information as needed
- Maintain an up-to-date product location database using a clean and minimal interface

This tool was specifically developed to solve a growing problem within the company—difficulty finding parts due to limited knowledge among staff and scattered storage patterns. The result: lost time, delayed orders, and reduced efficiency.

---

## Why I Built It

I created this web app to:

- Solve a major bottleneck in our packaging and shipping workflow
- Make it easier and faster for staff to locate products without relying on tribal knowledge
- Improve overall inventory accuracy and shipping efficiency
- Learn how to build a full-stack solution using Python, Flask, SQL, and modern frontend technologies
- Deliver a production-ready solution that integrates smoothly into our company’s day-to-day operations

Before this app, locating parts could halt order fulfillment for extended periods. Now, the process is streamlined, and even new employees can find products with ease.

---

## How I Built It

Technologies and frameworks used:

- Python + Flask for the backend web server and routing
- SQLite for a lightweight, file-based relational database
- HTML, CSS, JavaScript for the frontend user interface

### Workflow Overview:

1. Packaging staff visits the web app via browser
2. User enters a part number in the search bar
3. App queries the SQLite database
4. App returns location(s): aisle, section, and shelf
5. If updates are needed, users can add, remove, or edit part entries via a simple form
6. Database is updated in real time

The app is optimized for speed, simplicity, and ease of use.
---

## Challenges I Faced

- Database integration: Learning how to use SQLite with Flask, set up models, and safely perform CRUD operations
- Frontend/backend connection: Making Python, HTML/CSS, and JavaScript work together smoothly with Flask
- User-friendliness: Designing an interface that’s easy for warehouse staff to use without training
- Data accuracy: Ensuring that location data is consistent and updatable without creating confusion
- Real-world testing: Validating that the app performs well in a busy production environment

Despite these challenges, this project gave me valuable full-stack development experience and solved a real problem.

---

## Tools & Tech Used

- Python
- Flask
- SQLite
- HTML, CSS, JavaScript

---

## What I'd Do Differently

If I expand this app in the future, I’d like to:
- Add support for product images to help identify parts visually
- Enable location tagging with notes for more context (e.g., "top shelf – behind skid plates")
- Improve search functionality with filters or fuzzy matching
- Add user authentication for update permissions
- Deploy the app via cloud services for broader access across departments

---