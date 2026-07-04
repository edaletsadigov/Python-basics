# Password Validator

Checks a password against five basic security criteria and gives a strength verdict.

## How it works

The script checks for:

- Minimum 8 characters
- At least one digit
- At least one uppercase letter
- At least one lowercase letter
- At least one special character (`!@#$%` etc.)

If the first four criteria are met, the password is considered **strong**.

## Run

```bash
python password_validator.py
```

## Example

```
Enter a password: Hello@99
Password length is sufficient.
Password contains at least one digit.
Password contains at least one uppercase letter.
Password contains at least one lowercase letter.
Password contains at least one special character.
Strong password!
```

## Requirements

Python 3.x — no external libraries needed.
