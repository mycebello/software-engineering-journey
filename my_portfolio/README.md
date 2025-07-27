Job Maisiba Portfolio

This is a personal portfolio website built using HTML and CSS to showcase Job Maisiba's background, skills, projects, and contact information.

Files Included

portfolio.html: Main structure and content of the website.

style.css: Styling and layout of the website.

 HTML Overview (portfolio.html)
Key Tags and Their Roles

<!DOCTYPE html>: Declares the document type and version (HTML5).

<html lang="en">: Root element; lang="en" helps with accessibility and SEO.

<head>: Metadata (charset, viewport, title, link to CSS).

<body>: Contains all visible content.

Major Sections

<header>: Introduces your name and profession.

<nav>: Navigation bar with anchor links to different sections using href="#section-id".

<section>: Divides content into logical blocks (about, education, skills, etc.).

<ul>, <li>: Used for listing skills and projects.

<a>: Anchor tags used for links (mailto:, tel:, or to the CV).

<form>: Collects contact messages with <input>, <textarea>, and <button>.

Special Attributes
id: Used to target sections from the navbar.

href: Specifies the link target (file, email, tel).

download: Instructs browser to download the file.

action, method: Used in form submission (placeholder only here).

 CSS Overview (style.css)
General Styling
*: Universal selector to reset margin/padding and apply box-sizing.

body: Sets font, background color, and base layout style.

Layout Components
.card: Styled section blocks with padding, box-shadow, and hover lift effect.

nav: Flexbox for horizontal layout with link spacing and hover styles.

.skills: Flex container for tech stack badges.

Interactive Elements
.btn: Reusable button style with hover transition.

form input, textarea: Styled inputs with focus states.

a[href^="mailto"], a[href^="tel"]: Clickable email and phone links.


