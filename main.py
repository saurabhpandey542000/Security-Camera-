# Import the Pip OpenCV (cv2) Package in the System for using the Better Feature of a Computer Vission Porogram..
import cv2
# THe WinSound is the package in which for Make n Noice --
import winsound

# Define a Variable for our Project that can Capture(Shoot) the Vedio or us-------
cam = cv2.VideoCapture(0)

# Here we applied an Condition that when our Camera is open --> then it can Read it..
# "Retrive" the Image that the Cam is 'read' in the Form of the "Frame" of the vedio format;

# When the Camera is turn Open ---> then it can Retrive the image that it will Read and Show up in the Frame
while cam.isOpened():
    retrive, frame1 = cam.read()

    # We Use Second Frame because we have to Compare the  first(initial) frame to second(current) frame by the "Substracting these two frame ...
    retrive, frame2 = cam.read()

    # This is the Absolute Difference between Frame(1) from Frame (2)
    diff = cv2.absdiff(frame1, frame2)

    # We use the gray color because -- In Camera when we are movement then it Shows colorfull images but we want  to Convert it into 1 Color --
    # It Convert the the Basic Color (Red , Blue , Green) into Grey Color--
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)

    # Now here , We Can Blur the Grey Image that we have to Shown in the Image After the Run --->

    # In argument , we Can the pass the Privious formatted image that you want to Convert , and Kernal Size (5,5)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    #  Now ,We can add an Thresh hold --> ("THresh hold is the way which cN remove the unwanted noice from the Camera")
    # In the Arguments , we can pass the Privious Formated images ,Thresh hold Value , and Max Value type -->
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    # Dilation is the Just opposite the Threshhold , After Removing the Unwanted things , we can Collect the Wanted things ,which can Improve it--
    # In argument Value , if you wants to add kernal size ,then is ok otherwise Pass (none) and Set How Many Iteration it will Pass
    dilated = cv2.dilate(thresh, None, iterations=3)

    # Contours is the Boundary of the Item or the Objects that is Moving in the Camera --that's why you are Visually seeing what is the Things is Moving nad What is Statics----->
    # In the Arguments , We Can Pass the [Src(privious Images) , declare the tyoe of the Mode , Methods]
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Now After Appling the Contours , we an Draw (print) the Contours
    # In Arguments , We Pass the Images(SRC) , the Contours (which is Also in the Form of Variable ) , Index value, Color (Green Color ) , thickness of the Contours (2)-->

    # cv2.drawContours(frame1 ,contours ,-1 ,(0 ,255 ,0) ,2)

    # Until now , Computer Visions can Detect even Every Small Movements , But If i Can see every Small Objects contours then we canot Focus on tthe Big Person (Theif) --

    # So we Can Set the Contours  into the Limits ,that It Shows the Contours of those thing whose Value is bigger than the Given Conditions -->

    for c in contours:
        if cv2.contourArea(c) <6000:
            continue

        # Here we can Define the Four Variable for the contours that can defines the X - Axis , Y -Axis , Wridth , and Height  of the Contours
        x, y, w, h = cv2.boundingRect(c)

        # Here CV2 can make a Rectangle frame for Contours  (for 3D axis like X axis ,Y axis , x+w axis , y+h axis , {Greencolor Contours} , Index Value [Border] )
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

        winsound.Beep(5000, 300)
    if cv2.waitKey(5) == ord('q'):
        break

    cv2.imshow("Security Camera", frame1)
