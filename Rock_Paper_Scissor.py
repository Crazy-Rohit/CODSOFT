#!/usr/bin/env python
# coding: utf-8

# In[8]:


import tkinter as tk
from tkinter import messagebox
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0, 0
    elif (user_choice == 'rock' and computer_choice == 'scissors') or          (user_choice == 'scissors' and computer_choice == 'paper') or          (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!", 1, 0
    else:
        return "Computer wins!", 0, 1

def play_game(user_choice):
    global user_score, computer_score, total_trials, chances_remaining
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    result, user_points, computer_points = determine_winner(user_choice, computer_choice)
    user_score += user_points
    computer_score += computer_points
    total_trials -= 1
    chances_remaining -= 1
    
    if chances_remaining > 0:
        messagebox.showinfo("Result", f"Computer chose: {computer_choice}\n{result}\nYour score: {user_score}\nComputer's score: {computer_score}\nChances remaining: {chances_remaining}")
    else:
        if user_score > computer_score:
            messagebox.showinfo("Game Over", "Congratulations! You win the game!")
        elif user_score < computer_score:
            messagebox.showinfo("Game Over", "Sorry, you lose the game.")
        else:
            messagebox.showinfo("Game Over", "It's a tie!")
        
        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
        if play_again:
            user_score = 0
            computer_score = 0
            total_trials = 5
            chances_remaining = total_trials
            return
        else:
            root.destroy()

def main():
    global user_score, computer_score, total_trials, chances_remaining
    user_score = 0
    computer_score = 0
    total_trials = 5
    chances_remaining = total_trials

    root = tk.Tk()
    root.title("Rock Paper Scissors Game")
    root.geometry("400x500")
    root.configure(bg="#f0f0f0")
    
    heading_label = tk.Label(root, text="Rock Paper Scissors", bg="#f0f0f0", font=("Times New Roman", 24, "bold"),fg="red")
    heading_label.pack(pady=10)
    
    rules_text = "Rules of the Game:\n\nRock beats Scissors\nScissors beats Paper\nPaper beats Rock"
    rules_label = tk.Label(root, text=rules_text, bg="#f0f0f0", font=("Times New Roman", 18, "bold"), fg="blue", justify="left")
    rules_label.pack(pady=10)
    
    user_score_label = tk.Label(root, text=f"Your Score: {user_score}", bg="#f0f0f0", font=("Arial", 12))
    user_score_label.pack()
    
    chances_label = tk.Label(root, text=f"Chances Remaining: {chances_remaining}", bg="#f0f0f0", font=("Arial", 12))
    chances_label.pack()

    def on_button_click(choice):
        play_game(choice)
        user_score_label.config(text=f"Your Score: {user_score}")
        chances_label.config(text=f"Chances Remaining: {chances_remaining}")

    rock_button = tk.Button(root, text="Rock", width=10, height=2, command=lambda: on_button_click("rock"), bg="#FF5733", fg="white", font=("Arial", 12, "bold"))
    paper_button = tk.Button(root, text="Paper", width=10, height=2, command=lambda: on_button_click("paper"), bg="#3498DB", fg="white", font=("Arial", 12, "bold"))
    scissors_button = tk.Button(root, text="Scissors", width=10, height=2, command=lambda: on_button_click("scissors"), bg="#27AE60", fg="white", font=("Arial", 12, "bold"))
    
    rock_button.pack(pady=10)
    paper_button.pack(pady=10)
    scissors_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()


# In[ ]:




