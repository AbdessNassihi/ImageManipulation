import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import matplotlib.pylab as plt
import numpy as np
# libraries

root = tk.Tk()
root.geometry("1200x700")  # Size of the window 
root.title('Image manipulation')
root.resizable(False, False)
root.config(background = '#811ef8') # sets background color to purple with hexadecimal code
# window configuration

gamma =1 # value of gamma for the gamma manipulator

def ClearRoot(): # removes all elemets from the root
    for widget in root.winfo_children():
        widget.destroy()
        
def HomeScreen(): # first screen shown
    ClearRoot() 
    label_title = tk.Label(root,text="Choose image to manipulate", font = ("Courrier",35),
                      bg = '#811ef8',fg = 'white')
    label_title.place(x=320,y=250) # position of the label
    
    UploadBtn = tk.Button(root, text='Upload image',font = ("Courrier",25),bg = 'white',
                      fg = '#811ef8',command = lambda:SelectImage())
    UploadBtn.place(relx =0.5,rely=0.5,anchor='center')  # position of the button
    
    # adds the necessary buttons and lables
    
def SecondScreen(): # screen after chosing the image
    ClearRoot()
    OtherImageBtn = tk.Button(root, text='<< Choose other image',font = ("Courrier",25),bg = 'white',
                      fg = '#811ef8',command = lambda : HomeScreen())
    
    SaveImageBtn = tk.Button(root, text='Save manipulated image >>',font = ("Courrier",25),bg = 'white',
                      fg = '#811ef8',command = lambda :SaveManipulatedImage())
    
    ResetBtn = tk.Button(root, text='Reset changes',font = ("Courrier",25),bg = 'white',
                      fg = '#811ef8',command = lambda :ShowImage())
    ResetBtn.place(x = 900,y= 500)
    OtherImageBtn.place(anchor='nw')
    SaveImageBtn.place(x = 780,y=0)
    # posistion of the buttons
    
    lbl = tk.Label(text = "Select modification feature",font = ("Courrier",20,'bold'),bg = '#811ef8',fg = 'white')
    lbl.place(x = 400,y=120)
    CreateCombobox()  # add combobox
    
def SelectImage(): # function for letting the user to choose his image from the disk
    
    global path
    f_types = [('PNG Files', '*.png'),('Jpg Files','*.jpg')] # files types
    path = filedialog.askopenfilename(filetypes=f_types) # access image from disk and returns the pad
    ShowImage() 
    
def ShowImage(): # displays the images on the screen
    
    global path
    global img
    global data
    global NewRGB
    global ManipulatedImage
    global ManipulatedImg
    # global variables
    
    img = Image.open(path)
    data = plt.imread(path)  # converts the image into a numpy array
    NewRGB = data.copy() # new image for the rgb manipulator
    img = ResizeImage(img) # resizes image to fit well in the root
    img = ImageTk.PhotoImage(img) # transforms image to PhotoImage
    ManipulatedImg = img 
    
    SecondScreen() 
    
    OriginalImage =tk.Label(root,image=img,text = 'Original image',font = ("Courrier",25,'bold'),
                            compound='bottom',bg ='#811ef8',fg = 'white')
    ManipulatedImage = tk.Label(root,image=ManipulatedImg,text = 'Manipulated image',font = ("Courrier",25,'bold'),
                                compound='bottom',bg ='#811ef8',fg = 'white')
    OriginalImage.place(x=80,y=150)
    ManipulatedImage.place(x=850,y=150)
    # display the images by putting it in a label
def SelectedCombo():
    global ManipulatedImage
    global ManipulatedImg
    global img
    global data
    
    SecondScreen() 
    
    OriginalImage =tk.Label(root,image=img,text = 'Original image',font = ("Courrier",25,'bold'),
                            compound='bottom',bg ='#811ef8',fg = 'white')
    ManipulatedImage = tk.Label(root,image=ManipulatedImg,text = 'Manipulated image',font = ("Courrier",25,'bold'),
                                compound='bottom',bg ='#811ef8',fg = 'white')
    OriginalImage.place(x=80,y=150)
    ShowManipulatedImage(data)
    

def ResizeImage(im): # function to resize the image
    maxHeight=200
    maxWidth = 200
    width, height = im.size
    if width > maxWidth or height > maxHeight:
         img_resized = im.resize((int(width/3),int(height/3)))
    else:
        img_resized = im.resize((width*2,height*2))
    return img_resized

def CreateCombobox(): # functon to create a combobox
    
    global selected_feature
    selected_feature = tk.StringVar()
    feature_cb = ttk.Combobox(root,textvariable=selected_feature,width = 30,font = ("Courrier",15,'bold') )
    feature_cb['values'] = ['Modify RGB and gamma value','Modify the shape','Add filter']
    feature_cb['state'] = 'readonly'
    feature_cb.place(x=400,y=180)
    feature_cb.bind('<<ComboboxSelected>>',Manipulate)

def Manipulate(event): # shows manipulate features
    if selected_feature.get() == 'Modify RGB and gamma value': 
        SelectedCombo()
        RGBandGammaModificationScreen()
        
    elif selected_feature.get() == 'Modify the shape':
        SelectedCombo()
        ShapeModificationScreen()
        
    elif selected_feature.get() == 'Add filter':
        SelectedCombo()
        AddFilterScreen()
     # controls what the user selected and executes the right function   
        
def RGBandGammaModificationScreen(): 
  
    RValueLbl = tk.Label(root,text = 'Red:',font = ("Courrier",20,'bold'),
                             bg ='#811ef8',fg = 'white')
    RValueLbl.place(x = 410, y = 230)
    
    RValuePlusBtn = tk.Button(root, text='+',font = ("Courrier",10),bg = 'white',
                      fg = '#811ef8',width = 2,command = lambda:ModifyRGB(0,"+"))
    RValuePlusBtn.place(x = 550,y= 230)
    
    RValueMinBtn = tk.Button(root, text='-',font = ("Courrier",10),bg = 'white',
                      fg = '#811ef8',width = 2,command = lambda:ModifyRGB(0,"-"))
    RValueMinBtn.place(x = 600,y= 230)
    
    GValueLbl = tk.Label(root,text = 'Green:',font = ("Courrier",20,'bold'),
                             bg ='#811ef8',fg = 'white')
    GValueLbl.place(x = 410, y = 280)
    
    GValuePlusBtn = tk.Button(root, text='+',font = ("Courrier",10),bg = 'white',
                      fg = '#811ef8',width = 2,command = lambda:ModifyRGB(1,"+"))
    GValuePlusBtn.place(x = 550,y= 280)
    
    GValueMinBtn = tk.Button(root, text='-',font = ("Courrier",10),bg = 'white',
                      fg = '#811ef8',width = 2,command = lambda:ModifyRGB(1,"-"))
    GValueMinBtn.place(x = 600,y= 280)
    
    BValueLbl = tk.Label(root,text = 'Blue:',font = ("Courrier",20,'bold'),
                             bg ='#811ef8',fg = 'white')
    BValueLbl.place(x = 410, y = 330)
    
    BValuePlusBtn = tk.Button(root, text='+',font = ("Courrier",10),bg = 'white',
                      fg = '#811ef8',width = 2,command = lambda:ModifyRGB(2,"+"))
    BValuePlusBtn.place(x = 550,y= 330)
    
    BValueMinBtn = tk.Button(root, text='-',font = ("Courrier",10),bg = 'white',
                      fg = '#811ef8',width = 2,command = lambda:ModifyRGB(2,"-"))
    BValueMinBtn.place(x = 600,y= 330)
    
    GammaValueLbl = tk.Label(root,text = 'Gamma:',font = ("Courrier",20,'bold'),
                             bg ='#811ef8',fg = 'white')
    GammaValueLbl.place(x = 410, y = 400)
    
    GammaValuePlusBtn = tk.Button(root, text='+',font = ("Courrier",10),bg = 'white',
                      fg = '#811ef8',width = 2,command = lambda:ModifyRGB(3,"++"))
    GammaValuePlusBtn.place(x = 550,y= 405)
    
    GammaValueMinBtn = tk.Button(root, text='-',font = ("Courrier",10),bg = 'white',
                      fg = '#811ef8',width = 2,command = lambda:ModifyRGB(3,"--"))
    GammaValueMinBtn.place(x = 600,y= 405) 
    
    # adds the necessary buttons and lables for RGB manipulation feature
    
    
    
def ShapeModificationScreen():
    
    CropLbl = tk.Label(root,text = 'How much to cut:',font = ("Courrier",20,'bold'),
                             bg ='#811ef8',fg = 'white')
    CropLbl.place(x = 410, y = 230)
    
    LeftSideLbl = tk.Label(root,text = 'Left Side:',font = ("Courrier",15,'bold'),
                             bg ='#811ef8',fg = 'white')
    LeftSideLbl.place(x = 430, y = 280)
    
    LeftValue = tk.StringVar()
    LeftEntered = ttk.Entry(root,width=4, textvariable=LeftValue)
    LeftEntered.place(x=600,y=283)
    
    RightSideLbl = tk.Label(root,text = 'Right Side:',font = ("Courrier",15,'bold'),
                             bg ='#811ef8',fg = 'white')
    RightSideLbl.place(x = 430, y = 310)
    
    RightValue = tk.StringVar()
    RightEntered = ttk.Entry(root,width=4, textvariable=RightValue)
    RightEntered.place(x=600,y=314)
    
    TopSideLbl = tk.Label(root,text = 'Top Side:',font = ("Courrier",15,'bold'),
                             bg ='#811ef8',fg = 'white')
    TopSideLbl.place(x = 430, y = 340)
    
    TopValue = tk.StringVar()
    TopEntered = ttk.Entry(root,width=4, textvariable=TopValue)
    TopEntered.place(x=600,y=345)
    
    
    BottomSideLbl = tk.Label(root,text = 'Bottom Side:',font = ("Courrier",15,'bold'),
                             bg ='#811ef8',fg = 'white')
    BottomSideLbl.place(x = 430, y = 370)
    
    BottomValue = tk.StringVar()
    BottomEntered = ttk.Entry(root,width=4, textvariable=BottomValue)
    BottomEntered.place(x=600,y=376)
    
    CropBtn = tk.Button(root, text='Crop image',font = ("Courrier",20),bg = 'white',
                      fg = '#811ef8',width = 10,command = lambda : CropImage(int(LeftValue.get()), int(RightValue.get()),
                                                                              int(TopValue.get()), int(BottomValue.get())))                                                                      
    CropBtn.place(x = 430,y= 410 )
    
    MirrorHBtn = tk.Button(root, text='Mirror horizontally',font = ("Courrier",20),bg = 'white',
                      fg = '#811ef8',width = 15,command = lambda : MirrorImage(0))                                                                      
    MirrorHBtn.place(x = 430,y= 480 )
    
    MirrorVBtn = tk.Button(root, text='Mirror Vertically',font = ("Courrier",20),bg = 'white',
                      fg = '#811ef8',width = 15,command = lambda : MirrorImage(1))                                                                      
    MirrorVBtn.place(x = 430,y= 550 )
    
    # adds the necessary buttons and lables for the shape modificator feature
    
    
def AddFilterScreen():
  
    SepiaFilterBtn = tk.Button(root, text='Sepia filter',font = ("Courrier",25),bg = 'white',
                      fg = '#811ef8',width = 15,command = lambda:SepiaFilter(data))
    SepiaFilterBtn.place(x = 450,y= 250)
        
    EdgeDetectionEffectBtn =  tk.Button(root, text='Edge detection',font = ("Courrier",25),bg = 'white',
                      fg = '#811ef8',width = 15,command = lambda:ConvolveImage(data,[[-1,-1,-1], [-1,8,-1], [-1,-1,-1]]))
    EdgeDetectionEffectBtn.place(x = 450,y= 320)
    
    BlurEffectBtn =  tk.Button(root, text='Blur effect',font = ("Courrier",25),bg = 'white',
                      fg = '#811ef8',width = 15,command = lambda:ConvolveImage(data,[[1/9.0,1/9.0,1/9.0], [1/9.0,1/9.0,1/9.0], [1/9.0,1/9.0,1/9.0]]))
    BlurEffectBtn.place(x = 450,y= 390)
    
    BlurEffectBtn =  tk.Button(root, text='Sharpen effect',font = ("Courrier",25),bg = 'white',
                      fg = '#811ef8',width = 15,command = lambda:ConvolveImage(data,[[0,-1,0], [-1,5,-1], [0,-1,0]]))
    BlurEffectBtn.place(x = 450,y= 460)
        
        
    PixelationFilterBtn = tk.Button(root, text='Pixelation filter',font = ("Courrier",25),bg = 'white',
                      fg = '#811ef8',width = 15,command = lambda:PixelationFilter(data,int(PixelSize.get())))
    PixelationFilterBtn.place(x = 450,y= 600)
    
    GrayscaleFilterBtn = tk.Button(root, text='Grayscale filter',font = ("Courrier",25),bg = 'white',
                      fg = '#811ef8',width = 15,command = lambda:Grayscale(data))
    GrayscaleFilterBtn.place(x = 450,y= 530)
    
    PixelSizeLbl = tk.Label(root,text = 'Insert pixel size for pixelation',font = ("Courrier",15),
                             bg ='#811ef8',fg = 'white')
    PixelSizeLbl.place(x = 750, y = 640)
        
    PixelSize = tk.StringVar()
    PixelEntered = ttk.Entry(root,width=5, textvariable=PixelSize)
    PixelEntered.place(x=1010,y=645)
    
    # adds the necessary buttons and lables for the filter feature
    
def ConvolveImage(pic,kernel): # function for the covolution feature
    global output
    
    if kernel == [[-1,-1,-1], [-1,8,-1], [-1,-1,-1]]:
        pic[:] = (np.max(pic,axis=-1,keepdims=1) + np.min(pic,axis=-1,keepdims=1)) /2 # converts the image into grayscale if the edge detection filter was selected 
        
    output = pic.copy()
    row,col = (pic.shape[0],pic.shape[1])
    img2 = np.zeros((row+2,col+2,3))
    img2[1:-1,1:-1] = pic[:]
    # creates new image that is like the original image but with a blank border of pixels
    xkernel,ykernel = (len(kernel),len(kernel[0]))
    for i in range (0,row-1):
        for j in range (0,col-1):
            R = np.sum(kernel*img2[i:i+xkernel,j:j+ykernel,0]) 
            G = np.sum(kernel*img2[i:i+xkernel,j:j+ykernel,1]) 
            B = np.sum(kernel*img2[i:i+xkernel,j:j+ykernel,2]) 
            output[i+1,j+1] = [R,G,B]
    
    # multiplies each corresponding pixels and takes the sum of it
    output[output>1] = 1
    output[output<0] = 0
    # limiting the pixels values between 0 and 1
    ShowManipulatedImage(output) # function that displays the manipulated image
    
def Grayscale(pic): # function for turning the image into grayscale
     grayscale = pic.copy()
     grayscale[:] = (np.max(grayscale,axis=-1,keepdims=1) + np.min(grayscale,axis=-1,keepdims=1)) /2 # takes the average of nearby pixels
     ShowManipulatedImage(grayscale) # function that displays the manipulated image
    
def ModifyRGB(color,sign): # function for the RGB manipulation
    global NewImage
    global gamma
    #global variables
    
    if sign == "+":
        NewRGB[:,:,color] = NewRGB[:,:,color] +(10/255.0)
        NewRGB[NewRGB > 1] = 1
        result = NewRGB.copy()
         # increases the given color value by 10
    elif sign == "-":
         NewRGB[:,:,color] =  NewRGB[:,:,color] -(10/255.0)
         NewRGB[NewRGB < 0] = 0
         result = NewRGB.copy()
         # decreases the given color value by 10
         
    elif sign == "++":
        gamma +=0.1
        result = np.copy(NewRGB)**(1/gamma)
        # increases the gamma value by 0.1
    elif sign == "--":
        gamma -=0.1
        result = np.copy(NewRGB)**(1/gamma)
        # decreases the gamma value by 0.1
    
    ShowManipulatedImage(result) # displays the manipulated image
    
    
    
def CropImage(left,right,top,bottom): # function for cropping the image
    
    if (right == 0  and bottom ==0):
        CroppedImg = data[top:,left:]
    elif bottom == 0:
        CroppedImg = data[top:,left:-right]
    elif right == 0:
        CroppedImg = data[top:-bottom,left:]
    else:
        CroppedImg = data[top:-bottom,left:-right]
     # cropping the image
    
    ShowManipulatedImage(CroppedImg)# displays the manipulated image
    
    
def MirrorImage(axis): # function for mirroring the image

    if axis == 0 :
        MirroredImg = data[::-1,:,:] # mirrors horizontally
    else:
        MirroredImg = data[:,::-1,:] # mirrors vertically
        
    ShowManipulatedImage(MirroredImg)# displays the manipulated image
    
def SepiaFilter(pic): # function for the sepia filter

    
    rows, cols, k = pic.shape # stores the shape of the image
   
    
    Sepia_Filter = pic.copy()
    newR = 0.393*pic[:,:,0] + 0.769*pic[:,:,1] + 0.189*pic[:,:,2]
    newG = 0.349*pic[:,:,0] + 0.686*pic[:,:,1] + 0.168*pic[:,:,2]
    newB = 0.272*pic[:,:,0] + 0.534*pic[:,:,1] + 0.131*pic[:,:,2]
    # calculates the new RGB values with the sepia formula
    
    for i in range(rows -1):
        for j in range(cols -1):
            colors = [newR[i][j],newG[i][j],newB[i][j]]
            Sepia_Filter[i][j] = colors
    # applying the new RGB value to the image
    
    Sepia_Filter[Sepia_Filter > 1] = 1  # keep RGB values between 0 and 1
    
    
    ShowManipulatedImage(Sepia_Filter) # displays the manipulated image
    
def PixelationFilter(pic,k): # function for pixelating the image
  
    rows,cols = (pic.shape[0],pic.shape[1])
    rows, cols = rows - rows % k, cols - cols % k
    PixelatedImg = np.zeros((rows, cols, 3))
    for x in range(0, rows, k):
        for y in range(0, cols, k):
            PixelatedImg[x:x+k,y:y+k] = pic[x:x+k,y:y+k].mean(axis=(0,1))

    ShowManipulatedImage(PixelatedImg)  # displays the manipulated image
    

def ShowManipulatedImage(arr): # function for displaying the manipulated image 
    global ManipulatedImage
    global ManImg
    global ManImage
    global data
    global NewRGB
    global ManipulatedImg
    global img
    # global variables
    
    
    
    data = arr
    NewRGB = arr
    
    ManImg = Image.fromarray((arr * 255).astype(np.uint8))
    ManImage = ResizeImage(ManImg)
    ManImage = ImageTk.PhotoImage(ManImage)
    ManipulatedImage.destroy()
    
    ManipulatedImage = tk.Label(root,image=ManImage,text = 'Manipulated image',font = ("Courrier",25,'bold'),
                                compound='bottom',bg ='#811ef8',fg = 'white')
    ManipulatedImage.place(x=850,y=150)
    # add label to the root
    
def SaveManipulatedImage():
   ManImg.save('ManipulatedImage.png') # Saves manipulated image to disk
   messagebox.showinfo('information','Image succesfully saved!')

    
    
HomeScreen()
root.mainloop()  # Keep the window open