## Blue Butterfly
Blue Butterfly is a project that utilizes the Stability AI API and Django REST Framework to generate images.
> Code
- To access the code, you can download or clone the repository from https://github.com/yogita-kaushish/text-to-image. This will give you access to the source code and project files.

> Configuration
- Before running the project, you need to configure it properly. Follow these steps:
  + Navigate to the blue_butterfly directory in your terminal or command prompt.
  + Update your Stability AI API Secret in the configuration file. This secret key is necessary for the 
      project to interact securely with the Stability AI service.

> Development
- To set up the development environment, make sure you have the required packages installed. You can install them using your preferred package manager. For example:
  <code>pip install -r requirements.txt</code>

> Redis Installation on Windows
  - Go to the Redis website and download the latest stable version of Redis for Windows.
  - Navigate to the directory where you extracted the Redis files.
  - Double-click on the <code>redis-server.exe</code> file to start the Redis server.
  - Open a command prompt and navigate to the same directory where the Redis files are located.
  - Run the command <code>redis-cli.exe ping</code>. If Redis is running successfully, you should see the response PONG.

> DB Migration - Optional
   - For bonus task db is created with two models Requests and Prompts.
   - Schema definitions can be found in /text-to-image/models.py.
   - To run the database migration execute the command <code>python manage.py makemigrations</code>
   - <code>python manage.py migrate</code>
   - Note: I have already committed the database it is optional to run db migrations.  

> Testing
   - Testing the application is essential to ensure its functionality. Follow these steps to test the application:
   - navigate to the project directory and run the command <code>python manage.py runserver</code>
   - Open the application in your web browser by navigating to http://localhost:8000. 
   - Once the application is open, click on the "New Prompt Request" button. 
   - Enter five prompts for image generation. 
   - Click the "Submit" button to send your prompts to the Stability AI service. 
   - Wait for the request to complete processing. You can monitor the progress within the application. 
   - Once processing is complete, view the generated images or results.

To review past requests and their prompt results, click on the request with its unique ID from the sidebar.