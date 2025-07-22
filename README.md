# FavQs API Automation Tests

This project contains automated tests for the FavQs API (https://favqs.com/api/) written in Python using the `requests` library and `pytest` framework.

---

## Project Description

The goal of this project is to automate testing of user creation and update functionalities using the FavQs free API. All operations are performed via HTTP API calls.

---

## Technologies Used

- Python 3.12  
- requests  
- pytest

---

## Setup and Installation

1. Clone this repository:

```bash
git clone https://github.com/YuliaShap/favqs-api-tests.git
cd favqs-api-tests
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Setup configuration:

Copy the provided template:
```bash
cp config_template.py config.py
```
Open config.py and fill in your actual API Key like this:
```python
API_KEY = "your_api_key_here"
```

4. Run the tests:

```bash
pytest tests/
```


### Author
Yuliia Shaposhnikova — domik339@gmail.com