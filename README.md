## Binance Data Collection and Visualization

This project involves collecting candlestick data and pie chart data from the Binance API and visualizing it using a Flask-based web application.

### Installation and Usage

1. Clone the repository:

```shell
git clone https://github.com/alisea-natan/binance-data-collection.git
```

2. Change to the project directory:

```shell
cd binance-data-collection
```

3. Create a new virtual environment:

```shell
python -m venv venv
```

4. Activate the virtual environment:

    On Windows:

    ```shell
    venv\Scripts\activate
    ```
    
    On macOS and Linux:
    
    ```shell
    source venv/bin/activate
    ```

5. Install the required dependencies:

```shell
pip install -r requirements.txt
```

6. Run the data collection script:

```shell
python data_collecting.py
```

This will collect the candlestick data from the Binance API and save it to a CSV file.

7. Run the Flask web application:

```shell
python diagrams.py
```

The Flask application will start running locally. Access the web page by opening your web browser and navigating to `http://localhost:5000/`.

The candlestick chart will display the collected data, and the pie chart will show the market capitalizations for the top 10 symbols.

Remember to deactivate the virtual environment once you're done:

```shell
deactivate
```

Using a virtual environment helps isolate the project's dependencies and prevents conflicts with other Python projects on your system.

### Notes
To improve the current state of the project and make it more professional, here are some suggested changes:

1. Add command-line arguments for interval and symbols: Instead of hardcoding the interval and symbols in the code, it could be configurable by accepting command-line arguments. This allows users to specify the interval and symbols when running the script. Preferred library for that is click, but also argparse could be used. 

2. Implement API endpoints in the Flask app: Instead of relying on the default route ("/") for retrieving data, dedicated API endpoints could be created to receive the interval and symbols as parameters. This way, the Flask app can receive the data from the user through API calls.

3. Implement input prompts for interval and symbols: If running the script directly without using APIs, user could be prompted to enter the desired interval and symbols using the input() function. This allows users to provide the input interactively in the console.

4. Add unit tests: To cover code with tests usually recommended. It could help to verify the functionality of data collection, data processing, and any other critical parts of project. Libraries like pytest can be used for writing and running tests.