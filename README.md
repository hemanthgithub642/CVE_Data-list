# CVE Data Web Application

This project is a web application that displays CVE (Common Vulnerabilities and Exposures) data fetched from a backend API. The application features dynamic data fetching, pagination, and an interactive user interface.

## Key Features

- **Fetch CVE Data**: Fetches and displays CVE data from the server.
- **Top Results Dropdown**: Allows users to select and display top N CVE records.
- **Interactive CVE IDs**: Clickable CVE IDs that fetch detailed CVE information.
- **Pagination**: Simple pagination for navigating through records.
- **Responsive Design**: Uses CSS for responsive and interactive design elements.

## Skills Utilized

### Frontend Skills

- **HTML**: Structured the web page with semantic elements and interactive components.
- **CSS**: Styled the application with custom styles for tables, buttons, dropdowns, and pagination.
- **JavaScript**: Implemented dynamic data fetching, event handling, and DOM manipulation.

### JavaScript Skills

- **Fetch API**: Used to fetch data from the server and handle HTTP responses.
- **DOM Manipulation**: Dynamically updated the DOM with fetched data.
- **Event Handling**: Managed user interactions with buttons and clickable elements.
- **JSON Handling**: Parsed and utilized JSON data fetched from the API.

## Application Structure

### HTML Structure

- **Header**: Displays the title and total records.
- **Button**: Fetches CVE data when clicked.
- **Table**: Displays the CVE data with columns for CVE ID, description, published date, last modified date, and CVSS score.
- **Dropdown**: Allows selection of the top N results to display.
- **Pagination**: Simple pagination controls for navigating through records.

### CSS Styles

- **Table Styling**: Styled the table for better readability.
- **Button Styling**: Custom styles for buttons to make them visually appealing.
- **Dropdown Styling**: Styled dropdown menu for selecting top results.
- **Pagination Styling**: Styled pagination controls for navigation.

### JavaScript Functions

- **showTopX(x)**: Fetches and displays the top X CVE records from the server.
- **fetchCVEData()**: Fetches and displays all CVE records from the server.
- **addClickEventToCVEIds(cveIds)**: Handles click events on CVE IDs and fetches detailed information.

## Usage

1. **Fetch All CVE Data**:
    - Click the "Fetch CVE Data" button to load all CVE records.

2. **Show Top Results**:
    - Use the dropdown menu to select and display the top N results.

3. **View CVE Details**:
    - Click on any CVE ID in the table to fetch and view detailed CVE information.

## Project Setup and Execution

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/hemanthgithub642/CVE_Data-list
    cd your-repo
    ```

2. **Run the Server**:
    - Ensure your backend server is set up to serve the necessary endpoints (`/fetch_n_records`, `/fetch_cve_data`, `/fetch_cve_record`).

3. **Open the HTML File**:
    - Open `index.html` in your web browser to view the application.

## Conclusion
  This CVE Data Web Application demonstrates a comprehensive approach to building a dynamic and interactive web interface for displaying CVE data. By leveraging modern frontend technologies, it effectively handles data fetching, user interactions, and responsive design. This project showcases key skills in HTML, CSS, and JavaScript, providing a practical example of how to integrate these technologies to create a functional and user-friendly application. The outcome is a robust tool for viewing and managing CVE records, illustrating the potential of web development in handling and presenting complex data sets.
