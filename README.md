# Hello, Yekaterinburg!

### Project for "Код города 300 | Хакатон Сбера x УрФУ"  
**Case #1: "Hello, Yekaterinburg!"**

This web service helps both visitors and residents of Yekaterinburg discover nearby events. The platform gathers and parses event information from selected VK communities, and content managers can conveniently view all upcoming events on a single dashboard.

![Demo GIF](demo.gif)

## Features:
- Displays the nearest events happening in Yekaterinburg.
- Event information is parsed automatically from VK communities.
- Content managers can access a dashboard to view and manage the event listings.

## Technology Stack:
- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite
- **Web Scraping**: Custom VK parser

## Setup Instructions

1. **Install Required Libraries**  
   Ensure you have Python installed on your system. Then, install the dependencies using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

2. **Navigate to the Project Directory**  
   Open a terminal and move into the main project folder:
   ```bash
   cd HelloEkaterinburg
   ```

3. **Run the Development Server**  
   Start the Django development server using the following command:
   ```bash
   python manage.py runserver
   ```

4. **Create a Superuser**  
   To add the first content manager (superuser), use the following command:
   ```bash
   python manage.py createsuperuser
   ```
   You will be prompted to enter a username, email, and password.

5. **Access the Web App**  
   Open your browser and go to `http://127.0.0.1:8000/` to start exploring events!
   
