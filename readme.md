# Diabetes Cube Trainer

## Comprehensive Description of the Diabetes Simulator

**Author:** Vasiliy Dautov  
**License:** Open Source ([MIT License](https://opensource.org/licenses/MIT))

### Project Name
**"Diabetes Cube Trainer"**  
An interactive simulator for learning blood glucose management in diabetes. Based on the "Rubik's Cube" game mechanics, where users learn to balance insulin, nutrition, and physical activity.

### Project Goals
The simulator is designed for:
1. **Educating diabetes patients** on the basics of blood glucose management.
2. **Developing self-control skills** through hands-on experimentation with parameters.
3. **Visualizing decision consequences** (hypoglycemia, hyperglycemia) in real-time.

### Concept
The simulator uses a Rubik's Cube analogy:
- In the initial state ("solved"), all parameters are normal: blood glucose is within the target range, insulin dosage matches the body's needs, and nutrition and activity are balanced.
- The user "scrambles" the system by adjusting parameters (e.g., increasing insulin dose or reducing carbs), leading to changes in blood glucose levels.
- The user's task is to "solve" the cube again by adjusting parameters to restore blood glucose to normal levels.

### Core Features
1. **Parameter Management**:
   - **Insulin Dose**: Specified in units (U). Bolus insulin affects glucose reduction.
   - **Carbohydrates**: Specified in grams or bread units (BU). Complex carbs are accounted for via **glycemic load (GL)**.
   - **Physical Activity**: Specified in minutes. Intensity affects the rate of glucose reduction.

2. **Blood Glucose Simulation**:
   - Glucose levels are calculated based on input parameters, accounting for delays in insulin and food action.
   - If glucose levels exceed the target range (4–7 mmol/L), the system alerts the user.

3. **System State Visualization**:
   - **Rubik's Cube**:
     - A solved cube symbolizes normal conditions (all parameters in range).
     - A scrambled cube shows deviations (hypoglycemia or hyperglycemia).
   - **Glucose Level Graph**:
     - Real-time display of glucose level trends.
     - Target glucose level (5.5 mmol/L) and normal range (4–7 mmol/L) are highlighted.

4. **Reset Function**:
   - A "Reset" button returns the system to its initial state (glucose level: 5.5 mmol/L, all parameters normalized).

### Interface
1. **Left Panel (Parameter Controls)**:
   - Input field for insulin dose.
   - Input field for carbohydrate amount.
   - Input field for glycemic load (GL).
   - Slider for physical activity level.
   - "Apply Changes" and "Reset" buttons.

2. **Right Panel (Visualization)**:
   - **Rubik's Cube**: Displays the current system state.
   - **Glucose Level**: Text indicator with the current value.
   - **Graph**: Shows historical glucose level changes over time.

### Glucose Level Calculation Model
Glucose levels are calculated using the formula:  
![image](https://github.com/user-attachments/assets/7552599a-d45f-462a-bd62-d11d39ee6b94)  
Where:
- **carbs**: Carbohydrate amount (g).
- **glycemic_load**: Glycemic load (GL).
- **insulin**: Insulin dose (U).
- **activity**: Physical activity level (min).

The result is added to the current glucose level. If the value exceeds the normal range, the cube becomes "scrambled."

### Educational Aspects
1. **Understanding Relationships**:
   - How insulin affects glucose levels.
   - How nutrition and activity adjust these levels.
2. **Developing Self-Control Skills**:
   - Predicting the consequences of actions.
   - Learning to respond quickly to glucose level changes.
3. **Gamified Motivation**:
   - Enjoyable learning process.
   - Progress tracking.

### Future Improvements
1. **Insulin Action Time Modeling**:
   - Account for insulin peak action (e.g., after 1–2 hours).
2. **Device Integration**:
   - Connect with CGM (continuous glucose monitoring) devices.
3. **Difficulty Settings**:
   - Add difficulty levels for tailored learning.
4. **Mobile Version**:
   - Adapt the app for smartphones.

---

**License Notice:**  
This project is open source under the MIT License. Feel free to use, modify, and distribute it as per the license terms. Contributions are welcome!
