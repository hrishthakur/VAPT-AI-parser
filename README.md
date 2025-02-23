# VAPT AI Parser

VAPT AI Parser is a web application designed to parse Vulnerability Assessment and Penetration Testing (VAPT) reports. It uses OpenAI's API to generate detailed vulnerability analyses, including CWE IDs, business impacts, and recommended fixes.

## Features

- Upload VAPT reports in various formats (CSV, JSON, XLSX, PDF).
- Parse and validate report data.
- Generate AI-based vulnerability details using OpenAI.
- Display results in a user-friendly dashboard.

## Prerequisites

- Python 3.8 or higher
- Node.js and npm
- OpenAI API Key

## Installation

### Backend Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/hrishthakur/VAPT-AI-parser.git
   cd VAPT-AI-parser/backend
   ```

2. **Create a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Python Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**

   Create a `.env` file in the `backend` directory with the following content:

   ```plaintext
   OPENAI_API_KEY=your_openai_api_key_here
   DATABASE_URL=sqlite:///vapt_ai_parser.db
   ```

6. **Run the Backend Server:**

   ```bash
   python app.py
   ```

### Frontend Setup

1. **Navigate to the Frontend Directory:**

   ```bash
   cd ../frontend
   ```

2. **Install Node.js Dependencies:**

   ```bash
   npm install
   ```

3. **Run the Frontend Development Server:**

   ```bash
   npm run serve
   ```

## Usage

1. **Access the Application:**

   Open your web browser and go to `http://localhost:5173` to access the VAPT AI Parser application.

2. **Upload a VAPT Report:**

   - Use the upload form to select and upload your VAPT report file.
   - Supported formats: CSV, JSON, XLSX, PDF.

3. **View AI-Generated Results:**

   - Navigate to the dashboard to view detailed vulnerability analyses.
   - The dashboard displays CWE IDs, business impacts, and recommended fixes.