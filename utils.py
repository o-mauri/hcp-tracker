import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime
matplotlib.use('Qt5Agg')

def scores_to_use(differential_count):
    adjustment = 0
    scoresToUse = 0
    
    match differential_count:
        case 3:
            scoresToUse = 1
            adjustment = -2.0
        case 4:
            scoresToUse = 1
            adjustment = -1.0
        case 5:
            scoresToUse = 1
            adjustment = 0
        case 6:
            scoresToUse = 2
            adjustment = -1.0
        case 7 | 8:
            scoresToUse = 2
            adjustment = 0
        case 9 | 10 | 11:
            scoresToUse = 3
            adjustment = 0
        case 12 | 13 | 14:
            scoresToUse = 4
            adjustment = 0
        case 15 | 16:
            scoresToUse = 5
            adjustment = 0
        case 17 | 18:
            scoresToUse = 6
            adjustment = 0
        case 19:
            scoresToUse = 7
            adjustment = 0
        case 20:
            scoresToUse = 8
            adjustment = 0

    return scoresToUse, adjustment

def plotHcp(data):
    # Sort data by date in descending order (newest first)
    sorted_data = sorted(data, key=lambda x: x['date'], reverse=True)
    
    # Convert dates to datetime objects and prepare data for plotting
    dates = [datetime.strptime(score['date'], '%Y-%m-%d') for score in sorted_data]
    hcp_values = [score['HCPafter'] for score in sorted_data]

    # Create the line plot
    plt.figure(figsize=(10, 6))
    plt.plot(dates, hcp_values, marker='o', color='darkgreen', label='Handicap History')

    # Add horizontal dashed line for current handicap
    current_hcp = hcp_values[0]  # Most recent handicap value
    plt.axhline(y=current_hcp, color='blue', linestyle='--', alpha=0.7, 
                label=f'Current HCP: {current_hcp:.1f}')

    # Customize the plot
    plt.title('Handicap Progress Over Time')
    plt.xlabel('Date')
    plt.ylabel('Handicap')
    plt.grid(True)

    # Add legend
    plt.legend()

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Adjust layout to prevent label cutoff
    plt.tight_layout()

    # Show the plot
    plt.show()


def calculate_handicap(data):
    if len(data) < 3:
        print("Not enough scores to calculate HCP")
        return 54.0

    print(f"Calculating HCP based on {len(data)} rounds")
    print()
    # Sort data by date in descending order (newest first)
    sorted_data = sorted(data, key=lambda x: x['date'], reverse=True)
    
    # Limit to most recent 20 scores if more than 20 exist
    limited_data = sorted_data[:20]
    
    scoresToUse, adjustment = scores_to_use(len(limited_data))

    print(f"Using lowest {scoresToUse} rounds from most recent {len(sorted_data)} rounds.")
    if adjustment != 0:
        print(f"Adjusting by {adjustment} due to insufficient round scores.")
    print()

    sorted_diffs = sorted(limited_data, key=lambda x: x['differential'])

    used_diffs = sorted_diffs[:scoresToUse]

    hcp = (sum(d["differential"] for d in used_diffs) / len(used_diffs)) + adjustment

    return hcp