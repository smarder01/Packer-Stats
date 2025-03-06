# Cheesehead Stats: Tackling the Packers’ Performance

## Project Overview  
This project analyzes the Green Bay Packers' performance over the past seven NFL seasons, examining season-by-season trends in offensive and defensive efficiency. Using game-level statistics, we investigate key performance metrics to identify patterns, strengths, and areas for improvement. The analysis aims to uncover trends in performance and assess the relationship between various factors such as possession time, offensive efficiency, and defensive consistency.

## Research Question  
How does the Packers' performance vary by season, and what trends are observable over time?

## Motivation  
Football teams experience performance fluctuations due to factors like roster changes, injuries, and coaching strategies. This study aims to:
- **Analyze offensive trends:** Examine how key metrics such as points scored, passing efficiency, and rushing performance fluctuate over time, and assess their impact on the Packers’ overall offensive success.
- **Evaluate sacks allowed and interceptions thrown:** Assess how the frequency of sacks and interceptions influences the Packers’ offensive efficiency and quarterback play, and identify potential areas for improvement.

By evaluating these metrics, we can gain deeper insights into the Packers' long-term strategies and their effectiveness. 

---

## Data Description  
The dataset includes game-level statistics for 117 Packers games from the regular seasons of the past seven NFL seasons, sourced from Pro-Football-Reference.com. Postseason games are not included in this dataset, ensuring that only regular-season performance is analyzed. The data captures a wide range of offensive, defensive, and special teams metrics, as well as the game outcomes. Key variables include passing (e.g., passing_y/a), rushing (e.g., rush_y/a), and overall game performance (e.g., total_points, opp_points, possession_time). Data was originally collected by NFL statisticians during each game and made publicly available through Pro Football Reference.

### Data Dictionary
- **id**: A unique identifier for each game. (Integer)
- **location**: Game location, either home or away. (Categorical)
- **opp**: Opponent team. (Categorical)
- **total_points**: Total points scored by the Packers in the game. (Integer)
- **opp_points**: Total points scored by the opponent team in the game. (Integer)
- **pass_completed**: Number of completed passes by the Packers. (Integer)
- **pass_attempts**: Number of pass attempts by the Packers. (Integer)
- **pass_yds**: Total passing yards by the Packers. (Integer)
- **pass_tds**: Total passing touchdowns by the Packers. (Integer)
- **int**: Number of interceptions thrown by the Packers. (Integer)
- **sacks**: Number of sacks allowed by the Packers’ offense. (Integer)
- **sacks_yds**: Total yards lost due to sacks. (Integer)
- **passing_y/a**: Passing yards per attempt. (Float)
- **passing_ny/a**: Net passing yards per attempt, including sacks. (Float)
- **cmp**: Completion percentage for passes. (Float)
- **passer_rating**: Passer rating, a measure of quarterback performance. (Float)
- **rush_attempts**: Total rushing attempts by the Packers. (Integer)
- **rush_yds**: Total rushing yards by the Packers. (Integer)
- **rush_y/a**: Rushing yards per attempt. (Float)
- **rushing_tds**: Total rushing touchdowns by the Packers. (Integer)
- **fgm**: Field goals made. (Integer)
- **fga**: Field goals attempted. (Integer)
- **xpm**: Extra points made after touchdowns. (Integer)
- **xpa**: Extra points attempted. (Integer)
- **punts**: Total number of punts by the Packers. (Integer)
- **punt_yds**: Total punting yards. (Integer)
- **3dconv**: Number of successful 3rd down conversions. (Integer)
- **3datt**: Number of 3rd down attempts. (Integer)
- **4dconv**: Number of successful 4th down conversions. (Integer)
- **4datt**: Number of 4th down attempts. (Integer)
- **possession_time**: Total time of possession (in minutes) for the Packers. (Time)
- **season**: The NFL season during which the game was played. (Categorical) 

*Note:* The dataset excludes playoff games to focus solely on regular-season performance.  

---
  
# Hypotheses  
1. **Offensive performance trends over time**:  
   - Total points scored, rushing yards per attempt, and passing efficiency (passing yards per attempt and passer rating) will show notable fluctuations or improvements across different seasons.
2. **Impact of sacks allowed and interceptions thrown on offensive efficiency**:  
   - A higher number of sacks allowed and interceptions thrown will negatively affect offensive efficiency, leading to fewer scoring opportunities and potentially influencing overall game outcomes. Teams that struggle to protect the quarterback and avoid turnovers tend to experience lower offensive performance and higher defensive pressures.

---

## Project Features  
- **Season-wise statistical summary**: Computes averages of key metrics per season.
- **Trend visualizations**: Line plots tracking offensive and defensive performance.
- **Correlation analysis**: Examines the relationship between possession time and total points scored.
- **Automated data processing**: Cleans and transforms raw game data for easy analysis.
- **CSV export**: Saves processed season-wise statistics for further exploration.

---

## Future Analysis Plans  
In the future, I plan to expand the analysis to focus on:
- **Opponent Analysis**: Evaluating the Packers' performance against specific teams, considering team-specific statistics, historical performance, and matchup data.
- **Home vs Away Performance**: Analyzing how the Packers' performance differs between home and away games.
- **Third and Fourth Down Conversions**: Exploring whether the Packers perform better on 3rd or 4th down conversions and how this impacts overall game outcomes.
- **Additional Variables**: Incorporating more variables to further refine the model and improve predictions.

---

## Installation & Usage  

### Install Dependencies  
Ensure Python is installed, then run:  
```bash
pip install pandas matplotlib seaborn numpy