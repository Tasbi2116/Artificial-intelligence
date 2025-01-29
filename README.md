# 🤖 Artificial-Intelligence

This repository contains the lab work for the course **"Artificial Intelligence Laboratory"** (Credit: 1.50), implemented in **Python**. Each lab assignment includes source code and corresponding test cases.

## 📂 Repository Structure
The repository consists of the following directories:

### 1️⃣ Lab_1 AI - Vacuum Cleaner 🧹
A simple vacuum cleaner agent that cleans dirt in a given environment. It follows a predefined set of actions to move left, right, and suck dirt while tracking its performance.
- **📁 Directories:**
  - `source/` - Contains the implementation files:
    - `__init__.py`
    - `calculate_performance.py`
    - `main.py`
    - `move_left.py`
    - `move_right.py`
    - `random_dirt.py`
    - `suck_dirt.py`
  - `tests/` - Contains test cases for the above source files:
    - `test_calculate_performance.py`
    - `test_move_left.py`
    - `test_move_right.py`
    - `test_random_dirt.py`
    - `test_suck_dirt.py`

### 2️⃣ Lab_2 AI - Simple Agent 🎭
Implements a basic AI agent that perceives its environment and takes actions accordingly. This agent follows simple rules to interact with its surroundings and make decisions.
- **📁 Directories:**
  - `source/` - Contains the implementation:
    - `__init__.py`
    - `actions.py`
    - `agent.py`
    - `boundary.py`
    - `environment.py`
    - `result.py`
    - `simulation.py`
  - `tests/` - Contains test cases for the source files.

### 3️⃣ Lab_3 AI - Model Based Agent 🏗️
A model-based AI agent maintains an internal model of the environment to improve decision-making. This allows the agent to predict future states and optimize actions efficiently.
- **📁 Directories:**
  - `source/` - Contains implementation:
    - `__init__.py`
    - `actuators.py`
    - `calculate_nearest_object.py`
    - `environment.py`
    - `gui_setup.py`
    - `perceptions.py`
    - `simulation.py`
    - `target_movement.py`
  - `tests/` - Contains test cases for all implemented modules.

### 4️⃣ Lab_4 AI - Learning Agent 📚
An AI agent that learns from past experiences and optimizes its actions accordingly. It adapts based on collected data to improve its efficiency over time.
- **📄 Files:**
  - `main.py`
  - `test_main.py`

### 5️⃣ Reinforcement Agent 🎮
This agent learns optimal actions through reinforcement learning techniques. It uses trial and error to maximize rewards and improve its performance over multiple interactions.
- **📄 Files:**
  - `__init__.py`
  - `main.py`
  - `test_simulation_logic.py`

## 🛠️ Setup and Installation
To run the programs and test cases, follow these steps:

1. 🚀 Clone the repository:
   ```bash
   git clone https://github.com/Tasbi2116/Artificial-intelligence.git
   cd Artificial-Intelligence
   ```
2. 📦 Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. ▶️ Run the lab programs:
   ```bash
   python Lab_1_AI/source/main.py
   ```
4. 🧪 Run the test cases:
   ```bash
   pytest
   ```

## 🤝 Contributions
Feel free to fork the repository, submit pull requests, or report issues.

## 📧 Contact

Have any questions? Reach out via:

- **GitHub Issues**: [Submit an issue](../../issues)
- **Email**: [tasbi2116@cseku.ac.bd](tasbi2116@cseku.ac.bd)

## 📜 License
This project is licensed under the MIT License.

---
### 👨‍🏫 Author
Developed as part of the Artificial Intelligence Laboratory coursework under the guidance of **Dr. Amit Kumar Mondal, Associate Professor, CSE, Khulna University**.

---
