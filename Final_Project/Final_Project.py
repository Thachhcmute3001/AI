from tkinter import Tk, Label, Button, filedialog
from PIL import ImageTk, Image
from keras.models import load_model
from keras.utils import load_img
from keras.utils import img_to_array

# Global variable to store the imported image
imported_image = None

def import_image():
    global imported_image
    file_path = filedialog.askopenfilename()
    image = Image.open(file_path)
    # Perform operations on the image

    # Resize the image if needed
    image = image.resize((200, 200), Image.ANTIALIAS)

    # Convert the image to Tkinter-compatible format
    photo = ImageTk.PhotoImage(image)

    # Create a label to display the image
    image_label = Label(window, image=photo)
    image_label.image = photo  # Keep a reference to prevent garbage collection
    image_label.place(x = 70, y = 150)
    
    # Store the imported image
    imported_image = image
 
def detect_disease():
    global imported_image
    global top_three_classes
    global class_names
    model = load_model('Disease.h5')
    # Implement the skin disease detection logic
    try:
        img = imported_image.resize((80, 80), Image.LANCZOS)

        img = img_to_array(img)
        img = img.reshape(1, 80, 80, 3)
        img = img.astype('float32')
        predictions = model.predict(img)[0]
        class_names = ['Skin allergies', 'Eczema', 'Warts', 'Skin fungus', 'Genital warts', 'Skin cancer', 'Psoriasis']
    
        # Get the indices of the top three predictions
        top_three_indices = predictions.argsort()[-3:][::-1]
        
        # Get the corresponding class names and probabilities
        top_three_classes = [class_names[i] for i in top_three_indices]
        top_three_probabilities = [predictions[i] * 100 for i in top_three_indices]
        
        # Format the probabilities as percentages
        formatted_probabilities = ["{:.2f}%".format(probability) for probability in top_three_probabilities]
        
        # Create a string to display the top three predictions and their probabilities
        prediction_string = ""
        for i in range(3):
            prediction_string += "{}:   {}\n\n".format(top_three_classes[i],formatted_probabilities[i])
        # Update the label with the prediction information
        class_label.config(text=prediction_string, font = ("Comic Sans MS", 13, "bold"), justify="left")
    except:
        class_label.config(text="Please select an image", font = ("Comic Sans MS", 13, "bold"), justify="left")
       
def top1_button():
    global top_three_classes
    global class_names
    try:
        # Instructions based on predicted disease
        if  top_three_classes[0] == class_names[0]:
            instruction_label.config(text="For self-care of skin allergies, avoid \ntriggers, apply cool compresses, use \nover-the-counter antihistamines \nor corticosteroid creams."
                                    , justify="left")
        elif top_three_classes[0] == class_names[1]:
            instruction_label.config(text="For self-care of eczema, keep skin \nmoisturized, avoid irritants and allergens, use \nmild soaps, apply topical \ncorticosteroids or anti-itch creams."
                                    , justify="left")
        elif  top_three_classes[0] == class_names[2]:
            instruction_label.config(text="For self-care of warts, keep the area \nclean and dry, avoid picking or scratching, use \nover-the-counter wart treatments \nor consult a pharmacist, and seek medical \nadvice if they persist or spread.",
                                    justify="left")
        elif  top_three_classes[0] == class_names[3]:
            instruction_label.config(text="For self-care of skin fungus, keep the \narea clean and dry, avoid sharing \npersonal items, use antifungal \ncreams or powders, and seek medical advice if \nsymptoms worsen or don't improve.",
                                    justify="left")
        elif  top_three_classes[0] == class_names[4]:
            instruction_label.config(text="For self-care of genital warts, abstain \nfrom sexual activity, keep the area \nclean and dry, avoid picking or \nscratching, and seek medical advice for \nproper diagnosis and treatment.",
                                    justify= "left")
        elif  top_three_classes[0] == class_names[5]:
            instruction_label.config(text="For self-care of skin cancer, regularly \ncheck your skin for changes, protect \nfrom sun exposure, wear protective \nclothing, and consult a healthcare professional \nfor evaluation and treatment.",
                                    justify= "left")
        elif  top_three_classes[0] == class_names[6]:
            instruction_label.config(text="For self-care of psoriasis, keep the skin \nmoisturized, avoid triggers, manage \nstress, use topical treatments or \nphototherapy, and consult a healthcare \nprofessional for personalized guidance.",
                                    justify="left")
    except:
        instruction_label.config(text="Please select the image")
        
def top2_button():
    global top_three_classes
    global class_names
    try:
        # Instructions based on predicted disease
        if  top_three_classes[1] == class_names[0]:
            instruction_label.config(text="For self-care of skin allergies, avoid \ntriggers, apply cool compresses, use \nover-the-counter antihistamines \nor corticosteroid creams."
                                    , justify="left")
        elif top_three_classes[1] == class_names[1]:
            instruction_label.config(text="For self-care of eczema, keep skin \nmoisturized, avoid irritants and allergens, use \nmild soaps, apply topical \ncorticosteroids or anti-itch creams."
                                    , justify="left")
        elif  top_three_classes[1] == class_names[2]:
            instruction_label.config(text="For self-care of warts, keep the area \nclean and dry, avoid picking or scratching, use \nover-the-counter wart treatments \nor consult a pharmacist, and seek medical \nadvice if they persist or spread.",
                                    justify="left")
        elif  top_three_classes[1] == class_names[3]:
            instruction_label.config(text="For self-care of skin fungus, keep the \narea clean and dry, avoid sharing \npersonal items, use antifungal \ncreams or powders, and seek medical advice if \nsymptoms worsen or don't improve.",
                                    justify="left")
        elif  top_three_classes[1] == class_names[4]:
            instruction_label.config(text="For self-care of genital warts, abstain \nfrom sexual activity, keep the area \nclean and dry, avoid picking or \nscratching, and seek medical advice for \nproper diagnosis and treatment.",
                                    justify= "left")
        elif  top_three_classes[1] == class_names[5]:
            instruction_label.config(text="For self-care of skin cancer, regularly \ncheck your skin for changes, protect \nfrom sun exposure, wear protective \nclothing, and consult a healthcare professional \nfor evaluation and treatment.",
                                    justify= "left")
        elif  top_three_classes[1] == class_names[6]:
            instruction_label.config(text="For self-care of psoriasis, keep the skin \nmoisturized, avoid triggers, manage \nstress, use topical treatments or \nphototherapy, and consult a healthcare \nprofessional for personalized guidance.",
                                    justify="left")
    except:
        instruction_label.config(text="Please select the image")
      
def top3_button():
    global top_three_classes
    global class_names
    try:
        # Instructions based on predicted disease
        if  top_three_classes[2] == class_names[0]:
            instruction_label.config(text="For self-care of skin allergies, avoid \ntriggers, apply cool compresses, use \nover-the-counter antihistamines \nor corticosteroid creams."
                                    , justify="left")
        elif top_three_classes[2] == class_names[1]:
            instruction_label.config(text="For self-care of eczema, keep skin \nmoisturized, avoid irritants and allergens, use \nmild soaps, apply topical \ncorticosteroids or anti-itch creams."
                                    , justify="left")
        elif  top_three_classes[2] == class_names[2]:
            instruction_label.config(text="For self-care of warts, keep the area \nclean and dry, avoid picking or scratching, use \nover-the-counter wart treatments \nor consult a pharmacist, and seek medical \nadvice if they persist or spread.",
                                    justify="left")
        elif  top_three_classes[2] == class_names[3]:
            instruction_label.config(text="For self-care of skin fungus, keep the \narea clean and dry, avoid sharing \npersonal items, use antifungal \ncreams or powders, and seek medical advice if \nsymptoms worsen or don't improve.",
                                    justify="left")
        elif  top_three_classes[2] == class_names[4]:
            instruction_label.config(text="For self-care of genital warts, abstain \nfrom sexual activity, keep the area \nclean and dry, avoid picking or \nscratching, and seek medical advice for \nproper diagnosis and treatment.",
                                    justify= "left")
        elif  top_three_classes[2] == class_names[5]:
            instruction_label.config(text="For self-care of skin cancer, regularly \ncheck your skin for changes, protect \nfrom sun exposure, wear protective \nclothing, and consult a healthcare professional \nfor evaluation and treatment.",
                                    justify= "left")
        elif  top_three_classes[2] == class_names[6]:
            instruction_label.config(text="For self-care of psoriasis, keep the skin \nmoisturized, avoid triggers, manage \nstress, use topical treatments or \nphototherapy, and consult a healthcare \nprofessional for personalized guidance.",
                                    justify="left")
    except:
        instruction_label.config(text="Please select the image")

def exit_app():
    window.destroy()

window = Tk()
window.title("SKIN DISEASE DETECTOR")

# Set the window size
window.geometry("800x600")

import_button = Button(window, text="IMPORT IMAGE",font = ("Arial", 11, "bold"), command=import_image, bg="blue", fg="white", width= 15, height=2)
import_button.place(x = 600, y = 130)

# Button for detecting disease
detect_button = Button(window, text="DETECT DISEASE",font = ("Arial", 11, "bold"), command=detect_disease, bg="blue", fg="white", width= 15, height=2)
detect_button.place(x = 600, y = 200)

# Button for top 1 disease
first_button = Button(window,font = ("Arial", 11, "bold"), command=top1_button, bg="red", width = 2, height = 1)
first_button.place(x = 550, y = 150)

# Button for top 2 disease
second_button = Button(window,font = ("Arial", 11, "bold"), command=top2_button, bg="red", width = 2, height = 1)
second_button.place(x = 550, y = 200)

# Button for top 3 disease
third_button = Button(window,font = ("Arial", 11, "bold"), command=top3_button, bg="red", width = 2, height = 1)
third_button.place(x = 550, y = 250)

# Button for exiting the app
exit_button = Button(window, text="EXIT",font = ("Arial", 11, "bold"), command=exit_app, bg="blue", fg="white", width= 15, height=2)
exit_button.place(x = 600, y = 270)

# Create a label for the tittle
tittle_label = Label(window, text="Skin Disease Detection Using Convolutional Neutral Network",
                      font = ("Arial", 16, "bold", "italic"), fg = "red")
tittle_label.place(x = 100, y = 50)

# Create a label for the student information
student_label = Label(window, text="Nguyen Ba Vu Thach - MSSV: 20146530",
                      font = ("Comic Sans MS", 13, "bold"), fg = "black")
student_label.place(x = 20, y = 10)

university_label = Label(window, text="University of Education and Technology",
                      font = ("Comic Sans MS", 13, "bold"), fg = "black")
university_label.place(x = 450, y = 10)

# Create a label for the image name
name_label = Label(window, text="DETECTED DISEASE", font = ("Comic Sans MS", 13))
name_label.place(x = 300, y = 120)

# Create a label for imported image
imported_label = Label(window, text="IMPORT IMAGE", font = ("Comic Sans MS", 13))
imported_label.place(x = 100, y = 120)

# Create a label for Guidance
guidance_label = Label(window, text="INSTRUCTION - CLICK THE RED BUTTON", font = ("Comic Sans MS", 13, "bold"), fg = "red")
guidance_label.place(x = 20, y = 370)

# Create a label for information contact:
contact_label = Label(window, text="CONTACT INFORMATION:", font = ("Comic Sans MS", 13, "bold"), fg = "red")
contact_label.place(x = 450, y = 370)

name2_label = Label(window, text="Nguyen Ba Vu Thach", font = ("Comic Sans MS", 12))
name2_label.place(x = 450, y = 400)

gmail_label = Label(window, text="Gmail: 20146530@student.hcmute.edu.vn", font = ("Comic Sans MS", 12))
gmail_label.place(x = 450, y = 430)

phone_label = Label(window, text="Contact number: 0985075354", font = ("Comic Sans MS", 12))
phone_label.place(x = 450, y = 460)

youtube_label = Label(window, text="Youtube: youtube.com/@vuthach8188", font = ("Comic Sans MS", 12))
youtube_label.place(x = 450, y = 490)

face_label = Label(window, text="Facebook: facebook.com/vuthach3001", font = ("Comic Sans MS", 12))
face_label.place(x = 450, y = 520)

github_label = Label(window, text="Github: github.com/Thachhcmute3001", font = ("Comic Sans MS", 12))
github_label.place(x = 450, y = 550)

# Create a label for displaying the predicted class
class_label = Label(window)
class_label.place(x = 300, y = 150)

#Create instruction lable
instruction_label = Label(window, text="", font=("Comic Sans MS", 13))
instruction_label.place(x=20, y=430)

window.mainloop()
