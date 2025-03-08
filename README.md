# Roulette Strategies Simulation

This project simulates various strategies for playing Roulette, specifically focusing on Oscar's Grinding, Martingale, and Romanovsky strategies. The aim is to analyze the effectiveness of these strategies through simulations and visualizations.

## Project Structure

```
roulette-strategies
├── src
│   ├── oscars_grinding.py
│   ├── martingale.py
│   ├── romanovsky.py
│   └── roulette_simulation.py
├── requirements.txt
└── README.md
```

## Strategy Descriptions

### Oscar's Grinding
This strategy involves gradually increasing bets after wins and minimizing losses. The simulation includes:
- Visualization of failure probabilities based on varying starting balances and target amounts.
- A line graph showing the account balance over 50 games.

### Martingale
The Martingale strategy involves doubling the bet after each loss, aiming to recover previous losses with a single win. The simulation includes:
- Histograms of amounts won after playing 10, 20, 30, 40, and 50 games.
- A plot of the account balance over 100 games, simulated 30 times.

### Romanovsky
Similar to Martingale but with a more structured approach to betting. The simulation includes:
- Histograms of amounts won after playing 10, 20, 30, 40, and 50 games.
- A plot of the account balance over 100 games, simulated 30 times.

## Requirements

To run this project, you will need the following Python libraries:
- numpy
- pandas
- matplotlib
- seaborn

You can install the required libraries using the following command:

```
pip install -r requirements.txt
```

## Running the Simulation

To execute the simulations for each strategy, run the `roulette_simulation.py` file located in the `src` directory. This file orchestrates the execution of the different strategies and generates the necessary visualizations.

```bash
python src/roulette_simulation.py
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.