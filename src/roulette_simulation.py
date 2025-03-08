from oscars_grinding import simulate_oscars_grinding
from martingale import simulate_martingale
from romanovsky import simulate_romanovsky
import matplotlib.pyplot as plt

def main():
    # Oscar's Grinding Strategy Simulation
    print("Simulating Oscar's Grinding Strategy...")
    oscar_results = simulate_oscars_grinding(start_balance_range=range(5000, 15001, 1000), target_range=range(600, 3001, 100))
    
    # Martingale Strategy Simulation
    print("Simulating Martingale Strategy...")
    martingale_results = simulate_martingale(start_balance=10000, games=100, simulations=30)
    
    # Romanovsky Strategy Simulation
    print("Simulating Romanovsky Strategy...")
    romanovsky_results = simulate_romanovsky(start_balance=10000, games=100, simulations=30)

    # Visualization of results
    plt.figure(figsize=(12, 8))
    
    # Plotting Oscar's Grinding results
    plt.subplot(3, 1, 1)
    plt.title("Oscar's Grinding Strategy Results")
    plt.plot(oscar_results['balance_over_time'], label='Account Balance Over Time')
    plt.xlabel('Games Played')
    plt.ylabel('Account Balance')
    plt.legend()
    
    # Plotting Martingale results
    plt.subplot(3, 1, 2)
    plt.title("Martingale Strategy Results")
    plt.hist(martingale_results['amounts_won'], bins=10, alpha=0.7, label='Amounts Won')
    plt.xlabel('Amount Won')
    plt.ylabel('Frequency')
    plt.legend()
    
    # Plotting Romanovsky results
    plt.subplot(3, 1, 3)
    plt.title("Romanovsky Strategy Results")
    plt.hist(romanovsky_results['amounts_won'], bins=10, alpha=0.7, label='Amounts Won')
    plt.xlabel('Amount Won')
    plt.ylabel('Frequency')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()