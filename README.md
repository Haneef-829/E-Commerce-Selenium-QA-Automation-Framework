# E-Commerce Selenium QA Automation

End-to-end UI automation framework built with Python,
Selenium WebDriver and pytest.

## Application

SauceDemo

https://www.saucedemo.com/

## Tech Stack

- Python
- Selenium WebDriver
- pytest
- pytest-html
- GitHub Actions
- Page Object Model

## Automated Test Coverage

### Authentication

- Valid login
- Invalid login
- Login error validation

### Product

- Product page validation
- Product listing validation
- Add product to cart

### Cart

- Cart navigation
- Cart item validation

### Checkout

- Customer information
- Checkout navigation
- Order completion
- Confirmation validation

## Architecture

```text
tests/
    |
    v
page objects/
    |
    v
BasePage
    |
    v
Selenium WebDriver
    |
    v
SauceDemo
