import cv2

def main():
    # Open a connection to the camera (0 is typically the default camera)
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open the camera.")
        return


    # Capture a single frame
    ret, frame = cap.read()

    # Check if the frame was captured successfully
    if not ret:
        print("Error: Failed to capture frame.")
        return

    # Display the frame in a window
    #cv2.imshow("Camera Feed", frame)

    # Get the default video frame width and height
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(frame_width)

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Use XVID codec
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (frame_width, frame_height))
    out.write(frame)

    # Break the loop when 'q' is pressed
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break

    # Release the camera and close any OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

