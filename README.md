<h1>Django Data Analysis Project</h1>
<p>This project allows users to upload a CSV file, perform basic data analysis on the file, and display the results in a web application built with Django.</p>

<h2>Features</h2>
<ol>
    <li>Upload CSV files</li>
    <li>Display the first few rows of the data</li>
    <li>Show summary statistics of the data</li>
    <li>Identify and handle missing values</li>
    <li>Generate and display a histogram for numerical data</li>
</ol>

<h2>Setup Instructions</h2>
<h3>Prerequisites</h3>
<ol>
    <li><a href="https://www.python.org/downloads/">Python 3.12.4</a></li>
    <li>Django~=5.0.7</li>
    <li>Pandas</li>
    <li>Matplotlib</li>
    <li>Seaborn</li>
</ol>

<h3>Installation</h3>
<ol>
    <li>Clone the Repository:
    <ul>git clone https://github.com/your-username/data_analysis_project.git</ul>
    <ul>cd data_analysis_project</ul></li>
    <br>
    <li>Create a Virtual Environment:
    <ul>python -m venv venv</ul>
    <ul>source venv/bin/activate   # On Windows use `venv\Scripts\activate`</ul></li>
    <br>
    <li>Install Dependencies:
    <ul>pip install -r requirements.txt
    </ul></li>
    <br>
    <li>Apply Migrations:
    <ul>python manage.py migrate</ul></li>
    <br>
    <li>Run the Development Server:
    <ul>python manage.py runserver</ul></li>
    <br>
    <li>Access the Application:
    <ul>Open your web browser and go to 'http://127.0.0.1:8000/'.
    </ul></li>
</ol>

<h2>Project Structure</h2>
<ul>
    <li><h4>data_analysis_project/urls.py:</h4>Defines the URL patterns for the project.</li>
    <li><h4>analysis/urls.py:</h4>Defines the URL patterns for the 'analysis' app.</li>
    <li><h4>analysis/forms.py:</h4>Contains the form class for file upload.</li>
    <li><h4>analysis/views.py:</h4>Contains the view logic for file upload and data analysis.</li>
    <li><h4>templates/upload.html:</h4>Template for file upload form.</li>
    <li><h4>templates/results.html:</h4>Template to display the analysis results.</li>
    <li><h4>static/css/styles.css:</h4>CSS styles for the application.</li>
    <li><h4>static/js/scripts.js:</h4>JavaScript for the application.</li>
</ul>

<h2>Usage</h2>
<ol>
    <li>Upload a CSV File:
        <ul>
        <li>Navigate to the home page.</li>
        <li>Upload a CSV file using the provided form.</li>
        </ul>
    </li>
    <br>
    <li>View Analysis Results:
        <p>After uploading, you will be redirected to a results page showing:</p>
        <ul>
        <li>The first few rows of the data.</li>
        <li>Summary statistics.</li>
        <li>Missing values.</li>
        <li>A histogram of the first numerical column.</li>
        </ul>
    </li>
</ol>

<h2>Handling Missing Values</h2>
<ul>
    <li>The current implementation fills missing values with '0'.</li>
    <li>Alternatively, you can drop rows with missing values by using 'df.dropna()' in the 'views.py' file.</li>
</ul>

<h2>Customization</h2>
<ul>
    <li>To change how missing values are handled, modify the corresponding section in 'analysis/views.py'.</li>
    <li>Additional analysis or visualizations can be added by updating the 'upload_file' function in 'views.py'.</li>
</ul>

<h2>Contributing</h2>
<p>Contributions are welcome! Please fork the repository and create a pull request with your changes.</p>
<br><hr>
<span>For any questions or issues, please contact <a href="https://mail.google.com/mail/u/0/#starred?compose=new">[kothimeravinod@gmail.com]</a> or connect with me on <a href="www.linkedin.com/in/vinodkothimera">LinkedIn</a>.</span>
