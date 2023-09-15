# Flask Persons API

This is a simple API for managing persons' data.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the API](#running-the-api)
  - [Endpoints](#endpoints)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

To get started with this API, follow the instructions below.

### Prerequisites

- Python 3.x
- SQLite

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Fidelis-7/HNG_stage2.git
```

2. Install the required dependencies:

```bash
pip install Flask
```

3. Create a virtual environment (optional but recommended):

```bash
python3 -m venv venv
```

4. Activate the virtual environment (if created):

   - On Windows:

   ```bash
   venv\Scripts\activate
   ```

   - On MacOS and Linux:

   ```bash
   source venv/bin/activate
   ```

5. Run the API:

```bash
python app.py
```

## Usage

### Running the API

```bash
python app.py
```

### Endpoints

- `GET /api`: Retrieves a list of persons.

- `POST /api`: Creates a new person.

- `GET /api/<int:user_id>`: Retrieves information about a specific person.

- `PUT /api/<int:user_id>`: Updates information about a specific person.

- `DELETE /api/<int:user_id>`: Deletes a specific person.

## Examples

### Example 1: Getting all persons

Request:

```bash
curl -X GET http://localhost:5000/api
```

Response:

```json
[
  {
    "user_id": 1,
    "name": "John Doe",
    "gender": "Male"
  },
  {
    "user_id": 2,
    "name": "Jane Doe",
    "gender": "Female"
  }
]
```

### Example 2: Creating a new person

Request:

```bash
curl -X POST http://localhost:5000/api -d "name=Bob&gender=Male"
```

Response:

```json
"user with the id: 3 created successfully"
```

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Make your changes and commit them.
4. Push to your fork and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---
