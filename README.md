# RoboCup visualization dashboard

## Overview
This repository contains the source code for the dashboard, built using Dash - a Python framework for building analytical web applications.

## Project Structure
The project is organized as follows:

- **/components**: This directory contains reusable components used in the dashboard. Components are modular pieces of the user interface, such as custom charts, filters, or other UI elements.

- **/pages**: The pages directory houses the different sections or views of your dashboard. Each page may consist of a layout, callback functions, and associated assets.

- **/parsers**: Parsers are located in this directory. Parsers handle data processing tasks, transforming raw data into a format suitable for visualization or analysis in the dashboard.

## Getting Started
Follow these steps to get the dashboard up and running:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/xl3ehindTim/RoboCup-dashboard.git
    cd RoboCup-dashboard
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Dashboard:**
    ```bash
    python app.py
    ```
   Visit `http://127.0.0.1:8050/` in your web browser to view the dashboard.

## Customization
Feel free to customize and extend the dashboard based on your specific requirements. Here are a few tips:

- Add new pages in the `/pages` directory to introduce new sections to your dashboard.
- Create additional components in the `/components` directory to enhance the user interface.
- Extend or modify the parsers in the `/parsers` directory to handle new data sources or update existing ones.