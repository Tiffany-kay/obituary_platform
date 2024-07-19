# Obituary Management Platform

## Project Overview

This project is a web application for submitting, managing, and displaying obituaries. The platform includes features for SEO and Social Media Optimization to enhance visibility and engagement.

## Features

- Submit obituaries through a user-friendly form.
- View a list of submitted obituaries.
- SEO and Social Media Optimization for each obituary.
- Dynamic meta tags and Open Graph tags for better social media sharing previews.
- Social media sharing buttons.
- Canonical tags to avoid duplicate content issues.
- XML sitemap for search engine indexing.

## Technologies Used

- Flask (Python Web Framework)
- SQLite (Database)
- HTML/CSS (Frontend)
- JavaScript (Frontend Validation)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/obituary_platform.git
   cd obituary_platform
   
Create a virtual environment:
bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install dependencies:
bash
pip install Flask

Run the application:
bash
python app.py
Access the application:

Open your web browser and go to http://127.0.0.1:5000/submit to submit an obituary.
Go to http://127.0.0.1:5000/view_obituaries to view the list of obituaries.
Go to http://127.0.0.1:5000/sitemap.xml to view the XML sitemap.

Project Structure
obituary-platform/
│
├── app.py
├── obituary_platform.db
├── templates/
│   ├── obituary_form.html
│   ├── view_obituaries.html
│   └── sitemap_template.xml
└── README.md

SEO and Social Media Optimization
Meta tags (title, description, keywords) are dynamically added based on the obituary content.
Semantic HTML tags and structured data (schema.org) are used to improve search engine visibility.
Open Graph tags are implemented for better social media sharing previews.
Social media sharing buttons are integrated on obituary pages.
Canonical tags are implemented to avoid duplicate content issues.
An XML sitemap is created and can be submitted to search engines.

Contribution
Contributions are welcome! Please fork the repository and create a pull request with your changes.

License
This project is licensed under the MIT License.
