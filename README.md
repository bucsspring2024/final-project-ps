[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14587785&assignment_repo_type=AssignmentRepo)

:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Simon
## CS110 Final Project  Spring, 2024

## Team Members

Parker Schafer

***

## Project Description

Memorize the pattern of the buttons and repeat it. Every completion the pattern gets longer.

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Buttons to click
2. Start Menu
3. obstacle collisions  
4. game over screen
5. Points and Highscore tracker

### Classes

- Button:
    - initializes the 4 buttons and handles lighting them on/off 
  SimonScore:
    - handles current score tracking and writing/reading highscore file for tracking.
  Utility:
    - holds constants

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      | 
