# Valuation Multiple App

## Work In Progress

The Valuation Multiple Web App allows users to calculate multiples of stocks for valuation purposes. 
## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Examples](#examples)
- [License](#license)

## Features

- Calculate valuation multiples for stocks using various metrics.
- Customizable inputs for key valuation parameters.
- Interactive and user-friendly interface.
- Comprehensive error handling and validation.

## Getting Started

### Installation

1. Clone the repository from GitHub:

`git clone git@github.com:mxstrv/valuation-multiple-django.git`

2. Install the necessary dependencies:

`pip install -r requirements.txt`

3. Get API key from [financialmodelingprep.com](https://financialmodelingprep.com)
### Usage

1. Start the web app server:

2. Open your web browser and navigate to `http://localhost:8000` to access the web app.

## Inputs

The Valuation Multiple Web App requires the following inputs for calculating multiples:

1. **Stock Symbol**: Enter the stock symbol or ticker of the company you want to value.

2. **Valuation Metric**: Select the desired valuation metric from a predefined list, such as Price/Earnings (P/E) ratio, Price/Sales (P/S) ratio, or Price/Book (P/B) ratio.

3. **Time Period**: Specify the time period for which you want to calculate the multiple (e.g., trailing twelve months or forward estimates).

4. **Market Data**: Choose the appropriate market data source (e.g., public exchange, Bloomberg, Yahoo Finance).

5. **Peer Group**: Optionally, you can select a peer group or industry to compare the valuation multiples against.

## Outputs

The Valuation Multiple Web App provides the following outputs:

- **Valuation Multiple**: The calculated valuation multiple based on the selected inputs.

## Examples

**Example 1: Calculate P/E Ratio for Apple Inc.**
- Stock Symbol: AAPL
- Valuation Metric: Price/Earnings (P/E) ratio


The app will display the P/E ratio for Apple Inc. based on the most recent financial data.

## License

The Valuation Multiple Web App is open source and released under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and distribute it according to your needs.

