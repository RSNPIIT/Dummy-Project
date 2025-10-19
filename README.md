E-Book Management System UI

This repository contains the front-end components (HTML/CSS) for a simple, modern E-Book Management System, including user authentication forms and an administrative dashboard.

The entire UI is built as single HTML files for maximum simplicity and portability, leveraging the power of Tailwind CSS for all styling.

🚀 Key Technologies & Design Principles

Core Technology: HTML5 and JavaScript (No external frameworks like React or Angular).

Styling: Tailwind CSS (via CDN) for utility-first, fully responsive design.

Structure: Strict, neat XHTML-like syntax is used for all self-closing tags (e.g., <input />).

Aesthetics: A focus on modern trends, including Glassmorphism for authentication pages and a clean, blueish material theme for the dashboard.

✨ Component Breakdown

1. Admin Dashboard (index.html)

The dashboard is designed for administrative oversight of user requests and platform statistics.

Feature

Description

Theme

Light-bluish background (bg-blue-50) with a dark, contrasting navbar (bg-gray-800).

Requested E-Books Table

Clear table layout with blue headers (bg-blue-200) and hover states.

Action Button

Distinct, rounded Green "Grant" buttons for clear administrative actions.

Summary Cards

Four key metrics (Users, Requested, Granted, Available) displayed in a responsive 4-column grid on large screens. Each card uses a unique, vibrant color theme for easy recognition (Indigo, Cyan, Green, Yellow).

Navigation

The "Summary" link in the navbar uses a smooth scroll to navigate to the summary card section (#summary-section) on the same page.

2. Authentication Forms (login.html & register.html)

The authentication pages implement a modern "Liquid Glass" aesthetic for visual flair.

Design Style: Glassmorphism (semi-transparent, blurred backdrop-filter) is used on the form card, set against a deep blue/purple gradient background.

Readability: High contrast is maintained by using light text and vibrant action buttons (Cyan for Register, Indigo/Cyan for Login) against the blurred glass element.

🛠 Setup & Usage

Since this project uses a standard HTML structure with the Tailwind CDN, no build steps are required.

Clone this repository.

Open any of the HTML files (e.g., index.html, login.html) directly in your web browser.
