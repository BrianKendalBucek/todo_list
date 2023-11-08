# Walmart Costa Rica Scraper

This Scrapy project is designed to scrape the names and prices of specific items from the [Walmart Costa Rica](https://www.walmart.co.cr/) website. The scraper will output the data in a JSON file.

## Prerequisites

Before you can run this project, you'll need to install Python 3 and set up a virtual environment.

### Installing Python 3

- **Windows**: Download the latest version of Python 3 from the [Python.org](https://www.python.org/downloads/windows/) downloads page and run the installer. Make sure to check the option that says "Add Python 3.x to PATH" during installation.
  
- **macOS/Linux**: Python 3 is usually pre-installed on macOS and most Linux distributions. If it's not, you can install it using Homebrew on macOS (`brew install python3`) or your distribution's package manager on Linux.

## Setting Up a Virtual Environment

### Creating a Virtual Environment

- **Windows**:
  ```
  python -m venv venv
  ```

- **macOS/Linux**:
  ```
  python3 -m venv venv
  ```

### Activating the Virtual Environment

- **Windows**:
  ```
  .\venv\Scripts\activate
  ```

- **macOS/Linux**:
  ```
  source venv/bin/activate
  ```

### Deactivating the Virtual Environment

When you're done working on the project, you can deactivate the virtual environment by running:

```
deactivate
```

## Installation

With your virtual environment activated, install Scrapy:

```
pip install scrapy
```

## Running the Scraper

To run the scraper, from within the directory outside of the walmart_scraper directory, use the following command:

```
scrapy crawl walmart_costa_rica
```

This will execute the `walmart_costa_rica` spider and save the scraped data into a JSON file located in the `data/` directory.

## Output

The output will be stored in the `data/` directory with the filename format `walmart_costa_rica_<timestamp>.json`.