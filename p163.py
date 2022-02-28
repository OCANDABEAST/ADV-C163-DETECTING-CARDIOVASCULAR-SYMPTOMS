from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Fever_Report")
root.geometry("600x600")

question1_radioButton=StringVar(value="0")

Question1=Label(root, text ="Do you Experience shortness of breath durning routine activities")
Question1.pack()
question_r1=Radiobutton(root, text = "yes", variable=question1_radioButton, value="yes")
question_r1.pack()
question_r2=Radiobutton(root, text = "no", variable=question1_radioButton, value="no")
question_r2.pack()

question2_radioButton=StringVar(value="0")
Question2=Label(root, text ="Do you have swelling in the feet/ ankles/legs")
Question2.pack()
question_r2=Radiobutton(root, text = "yes", variable=question2_radioButton, value="yes")
question_r2.pack()
question_r2=Radiobutton(root, text = "no", variable=question2_radioButton, value="no")
question_r2.pack()

question3_radioButton=StringVar(value="0")
Question3=Label(root, text ="Do you have any of these symptoms - confusion, disorientation or loss of memory?")
Question3.pack()
question_r3=Radiobutton(root, text = "yes", variable=question3_radioButton, value="yes")
question_r3.pack()
question_r3=Radiobutton(root, text = "no", variable=question3_radioButton, value="no")
question_r3.pack()

question4_radioButton=StringVar(value="0")
Question4=Label(root, text ="Do you Experience shortness of breath whille at rest/lying down?")
Question4.pack()
question_r4=Radiobutton(root, text = "yes", variable=question4_radioButton, value="yes")
question_r4.pack()
question_r4=Radiobutton(root, text = "no", variable=question4_radioButton, value="no")
question_r4.pack()

question5_radioButton=StringVar(value="0")
Question5=Label(root, text ="Do you experience persistent wheezing/ coughing that produce white or pink blood tinged mucus?")
Question5.pack()
question_r5=Radiobutton(root, text = "yes", variable=question5_radioButton, value="yes")
question_r5.pack()
question_r5=Radiobutton(root, text = "no", variable=question5_radioButton, value="no")
question_r5.pack()

def fever_score():
    score = 0 
    if question1_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question2_radioButton.get()=="yes":
         score = score+20
         print(score)
    if question3_radioButton.get()=="yes":
          score = score+20
          print(score)
    if question4_radioButton.get()=="yes":
         score = score+20
         print(score)
    if question5_radioButton.get()=="yes":
          score = score+20
          print(score)
          
    if score <= 20:
        messagebox.showinfo("Report","You don't need to visit a doctor.")
    elif score > 20 and score <= 60:
        messagebox.showinfo("Report", "You might perhaps have to visit a doctor.")
    else:
        messagebox.showinfo("Report", "I Strongly advise you to visit a doctor.")
btn = Button(root, text= "click me", command= fever_score)
btn.pack()
root.mainloop()

