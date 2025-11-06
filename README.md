
DS5216 Programming Assignment 02

First, I selected five badminton videos from the official Badminton World Federation TikTok page. Then, I converted each video into frames and carefully selected 15 high-quality, non-blurry images from each one. These images were then annotated using Roboflow to create a labeled dataset.

Google Drive setup and imports: The code first mounts Google Drive to allow Colab to access files stored there. It then imports all necessary libraries — OpenCV for video processing, PyTorch and torchvision for deep-learning tasks, NumPy for handling arrays, os for file management, and later, the Ultralytics YOLO library for training and inference using YOLOv8. These imports prepare the environment for both video processing and model execution.

Device selection and model loading: The script checks whether a GPU is available and uses it (via CUDA) if possible; otherwise, it defaults to the CPU. It then loads a pretrained Keypoint R-CNN model (keypointrcnn_resnet50_fpn) from torchvision and switches it to evaluation mode (model.eval()), ensuring that no weight updates occur during inference.

Skeleton definition: A predefined list of joint index pairs, called SKELETON_CONNECTIONS, defines which detected keypoints should be connected to form the human skeleton (e.g., shoulder–elbow, elbow–wrist). This mapping matches the keypoint ordering used by the Keypoint R-CNN model and is used for drawing skeletal lines between detected joints.

Drawing function: The draw_skeleton_on_frame function receives each video frame and an array of detected keypoints for one or more persons. It draws small red circles at each detected joint and green lines between joints defined in the skeleton list, provided both keypoints are valid. The function returns the frame with all the visualized skeletons.

Input/output folder setup: The script defines an input folder for original videos and an output folder for saving processed results, ensuring the output folder exists before starting. This keeps file organization consistent and makes it easy to find results in Google Drive.

Processing videos: The code loops through the five video files (named 1.mp4 to 5.mp4). For each video, it verifies the path, opens the video using OpenCV, and sets up a VideoWriter to save the processed output using the same resolution and MP4 codec.

Pose inference (frame-by-frame): Each video is read frame by frame. Every frame is converted from BGR to RGB, normalized to the range [0,1], and converted into a PyTorch tensor with the correct dimensions. The model then performs inference in torch.no_grad() mode to avoid gradient calculations. Detected persons with confidence scores above 0.9 are retained for accurate keypoint visualization.

Drawing and saving: The filtered keypoints are drawn on the frame using the drawing function, and the annotated frame is written to the output video file. This process repeats until all frames are processed.

Releasing resources: After completing each video, the script releases both the VideoCapture and VideoWriter objects, prints the total number of frames processed, and indicates where the output was saved.

Training YOLOv8: After pose detection, the script trains a custom object detection model using Ultralytics YOLOv8. It loads a pretrained yolov8n.pt model and starts training with a dataset configuration file (YAML) stored in Google Drive. The training runs for 30 epochs with an image size of 640, saving all results (weights and logs) in a project folder within Drive.

Loading trained weights: Once training completes, the script checks for the file best.pt under the weights directory. If it exists, it loads the trained model for inference; otherwise, it raises an error.

Running YOLOv8 predictions: The trained model is then used to make predictions on the test videos. The script saves annotated videos with bounding boxes, confidence scores, and class labels to a dedicated output folder. Progress messages are printed for each video processed.

Final outputs and purpose: In the end, the project produces two key outputs — skeleton-annotated videos from the Keypoint R-CNN model and detection results from the YOLOv8 model. Together, these enable detailed player detection and pose analysis, which are valuable for applications such as sports analytics, performance tracking, and motion behavior analysis in badminton.

<img width="369" height="626" alt="Capture1" src="https://github.com/user-attachments/assets/10d07808-4c57-4301-aae4-e29461e6e60b" />
<img width="369" height="530" alt="Capture" src="https://github.com/user-attachments/assets/41d081dc-9251-492f-b3a5-56c852d81dba" />
