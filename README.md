# RoboCup visualization dashboard

## Overview
This repository contains the source code for the dashboard, built using Dash - a Python framework for building analytical web applications.

## Project Structure
The project is organized as follows:

- **/components**: This directory contains reusable components used in the dashboard. Components are modular pieces of the user interface, such as custom charts, filters, or other UI elements.

- **/pages**: The pages directory houses the different sections or views of your dashboard. Each page may consist of a layout, callback functions, and associated assets.

- **/parsers**: Parsers are located in this directory. Parsers handle data processing tasks, transforming raw data into a format suitable for visualization or analysis in the dashboard.

- **/assets**: The assets directory stores images, CSS files, or other static files used in the dashboard.

- **Dockerfile**: This file specifies the Docker image configuration for running the dashboard in a containerized environment.

- **docker-compose.yml**: This file defines a <!-- multi- --> container environment using Docker Compose, simplifying the setup <!-- and deployment --> process.

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

## Running with Docker Compose
To run the dashboard using Docker Compose in a single step, follow these steps:

1. **Build and Start Containers:**
    ```bash
    docker-compose up -d
    ```
   This command builds the necessary Docker image and starts the containers in detached mode.

2. **Access the Dashboard:**
   Open your web browser and visit `http://127.0.0.1:8050/` to view the running dashboard.

3. **Stop Containers (Optional):**
   If you want to stop the containers, use the following command:
    ```bash
    docker-compose down
    ```

## Customization
Feel free to customize and extend the dashboard based on your specific requirements. Here are a few tips:

- Add new pages in the `/pages` directory to introduce new sections to your dashboard.
- Create additional components in the `/components` directory to enhance the user interface.
- Extend or modify the parsers in the `/parsers` directory to handle new data sources or update existing ones.