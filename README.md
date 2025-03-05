```markdown
# CTFd Bulk User Importer

Welcome to the **CTFd Bulk User Importer**! This script allows you to bulk import players into your CTFd platform by uploading an Excel file. The file should contain the usernames and emails of all players. 

## Features

- Easily bulk import users into CTFd.
- Requires an admin account with an access token.
- Simple configuration for your CTFd domain and token.

## Prerequisites

Before running the script, make sure you have:

- A CTFd instance running.
- Admin access to your CTFd platform.
- A list of users in an Excel file containing **Username** and **Email** columns.

## Configuration

1. **Set Your CTFd Domain:**
   Replace `CTFd_DOMAIN` with the domain of your CTFd instance in the `base_url` variable. For example:

   ```python
   base_url = "https://your-ctfd-domain.com"
   ```

2. **Set Your Admin Access Token:**
   You’ll need an access token from an admin account in your CTFd instance. Add the token to the script as follows:

   ```python
   access_token = "your_admin_access_token"
   ```

3. **Prepare Your Excel File:**
   Your Excel file must contain at least two columns:

   - `Username`: The player's username.
   - `Email`: The player's email address.

   Make sure your file is formatted correctly before uploading it.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/ctfd-bulk-user-importer.git
   cd ctfd-bulk-user-importer
   ```

2. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script to import the users from your Excel file:

```bash
python import_users.py
```

The script will automatically read the user data from your Excel file and add them to your CTFd platform.

## Example Excel Format

| Username  | Email               |
|-----------|---------------------|
| player1   | player1@example.com |
| player2   | player2@example.com |

## Troubleshooting

- Ensure that the CTFd domain and admin access token are correct.
- Make sure your Excel file has the correct format (i.e., `Username` and `Email` columns).
- If you encounter any issues, feel free to open an issue in the GitHub repo!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
