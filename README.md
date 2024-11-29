---

# Algorithmic Trading with Fyers API

This repository contains a collection of Python scripts for automating trading tasks using the Fyers API. It includes modules for user authentication, profile and fund information retrieval, and historical data analysis.

## Features

1. **Authentication**:
   - Implements OAuth-based authentication to securely obtain access tokens.
   - Automates the process of generating and saving the access token.

2. **Profile Management**:
   - Retrieves user profile details, including fund limits and positions.
   - Exports order and trade details to CSV for analysis.

3. **Historical Data**:
   - Fetches historical market data for specified symbols.
   - Supports conversion and formatting of timestamps for analysis in IST.

---

## Project Structure

- **`1_login.py`**:
   - Handles authentication with the Fyers API.
   - Generates and saves the access token.

- **`2_profile.py`**:
   - Retrieves user profile and fund information.
   - Exports order book and trade book data to CSV.

- **`3_histroy.py`**:
   - Fetches and processes historical market data.
   - Formats the data for use in further analysis.

---

## Prerequisites

- Python 3.8 or above.
- Fyers API package (`fyers-apiv3`).
- Other dependencies as listed in `requirements.txt`.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Sairaj2807/Algorithmic-Trading.git
   cd Algorithmic-Trading
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your credentials:
   - Replace placeholder values in `crediential.py` with your Fyers API credentials:
     ```python
     client_id = "your_client_id"
     secret_key = "your_secret_key"
     redirect_uri = "your_redirect_uri"
     ```

---

## Usage

1. **Authentication**:
   - Run `1_login.py` to generate and save the access token.
   ```bash
   python 1_login.py
   ```

2. **Retrieve Profile Information**:
   - Run `2_profile.py` to fetch profile and fund details.
   ```bash
   python 2_profile.py
   ```

3. **Fetch Historical Data**:
   - Run `3_histroy.py` to download historical market data for a specific symbol.
   ```bash
   python 3_histroy.py
   ```

---

## Notes

- Ensure the `access.txt` file contains a valid token before running the profile or history scripts.
- Modify `3_histroy.py` to specify different symbols or date ranges as needed.

---

## Future Enhancements

- Integration of trading strategies using the retrieved data.
- Enhanced error handling and logging mechanisms.
- Real-time data streaming and trading.

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## Contributions

Contributions are welcome! Please create an issue or submit a pull request with your enhancements.

---


