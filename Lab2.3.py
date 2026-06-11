import sys

def run_recipe_ai():
    print("==================================================")
    print("   WELCOME TO THE RULE-BASED RECIPE ASSISTANT    ")
    print("==================================================\n")
    
    # Requirement: Gather user inputs
    ingredients_input = input("What primary protein/ingredient do you have? (e.g., salmon, burger, chicken): ").lower()
    diet_input = input("Enter any dietary preference or macro goals (e.g., low carb, high calorie, none): ").lower()
    
    # Initialize variables to hold our system's logical state
    chosen_recipe = ""
    side_dish = "standard sides"
    temp_setting = ""
    internal_target = ""
    macro_multiplier = 1.0
    
    # -------------------------------------------------------------------------
    # PART 3 REQUIREMENT: Rule-Based Decision-Making using Conditionals (If-Elif-Else)
    # -------------------------------------------------------------------------
    
    # RULE 1: Determine primary recipe based on keyword matching
    if "salmon" in ingredients_input:
        chosen_recipe = "Lemon-Herb Seared Salmon"
        side_dish = "roasted asparagus and seasoned rice"
        temp_setting = "190°C (375°F)"
        internal_target = "63°C (145°F)"
    elif "burger" in ingredients_input or "beef" in ingredients_input:
        chosen_recipe = "Classic High-Protein Beef Smashburgers"
        side_dish = "toasted brioche buns and baked fries"
        temp_setting = "220°C (425°F)"
        internal_target = "71°C (160°F)"
    elif "chicken" in ingredients_input:
        chosen_recipe = "Garlic Parmesan Chicken Tenders"
        side_dish = "steamed broccoli and sweet potato wedges"
        temp_setting = "200°C (400°F)"
        internal_target = "74°C (165°F)"
    else:
        # Fallback system logic if no primary keyword matches
        chosen_recipe = "Universal High-Protein Scrambled Egg & Meat Bowl"
        side_dish = "sliced avocado"
        temp_setting = "180°C (350°F)"
        internal_target = "Cook until completely firm"

    # RULE 2: Evaluate dietary preferences and modify variables using heuristics
    if "low carb" in diet_input:
        # Heuristic override for low carb parameter
        if chosen_recipe == "Classic High-Protein Beef Smashburgers":
            side_dish = "lettuce wraps and a side Caesar salad (no croutons)"
        elif chosen_recipe == "Lemon-Herb Seared Salmon":
            side_dish = "double serving of roasted asparagus"
        elif chosen_recipe == "Garlic Parmesan Chicken Tenders":
            side_dish = "steamed broccoli with olive oil"
    elif "high calorie" in diet_input:
        # Heuristic scaling multiplier for bulking/high calorie goals
        macro_multiplier = 1.5

    # -------------------------------------------------------------------------
    # PART 3 REQUIREMENT: Outputs Based on the Triggered Rules
    # -------------------------------------------------------------------------
    print("\n==================================================")
    print("          AI RECOMMENDATION GENERATED             ")
    print("==================================================")
    print(f"Recommended Recipe : {chosen_recipe}")
    print(f"Suggested Accompaniment: {side_dish}")
    print(f"Cooking Grid/Surface Temp: {temp_setting}")
    print(f"Target Safe Internal Temp: {internal_target}")
    
    if macro_multiplier > 1.0:
        print(f"Macro Adjustment   : Scale portions by {macro_multiplier}x for high-calorie targets.")
    else:
        print("Macro Adjustment   : Standard high-protein serving size.")
    print("==================================================\n")

if __name__ == "__main__":
    run_recipe_ai()