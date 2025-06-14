# Expense Dashboard Backend

A RESTful API backend for the Expense Dashboard project, built using **Flask** and **Pandas**. This service delivers monthly expense data to a frontend application, with CORS enabled for seamless integration.

## Features

- **REST API**: Provides endpoints to fetch monthly expense data in JSON format.
- **Data Processing**: Leverages Pandas to efficiently read and process CSV-based expense data.
- **Cross-Origin Support**: Configured with Flask-CORS to support frontend applications hosted on different domains.

## Installation

Follow these steps to set up and run the backend locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/dilshod1405/expenses-b.git
   cd backend
   ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

The API will be accessible at: [http://localhost:5002/api/monthly-expenses](http://localhost:5002/api/monthly-expenses)

## Technologies

- **Flask**: A lightweight Python framework for building the API.
- **Flask-CORS**: Enables cross-origin resource sharing for frontend compatibility.
- **Pandas**: Processes and analyzes expense data from CSV files.

## Data Source

The backend uses a CSV file (`company_expenses.csv`) located in the `backend` directory. This file contains sample monthly expense data for testing and demonstration.

## API Endpoints

- **GET /api/monthly-expenses**  
  Retrieves monthly expense data in JSON format.

## Author

Developed by [Dilshod Normurodov](https://github.com/dilshod1405).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.