# hcp-tracker
A simple python project for tracking my golf handicap, with entry and graphing capabilities

## Features

- Calculate current handicap index based on most recent scores
- Add new rounds with detailed scoring information
- Automatic handicap differential calculations
- Support for course rating and slope rating
- Score adjustment based on maximum hole scores
- Visual handicap trend plotting
- Maintains a history of all rounds and handicap changes

## Files

- `currentHCP.py`: Calculates and displays the current handicap index based on stored rounds
- `addRound.py`: Interactive script to add new rounds and update handicap
- `utils.py`: Helper functions for handicap calculations and plotting
- `differentials.json`: JSON file storing all round data and handicap history

## Usage

### Adding a New Round

Run `addRound.py` to add a new round:
```bash
python addRound.py
```

The script will prompt you for:
- Date of the round (YYYY-MM-DD)
- Course par
- Course rating
- Slope rating
- Hole-by-hole scoring information including:
  - Par for each hole
  - Stroke index for each hole
  - Raw score for each hole

### Checking Current Handicap

Run `currentHCP.py` to view your current handicap:
```bash
python currentHCP.py
```

This will:
- Calculate your current handicap based on the most recent scores
- Display the number of scores used in the calculation
- Show any adjustments made due to insufficient rounds
- Display a plot of your handicap trend

## Handicap Calculation

The system follows the World Handicap System rules:
- Uses the best 8 scores from the most recent 20 rounds
- Applies adjustments for insufficient rounds
- Calculates differentials using the formula: (113/Slope Rating) × (Adjusted Gross Score - Course Rating)
- Applies maximum hole score limits based on handicap

## Requirements

- Python 3.x
- Required Python packages (install via pip):
  - json
  - datetime
  - math
  - matplotlib (for plotting)

## Data Storage

All round data is stored in `differentials.json` with the following information for each round:
- Date
- Course rating
- Slope rating
- Raw score
- Adjusted score
- Differential
- Handicap before and after the round
