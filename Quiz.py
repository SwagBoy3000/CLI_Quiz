import random

qsts = [("What is the capital of France?", "Paris"),
        ("What is the capital of Germany?", "Berlin")]

############## UTILITY FUNCTIONS #############
def clr_scrn():
    """Clear terminal screen"""
    print("\n" * 3) #just enters white spaces till screen is empty
#end clr_scrn

def gt_vld_in(prompt, min_val, max_val):#Prompt:"the input prompt", min/max_val:"the interval of acceptable inputs"
    """Get integer input with validation"""
    while True: #Loop to keep asking for input till valid
        try:
            value = input(prompt).lower().strip() #input always reteruns a string
            if value in ['c', 'cancel'] or not value: #To cancel or skip
                return None
            num = int(value)
            if min_val <= num <= max_val: #if input is acceptable
                return num
            print(f"Enter number {min_val}-{max_val}") #if input is outside range
        except ValueError: #if input is an invalid character meaning a problem when converting with int()
            print("Enter a valid number")
        #end try
    #end while
#end gt_vld_in

def shw_hdr(title): #title:"the title text entered as a param"
    """Display section header"""
    border = "=" * 40
    print(f"\n{border} \n{title:^40} \n{border} \n") #^40 center the text along a space of 40 why 40? cuz the "=" take up 40 and i want it to be centered
#end shw_hdr

############## MAIN MENU #############
def main_menu():
    """Display and handle main menu"""
    while True: #Keeps main menu on
        clr_scrn() #clear screen
        shw_hdr("QUIZ MAIN MENU") #Write what u want for header as a param 
        
        print("1. Start Game")
        print("2. Manage Questions")
        print("3. View Questions")
        print("4. Quit")
        
        choice = gt_vld_in("Choice (1-4): ", 1, 4) #Validate input
        
        match choice:
            case 1:
                game() #main game
            case 2:
                manage_questions()
            case 3:
                view_questions()
                input("\nPress Enter to continue...")
            case 4:
                print("\nThanks for playing!")
                return
            #end match
        #end match
    #end while
#end main_menu

############## GAME FUNCTIONS #############
def game():
    """Run the quiz game"""
    clr_scrn()
    shw_hdr("QUIZ GAME")
    
    if not qsts: #checks if the qsts array is empty note that u can access variables outside the function scope if it's a read only operation 
        print("No questions available!")
        print("Add questions in the manager.")
        input("\nPress Enter to continue...")
        return
    #end if
    
    # Determine how many questions to use
    q_count = min(5, len(qsts))
    if q_count < 5:
        print(f"Only {q_count} question(s) available")
        if input("Play anyway? (y/n): ").lower() != 'y':
            return
        #end if
    #end if
    
    # Select and shuffle questions
    questions = random.sample(qsts, q_count) if len(qsts) > q_count else qsts[:]
    random.shuffle(questions)
    
    score = 0
    for i, (q, a) in enumerate(questions, 1):
        print(f"\nQuestion {i}/{q_count}:")
        print(f"  {q}")
        
        usr_ans = input("Answer: ").replace(" ","").lower()
        correct_ans = a.replace(" ","").lower()
        
        if usr_ans == correct_ans:
            print("✓ Correct!")
            score += 1
        else:
            print(f"✗ Wrong! Correct answer: {a}")
        #end if
    #end for
    
    # Show results
    shw_hdr("RESULTS")
    print(f"Score: {score}/{q_count}")
    print(f"Percentage: {(score/q_count*100):.1f}%")
    
    input("\nPress Enter to continue...")
#end game

############## QUESTION MANAGEMENT #############
def manage_questions():
    """Question manager menu"""
    while True:
        clr_scrn()
        shw_hdr("QUESTION MANAGER")
        print(f"Total questions: {len(qsts)}\n")
        
        print("1. View All")
        print("2. Add Question")
        print("3. Delete Question")
        print("4. Edit Question")
        print("5. Delete All")
        print("6. Back to Main")
        
        choice = gt_vld_in("Choice (1-6): ", 1, 6)
        
        match choice:
            case 1:
                view_questions()
                input("\nPress Enter to continue...")
            case 2:
                add_question()
            case 3:
                delete_question()
            case 4:
                edit_question()
            case 5:
                delete_all()
            case 6:
                return
            #end match
        #end match
    #end while
#end manage_questions

def view_questions():
    """Display all questions"""
    clr_scrn()
    shw_hdr("ALL QUESTIONS")
    
    if not qsts:
        print("No questions available")
        return
    #end if
    
    for i, (q, a) in enumerate(qsts, 1):
        print(f"{i:2}. Q: {q}") #:2 means to format the variable i as a 2 character like it takes 2 spaces
        print(f"    A: {a}") #the 4 spaces create indentention in the output
        print("-" * 40)
    #end for
    
    print(f"\nTotal: {len(qsts)} question(s)")
#end view_questions

def add_question():
    """Add a new question"""
    clr_scrn()
    shw_hdr("ADD QUESTION")
    
    print("Enter new question:")
    question = " ".join(input("Question: ").split())
    answer = " ".join(input("Answer: ").split())
    
    if not question or not answer:
        print("Question and answer required!")
        input("\nPress Enter to continue...")
        return
    #end if
    
    qsts.append((question, answer))
    print(f"✓ Question added! Total: {len(qsts)}")
    input("\nPress Enter to continue...")
#end add_question

def delete_question():
    """Delete a specific question"""
    if not qsts:
        print("No questions to delete")
        input("\nPress Enter to continue...")
        return
    #end if
    
    view_questions()
    print("\nEnter question number to delete")
    choice = gt_vld_in(f"Choice (1-{len(qsts)}): ", 1, len(qsts))
    
    if choice is None:
        print("Delete cancelled")
        input("\nPress Enter to continue...")
        return
    #end if
    
    # Confirm deletion
    q, a = qsts[choice-1]
    print(f"\nYou selected:")
    print(f"  Q: {q[:50]}{'...' if len(q) > 50 else ''}")
    print(f"  A: {a[:50]}{'...' if len(a) > 50 else ''}")
    
    if input("\nDelete this question? (y/n): ").lower() == 'y':
        qsts.pop(choice-1)
        print("✓ Question deleted!")
    else:
        print("✗ Delete cancelled")
    #end if
    
    input("\nPress Enter to continue...")
#end delete_question

def edit_question():
    """Edit an existing question"""
    if not qsts:
        print("No questions to edit")
        input("\nPress Enter to continue...")
        return
    #end if
    
    view_questions()
    print("\nEnter question number to edit")
    choice = gt_vld_in(f"Choice (1-{len(qsts)}): ", 1, len(qsts))
    
    if choice is None:
        print("Edit cancelled")
        input("\nPress Enter to continue...")
        return
    #end if
    
    # Get current question
    q, a = qsts[choice-1]
    print(f"\nCurrent question:")
    print(f"  Q: {q}")
    print(f"  A: {a}")
    print("\nEnter new values (leave blank to keep current):")
    
    # Get new values
    new_q = " ".join(input("New question: ").split()) or q #input control if blank keep og values
    new_a = " ".join(input("New answer: ").split()) or a
    
    # Update
    qsts[choice-1] = (new_q, new_a)
    print("✓ Question updated!")
    input("\nPress Enter to continue...")
#end edit_question

def delete_all():
    """Delete all questions"""
    if not qsts:
        print("Already empty")
        input("\nPress Enter to continue...")
        return
    #end if
    
    print(f"This will delete all {len(qsts)} questions")
    if input("Are you sure? (yes/no): ").lower() == 'yes':
        qsts.clear()
        print("✓ All questions deleted")
    else:
        print("✗ Delete cancelled")
    #end if
    
    input("\nPress Enter to continue...")
#end delete_all

############## MAIN EXECUTION #############
if __name__ == "__main__":
    try:
        print("Quiz Game Starting...")
        main_menu()
        print("\nGoodbye!")
    except KeyboardInterrupt: #incase manual interruption
        print("\n\nProgram interrupted")
    except Exception as e: #catches any error 
        print(f"\nError: {e}")
    #end try
#end if
