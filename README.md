## Part 1: Initial Project Ideas

The AI (Gemini) provided the following three ideas:

### 1. Project Idea 1: The Smart Tech Support & Device Diagnostic Assistant
* **Description:** Actively troubleshoots common tech issues (like a laptop not turning on, slow internet, or a smart watch failing to sync) by asking the user sequential questions.
* **Rule-Based Approach:** It uses nested if-elif-else structures acting as a decision tree.

### 2. Project Idea 2: The High-Protein “What’s in the Fridge?” Recipe Recommendation System
* **Description:** Suggests specific, tailored dinner recipes and optimal cooking guidelines based on whatever primary ingredients the user currently has available.
* **Rule-Based Approach:** It matches keywords from user input against a hardcoded dictionary of recipes.

### 3. Project Idea 3: The Retro Fantasy RPG Text Companion & Inventory Advisor
* **Description:** Acts as a classic text-based game master or dungeon master assistant, tracking a player's stats/inventory and deciding if they succeed at a task based strictly on mechanical rules.
* **Rule-Based Approach:** It evaluates text commands alongside stored variables.

**Chosen Idea:** The High-Protein Recipe Recommendation System

**Justification:** I am choosing this project because I am currently on my health fitness journey and am constantly struggling to find high protein meals to help me reach my macros daily. I would also like to see from the inside how software can handle various user inputs and run them through conditional logic to output precise recommendations without relying on probability models.

---

## Part 2: Rules/Logic for the Chosen System

The **High-Protein Recipe Recommendation System** follows these rules:

1. **Rule 1 (Primary Ingredient Matching):**
    * **IF** input contains "salmon" -> **THEN set base recipe to Lemon-Herb Seared Salmon.**
    * **ELIF** input contains "burger" or "beef" -> **THEN set base recipe to Classic High-Protein Beef Smashburgers.**
    * **ELIF** input contains "chicken" -> **THEN set base recipe to Garlic Parmesan Chicken Tenders.**
    * **ELSE** -> **THEN set base recipe to Universal High-Protein Scrambled Egg & Meat Bowl (Fallback Option).**

2. **Rule 2 (Dietary Preference / Macro Filters):**
    * **IF** user preference is "low carb" AND base recipe involves grains/carbs -> **THEN substitute the sides** (e.g., replace burger buns with lettuce wraps, replace pasta with zoodles).
    * **ELIF** user preference is "high calorie" -> **THEN scale up ingredient portion rules by 150% the overall macronutrient profile.**

3. **Rule 3 (Cooking/Hardware Optimization Heuristics):**
    * **IF** target recipe is Salmon -> **THEN output optimal surface temperature setting of 190°C (375°F) and a target internal pull temperature of 63°C (145°F).**
    * **IF** target recipe is Smashburgers -> **THEN output optimal surface temperature setting of 220°C (425°F) for maximum sear.**

---

## Part 3: Test Inputs Log

I collaborated with the AI (Gemini) and had it assist me in creating the code for the Recipe suggester. I fixed all errors and listened to the feedback of Gemini which allowed me to run three Tests (burger, chicken, salmon) with no errors. Comments have been added to the code to help explain the thought process.

Sample input and output from system execution:

### Test Case 1: Salmon Input with Low Carb Modifier
* **User Input - Primary:** salmon
* **User Input - Diet:** low carb
* **System Output:**
    * Recommended Recipe: Lemon-Herb Seared Salmon
    * Suggested Accompaniment: double serving of roasted asparagus *(Heuristic modification triggered successfully)*
    * Cooking Grid/Surface Temp: 190°C (375°F)
    * Target Safe Internal Temp: 63°C (145°F)
    * Macro Adjustment: Standard high-protein serving size.

### Test Case 2: Burger Input with High Calorie Modifier
* **User Input - Primary:** burger
* **User Input - Diet:** high calorie
* **System Output:**
    * Recommended Recipe: Classic High-Protein Beef Smashburgers
    * Suggested Accompaniment: toasted brioche buns and baked fries
    * Cooking Grid/Surface Temp: 220°C (425°F)
    * Target Safe Internal Temp: 71°C (160°F)
    * Macro Adjustment: Scale portions by 1.5x for high-calorie targets. *(Heuristic modification triggered successfully)*

### Test Case 3: Chicken Input with No Modifiers
* **User Input - Primary:** chicken
* **User Input - Diet:** none
* **System Output:**
    * Recommended Recipe: Garlic Parmesan Chicken Tenders
    * Suggested Accompaniment: steamed broccoli and sweet potato wedges
    * Cooking Grid/Surface Temp: 200°C (400°F)
    * Target Safe Internal Temp: 74°C (165°F)
    * Macro Adjustment: Standard high-protein serving size.

---


## Part 4: Reflection and Submission

My rule-based AI system works using straightforward, hardcoded logic instead of a modern machine learning model. The entire program runs on a basic if-elif-else pipeline that scans whatever the user types for specific keywords. For example, if the user inputs "salmon" or "burger," the script triggers a matching rule that sets up specific variables like the recipe name, standard side dishes, and the ideal cooking temperatures for a griddle. On top of that, I added a second layer of conditional logic to handle dietary goals. If a user inputs "low carb," the program goes in and dynamically changes the variables, swapping out heavy carbs like buns or rice for extra vegetables.

Working alongside an AI assistant to build this project was helpful, but it came with a few hurdles. The main challenge was keeping the AI focused on fixed, static rules. At first, it wanted to use advanced text parsing like regular expressions or fuzzy string matching, which felt too much like modern machine learning shortcuts. Because real-world user input can be unpredictable, a purely rule-based program requires you to map out every single possibility yourself. To prevent the script from crashing or breaking if someone typed something completely random, I had to prompt the AI to help me build a solid else fallback statement that acts as a catch-all safety net.

Overall, this project really showed me how early AI software worked before machine learning took over. In the past, developers had to act as domain experts and manually hardcode every piece of human logic directly into the software. While this kind of system is fast and incredibly predictable, it completely lacks the flexibility to adapt to things it wasn't specifically programmed for. It makes total sense why the tech industry eventually shifted toward data-driven, statistical models to handle how random and dynamic human users actually are.