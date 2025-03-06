# A Season in the Sun: Packers’ Performance Through the Years  

## Project Overview  
This project analyzes the Green Bay Packers' performance over the past seven NFL seasons, examining season-by-season trends in offensive and defensive efficiency. Using game-level statistics, we investigate key performance metrics to identify patterns, strengths, and areas for improvement.  

## Research Question  
How does the Packers’ performance vary by season, and what trends are observable over time?  

## Motivation  
Football teams experience performance fluctuations due to factors like roster changes, injuries, and coaching strategies. This study aims to:  
- **Track offensive trends** (e.g., points scored, passing/rushing efficiency).  
- **Assess defensive consistency** (e.g., points allowed, sacks).  
- **Analyze correlations** between time of possession and overall success.  

By evaluating these metrics, we can gain deeper insights into the Packers’ long-term strategies and their effectiveness.  

---

### Data Description
The dataset includes game-level statistics for 117 Packers games from the regular seasons of the past seven NFL seasons, sourced from Pro-Football-Reference.com. Postseason games are not included in this dataset, ensuring that only regular season performance is analyzed. The data captures a wide range of offensive, defensive, and special teams metrics, as well as the game outcomes. Key variables include passing (e.g., passing_y/a), rushing (e.g., rush_y/a), and overall game performance (e.g., total_points, opp_points, possession_time). Data was originally collected by NFL statisticians during each game and made publicly available through Pro Football Reference.

### Data Dictionary
	•	id: A unique identifier for each game. (Integer)
	•	location: Game location, either home or away. (Categorical)
	•	opp: Opponent team. (Categorical)
	•	total_points: Total points scored by the Packers in the game. (Integer)
	•	opp_points: Total points scored by the opponent team in the game. (Integer)
	•	pass_completed: Number of completed passes by the Packers. (Integer)
	•	pass_attempts: Number of pass attempts by the Packers. (Integer)
	•	pass_yds: Total passing yards by the Packers. (Integer)
	•	pass_tds: Total passing touchdowns by the Packers. (Integer)
	•	int: Number of interceptions thrown by the Packers. (Integer)
	•	sacks: Number of sacks allowed by the Packers’ offense. (Integer)
	•	sacks_yds: Total yards lost due to sacks. (Integer)
	•	passing_y/a: Passing yards per attempt. (Float)
	•	passing_ny/a: Net passing yards per attempt, including sacks. (Float)
	•	cmp: Completion percentage for passes. (Float)
	•	passer_rating: Passer rating, a measure of quarterback performance. (Float)
	•	rush_attempts: Total rushing attempts by the Packers. (Integer)
	•	rush_yds: Total rushing yards by the Packers. (Integer)
	•	rush_y/a: Rushing yards per attempt. (Float)
	•	rushing_tds: Total rushing touchdowns by the Packers. (Integer)
	•	fgm: Field goals made. (Integer)
	•	fga: Field goals attempted. (Integer)
	•	xpm: Extra points made after touchdowns. (Integer)
	•	xpa: Extra points attempted. (Integer)
	•	punts: Total number of punts by the Packers. (Integer)
	•	punt_yds: Total punting yards. (Integer)
	•	3dconv: Number of successful 3rd down conversions. (Integer)
	•	3datt: Number of 3rd down attempts. (Integer)
	•	4dconv: Number of successful 4th down conversions. (Integer)
	•	4datt: Number of 4th down attempts. (Integer)
	•	possession_time: Total time of possession (in minutes) for the Packers. (Time)
	•	season: The NFL season during which the game was played. (Categorical) 

*Note:* The dataset excludes playoff games to focus solely on regular-season performance.  

---

## 📌 Hypotheses  
1. **Offensive performance trends over time:**  
   - Total points scored, passing yards, and rushing yards will show consistent trends or fluctuations.  
2. **Defensive performance variability:**  
   - Opponent points allowed and sacks will exhibit greater season-to-season variations.  
3. **Impact of possession time:**  
   - Longer possession time will correlate with higher points scored and better overall performance.  

---

## 🚀 Project Features  
✅ **Season-wise statistical summary:** Computes averages of key metrics per season.  
✅ **Trend visualizations:** Line plots tracking offensive and defensive performance.  
✅ **Correlation analysis:** Examines the relationship between possession time and total points scored.  
✅ **Automated data processing:** Cleans and transforms raw game data for easy analysis.  
✅ **CSV export:** Saves processed season-wise statistics for further exploration.  

---

## 🛠️ Installation & Usage  

### 1️⃣ Install Dependencies  
Ensure Python is installed, then run:  
```bash
pip install pandas matplotlib seaborn numpy
