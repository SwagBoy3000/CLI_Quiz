import random
import json
import os

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
        print("6. Save/Load Menu")
        print("7. Back to Main")
        
        choice = gt_vld_in("Choice (1-7): ", 1, 7)
        
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
                save_load_menu()
            case 7:
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

############## SAVES MANAGER #################
def save_load_menu():
    """Menu for save/load operations"""
    while True:
        clr_scrn()
        shw_hdr("SAVE/LOAD MENU")
        
        print("1. Save Current Questions")
        print("2. Load Questions from File")
        print("3. List All Saves")
        print("4. Delete a Save")
        print("5. Back to Manager")
        
        choice = gt_vld_in("Choice (1-5): ", 1, 5)
        
        match choice:
            case 1:
                # Ask for filename
                filename = input("Enter save name (without .json): ").strip()
                if filename:
                    if not filename.endswith('.json'):
                        filename += ".json"
                    save_questions(filename)
                else:
                    print("✗ No filename entered!")
                    input("\nPress Enter to continue...")
            case 2:
                # Show available files first
                if os.path.exists("quiz_saves"):
                    files = [f for f in os.listdir("quiz_saves") if f.endswith('.json')]
                    if files:
                        print("Available files:")
                        for f in files[:5]:  # Show first 5
                            print(f"  {f}")
                        print("... or enter any filename")
                    else:
                        print("No save files found.")
                
                filename = input("\nEnter filename to load: ").strip()
                if filename:
                    if not filename.endswith('.json'):
                        filename += ".json"
                    load_questions(filename)
                else:
                    print("✗ No filename entered!")
                    input("\nPress Enter to continue...")
            case 3:
                list_saves()
            case 4:
                delete_save()
            case 5:
                return
        #end match
    #end while
#end save_load_menu

def delete_save():
    """Delete a save file"""
    if not os.path.exists("quiz_saves"):
        print("No saves folder found.")
        input("\nPress Enter to continue...")
        return
    
    files = [f for f in os.listdir("quiz_saves") if f.endswith('.json')]
    
    if not files:
        print("No save files to delete.")
        input("\nPress Enter to continue...")
        return
    
    # Show available files
    print("Select save to delete:")
    for i, file in enumerate(files, 1):
        print(f"{i}. {file}")
    
    # Get user choice
    try:
        choice = int(input(f"\nEnter number (1-{len(files)}): "))
        if 1 <= choice <= len(files):
            file_to_delete = files[choice-1]
            filepath = os.path.join("quiz_saves", file_to_delete)
            
            # Confirm
            if input(f"Delete '{file_to_delete}'? (y/n): ").lower() == 'y':
                os.remove(filepath)
                print(f"✓ Deleted '{file_to_delete}'")
            else:
                print("✗ Delete cancelled")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Please enter a number!")
    
    input("\nPress Enter to continue...")
#end delete_save

def list_saves():
    """Show all available save files"""
    if not os.path.exists("quiz_saves"):
        print("No saves folder found. No saves available.")
        input("\nPress Enter to continue...")
        return
    
    files = [f for f in os.listdir("quiz_saves") if f.endswith('.json')]
    
    if not files:
        print("No save files found.")
    else:
        print("Available saves:")
        for i, file in enumerate(files, 1):
            # Show file info
            filepath = os.path.join("quiz_saves", file)
            size = os.path.getsize(filepath)
            
            # Count questions in file
            try:
                with open(filepath, 'r') as f:
                    q_count = len(json.load(f))
                print(f"{i:2}. {file} ({q_count} questions, {size} bytes)")
            except:
                print(f"{i:2}. {file} (corrupted)")
        #end for
    #end if
    
    input("\nPress Enter to continue...")
#end list_saves

def load_questions(filename="save.json"):
    """Load questions from a JSON file"""
    global qsts  # Need global to reassign entire list
    
    filepath = os.path.join("quiz_saves", filename)
    
    if not os.path.exists(filepath):
        print(f"✗ File '{filename}' not found!")
        input("\nPress Enter to continue...")
        return
    
    try:
        with open(filepath, 'r') as file:
            loaded = json.load(file)  # Load JSON back to list
        
        # Ask for confirmation before overwriting
        print(f"Found {len(loaded)} questions in '{filename}'")
        if input("Load these questions? (y/n): ").lower() == 'y':
            qsts = loaded
            print(f"✓ Loaded {len(qsts)} questions!")
        else:
            print("✗ Load cancelled")
    except Exception as e:
        print(f"✗ Error loading: {e}")
    #end try
    
    input("\nPress Enter to continue...")
#end load_questions

def save_questions(filename="save.json"):
    """Save questions to a JSON file"""
    # Create saves folder if it doesn't exist
    if not os.path.exists("quiz_saves"):
        os.makedirs("quiz_saves")
    #end if
    
    # Create full path
    filepath = os.path.join("quiz_saves", filename)
    
    try:
        with open(filepath, 'w') as file:
            json.dump(qsts, file)  # Convert list to JSON
        print(f"✓ Saved {len(qsts)} questions to '{filename}'")
    except Exception as e:
        print(f"✗ Error saving: {e}")
    #end try
    
    input("\nPress Enter to continue...")
#end save_questions

############## MAIN EXECUTION #############
if __name__ == "__main__":
    try:
        print("Quiz Game Starting...")
        
        # Try to auto-load last save
        if os.path.exists("quiz_saves/autosave.json"):
            try:
                with open("quiz_saves/autosave.json", 'r') as f:
                    qsts = json.load(f)
                print(f"✓ Auto-loaded {len(qsts)} questions")
            except:
                pass
            #end try
        #end if
        
        main_menu()
        
        # Auto-save on exit
        if not os.path.exists("quiz_saves"):
            os.makedirs("quiz_saves")
        #end if 
        with open("quiz_saves/autosave.json", 'w') as f:
            json.dump(qsts, f)
        #end with
        print(f"✓ Auto-saved {len(qsts)} questions")
        
        print("\nGoodbye!")
    except KeyboardInterrupt:
        print("\n\nProgram interrupted")
    except Exception as e: #catches any error
        print(f"\nError: {e}")
    #end try
#end if