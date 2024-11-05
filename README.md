<h1>YouTube Transcript to Detailed Notes Converter</h1>

<p>This project is a web application that extracts the transcript from a YouTube video and provides a detailed, structured summary based on a pre-defined prompt. It uses <code>Streamlit</code> for the user interface, the <code>youtube-transcript-api</code> to fetch video transcripts, and <code>Google Gemini</code> for generating summaries.</p>

<h2>Features</h2>
<ul>
    <li>Fetches transcript data from YouTube videos using their URL.</li>
    <li>Generates a detailed summary based on a structured prompt.</li>
    <li>Displays the video thumbnail and summarized notes on the app interface.</li>
</ul>

<h2>Technologies Used</h2>
<ul>
    <li><strong>Python</strong> - The primary programming language for backend logic.</li>
    <li><strong>Streamlit</strong> - For building the web-based user interface.</li>
    <li><strong>dotenv</strong> - For securely loading environment variables.</li>
    <li><strong>Google Gemini API</strong> - To generate content summaries using AI.</li>
    <li><strong>YouTube Transcript API</strong> - To retrieve transcripts from YouTube videos.</li>
</ul>

<h2>Setup and Installation</h2>
<ol>
    <li>Clone the repository:
        <pre><code>git clone https://github.com/yourusername/YouTube-Transcript-Summarizer.git</code></pre>
    </li>
    <li>Navigate to the project directory:
        <pre><code>cd YouTube-Transcript-Summarizer</code></pre>
    </li>
    <li>Create a virtual environment:
        <pre><code>python -m venv env</code></pre>
    </li>
    <li>Activate the virtual environment:
        <ul>
            <li>For Windows: <code>env\Scripts\activate</code></li>
            <li>For macOS/Linux: <code>source env/bin/activate</code></li>
        </ul>
    </li>
    <li>Install the dependencies:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>Create a <code>.env</code> file in the project root directory with your Google API key:
        <pre><code>GOOGLE_API_KEY=your_api_key_here</code></pre>
    </li>
</ol>

<h2>Running the Application</h2>
<ol>
    <li>Make sure your virtual environment is activated.</li>
    <li>Run the Streamlit application:
        <pre><code>streamlit run app.py</code></pre>
    </li>
    <li>Open the provided local URL in your web browser to access the app.</li>
</ol>

<h2>Usage</h2>
<ol>
    <li>Enter the YouTube video link in the input box.</li>
    <li>Click <strong>Get Detailed Notes</strong> to extract and summarize the transcript.</li>
    <li>The app will display the video thumbnail and a detailed summary of the video content.</li>
</ol>

