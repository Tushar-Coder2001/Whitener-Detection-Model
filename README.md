# Whitener-Detection-Model
Our project deploys YOLOv3-based AI to detect correction pen fluid in images via a user-friendly Flask app, aiding precision in various industries.

## Steps to run the model on the test videos  
  
   ### 1. Clone the repository on the system:
   
        https://github.com/Tushar-Coder2001/Whitener-Detection-Model.git
        
   This might take sometime as in this repository there is some zip files that are larger in size. Once the repository is cloned, follow the next step.
   
   ### 2. Unzip all the zip files:
      
        unzip model_data.rar
        unzip dataset.rar
        unzip Whitener Detection Model.rar
        
   Once the zip files are unzipped, check that your folder structure should match with given folder structure.
   
          Whitener Detection Model
            | 
            |-> checkpoints -> contain additonal files inside it.
            |-> model_data -> contain additonal files inside it.
            |-> templates -> contain Front-End HTML files inside it.
            |-> static -> contain style file inside it.
            |-> dataset
                  |-> test -> contains xml and image files.
                  |-> train -> contains xml and image files.
            |-> tools -> contain additional files inside it.
            |-> yolov3 -> contain additional files inside it.
            |-> deepsort -> contain additional files inside it.
            |-> log -> contain additional files inside it.
            |-> detection_custom.py
            |-> requirements.txt
            |-> detection_demo.py
            |-> train.py
            |-> evaluate_mAP.py
            |-> object_tracker.py
            |-> collect_training_data.py
            |-> app.py -> user interface (flask server)
            
            
    
   If the folder structure matches, move to the following step.

   ### 3. Install the required libraries:
    
        pip install -r requirements.txt
                    or
        pip3 install -r requirements.txt
   
   ### 4. Run Flask Server.
  
          python app.py 
                    or       
          python3 app.py 
          
   ### 4. Now its time to detect the Whitener on the test Images given.
   Open a web browser and enter the IP address    
          localhost:5000
          
          
  
  The above python code might take sometime according to the specifications of the system.
        
        
