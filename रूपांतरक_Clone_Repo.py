

# @markdown

import base64
import subprocess
import time
import threading
import os
from IPython.display import display, HTML
import ipywidgets as widgets

# नमस्ते रुद्रमन्यव उतोत इषवेनमः |
gradient_button_css = """
<style>

.progress {
    width: 100%;
    height: 30px;
    background-color: #222222;
    border-radius: 15px;
    margin-bottom: 20px;
    overflow: hidden;
}
.progress-bar {
    border-radius: 20px;
    background-image: linear-gradient(to right, #FA8072, #D8D8B4);
}
.custom-accordion {
    width: 350px !important;
    margin: 10px auto !important;
    border-radius: 5px !important;
    background: linear-gradient(to right, #FA8072, #F5F5DC) !important;
    padding: 10px !important;
    z-index: 9999 !important;
}
.widget-container {
    border: none !important;
    background-color: #383838 !important; /* Background color changed */
    box-shadow: none !important;
    padding: 10px; /* Added padding */
    border-radius: 5px; /* Added border-radius */
}
.custom-accordion .custom-content {
    background-color: #F5F5DC !important;
    padding: 5px;
}
</style>
"""
# नमः प्रत्नय तॊषया गिरिश विप्रेषया ॥१॥
display(HTML(gradient_button_css))

# Function to generate the main repo URL
def generate_main_repo_url():
    main_repo_url = "https://github.com/nick-arch/Rupantarak.git"
    encoded_repo_url = base64.b64encode(main_repo_url.encode()).decode()
    return encoded_repo_url

# Function to display the gradient text logo
def display_logo():
    logo_html = """
    <div style='text-align: center;'><h1 style='font-family: Andika, sans-serif; font-size: 50px; background: -webkit-linear-gradient(left, #FA8072, #F5F5DC); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'><span style='color: #ff0066;'>र</span><span style='color: #ff6f00;'>ू</span><span style='color: #ffjd00;'>प</span><span style='color: #4caf50;'>ा</span><span style='color: #2196f3;'>ं</span><span style='color: #9c27b0;'>त</span><span style='color: #ff5722;'>र</span><span style='color: #FFC0CB;'>क</span> <span style='color: #2196f3; font-size: 22px;'>~ Rupantarak</span><br><span style='font-size: 18px;'>By Vishal Sharma</span><br><span style='color: #ff0066; font-size: 22px;'>ॐ नमः पार्वती पतये, हर-हर महादेव:</span></h1></div>
    """
    display(HTML(logo_html))

# Displaying the gradient text logo
display_logo()

# Progress bar
progress = widgets.IntProgress(value=0, min=0, max=3, step=1, description='Loading:')
display(progress)

# Downloading and installing रूपांतरक ~ Rupantarak
encoded_url = generate_main_repo_url()
progress.value += 1

# Executing git clone command using subprocess
subprocess.run(["git", "clone", base64.b64decode(encoded_url).decode()], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

progress.value += 1
os.chdir('/content/Rupantarak')
progress.value += 1

# Note 1
html_content_1 = '''
<div style="display: flex; justify-content: center; margin-top: 10px; margin-bottom: 10px;">
  <div style="width: 350px; margin: 10px 0;">
    <details id="details1">
      <summary id="summary1" style="border: none; border-radius: 8px; background: linear-gradient(to right, #FA8072, #F5F5DC); color: black; padding: 3px; text-align: center; cursor: pointer; list-style: none; font-weight: bold; margin-bottom: 10px;">
        <span id="arrow1">➼</span> <b>Must-Knows</b>
      </summary>
      <div style="border-radius: 8px; background-color: #333333; padding: 7px; color: white;">
        Hey there! Strap in for the GPU installation rodeo with our buddy रूपांतरक (Rupantarak). It's gonna be a wild 8-minute rollercoaster ride of tech wizardry. Grab some snacks, take a nap, or ponder life's mysteries while you wait. See you on the other side – hopefully with a shiny new GPU!
    </details>
  </div>
</div>
<script>
  var details1 = document.getElementById('details1');
  var arrow1 = document.getElementById('arrow1');
  details1.addEventListener('toggle', function(event) {
    if (details1.open) {
      arrow1.textContent = '➷';
    } else {
      arrow1.textContent = '➼';
    }
  });
</script>
'''

display(HTML(html_content_1))

import time
import threading
import os
from IPython.display import display, HTML
import ipywidgets as widgets

# स्थनुप्रभॊ विश्वभावः स्वयम्भू शम्भूवामनः |
total_duration = 600
# स भूमिं विश्वतो वर्त्त्या आत्मानं च जगत् स्थितं |
layout = widgets.Layout(width='90%', margin='0 auto 0 auto')
progress_bar = widgets.FloatProgress(
    value=0,
    min=0,
    max=100,
    layout=layout
)
# संभूतं च चराचरं तस्मै संभवाय नमः ॥६॥
display(progress_bar)


# सहस्रशीर्षा पुरुषः सहस्राक्षः सहस्रपात् ॥५॥
log_output = widgets.Output(layout={'border': '0px solid black', 'width': '100%', 'height': '300px', 'overflow_y': 'scroll'})
# यातुधान्वा गर्भिन्यॊऽधि कैतवानॊ अजायतः |
accordion = widgets.Accordion(children=[log_output])
accordion.set_title(0, 'Installation Logs')
accordion.selected_index = None
accordion.add_class("custom-accordion")
display(accordion)
# नमः प्रमथाधिपाया विश्वेश्वराय महादिव्याय |
def update_progress():
    for i in range(total_duration + 1):
        progress_bar.value = (i / total_duration) * 100
        time.sleep(1)
# नमः सहस्रकिर्त्ताय श्रवणाय महात्मने |
def run_installation():
    commands = [
        "pip install onnxruntime-gpu && pip install -r requirements.txt",
        "pip install onnxruntime-gpu --upgrade",
        "apt-get update --yes",
        "pip install gdown moviepy ipywidgets",
        "pip install pytube"
    ]
    with log_output:
        for command  in commands:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=True)
            for line in iter(process.stdout.readline, ''):
                print(line, end='')
            process.communicate()
# त्र्यक्षाय त्रिगुणात्मकाय त्रिपुरान्तकाय त्रिपुराय त्रिगुणायाथ नमः ॥१०॥
def start_processes():
    # नमः कालदीक्षिणाय नमः कलविकर्षणाय नमः कलायाय नमः कलात्मने |
    progress_thread = threading.Thread(target=update_progress)
    progress_thread.start()
    # नमः कलविचक्राय नमः कलप्रदाय नमः कलानाधाय नमो नमः ॥११॥
    run_installation()
    # त्र्यक्षाय त्रिगुणात्मकाय त्रिपुरान्तकाय त्रिपुराय त्रिगुणायाथ नमः ॥१०॥
    progress_thread.join()
# यातुधान्वा गर्भिन्यॊऽधि कैतवानॊ अजायतः |
start_processes()
# अशनाय पिपील्यानॊ अश्मनाभिर्व्याधिषू प्रभुः ॥७॥






import subprocess
import threading
import time
from IPython.display import display, HTML
import ipywidgets as widgets

def check_cuda_availability():
    try:
        import torch
        return torch.cuda.is_available()
    except ImportError:
        return False

def update_progress(progress_bar):
    total_duration = 100
    for i in range(total_duration + 1):
        progress_bar.value = (i / total_duration) * 100
        time.sleep(1)

def run_installation():
    if check_cuda_availability():
        display_heading()
        display_cuda_available_message()
        progress_bar = widgets.FloatProgress(
            value=0,
            min=0,
            max=100,
            layout=widgets.Layout(width='90%', margin='0 auto 0 auto')
        )
        display(progress_bar)
        progress_thread = threading.Thread(target=update_progress, args=(progress_bar,))
        progress_thread.start()

        commands = [
            "apt install nvidia-cuda-toolkit --yes",
            "pip install gdown",
        ]
        log_output = widgets.Output(layout={'border': '0px solid black', 'width': '100%', 'height': '300px', 'overflow_y': 'scroll'})
        accordion = widgets.Accordion(children=[log_output])
        accordion.set_title(0, 'Nvidia Cuda Toolkit Installation Logs')
        accordion.selected_index = None
        accordion.add_class("custom-accordion")
        display(accordion)
        
        with log_output:
            for command in commands:
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=True)
                for line in iter(process.stdout.readline, ''):
                    print(line, end='')
                process.communicate()
    else:
        display_cuda_not_available_message()

def display_heading():
    heading_html = """
    <style>
        .heading {
            text-align: center;
            font-weight: bold;
            font-size: 24px;
            margin-bottom: 20px;
        }
    </style>
    <div class="heading">
        GPU Acceleration Nvidia Cuda Toolkit Installation
    </div>
    """
    display(HTML(heading_html))

def display_cuda_available_message():
    available_html = """
    <style>
        .available-popup {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: #D4EDDA;
            border: 2px solid #28A745;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
        }
        .available-popup h2 {
            color: #28A745;
        }
        .available-popup p {
            color: #333333;
        }
    </style>
    <div id="available-popup" class="available-popup">
        <h2>CUDA toolkit is available for acceleration!</h2>
        <p>Proceeding with installation...</p>
    </div>
    <script>
        // Function to hide the popup after 2 seconds
        setTimeout(function() {
            var popup = document.getElementById('available-popup');
            popup.style.display = 'none';
        }, 2000);
    </script>
    """
    display(HTML(available_html))

def display_cuda_not_available_message():
    unavailable_html = """
    <style>
        .unavailable-popup {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: #F8D7DA;
            border: 2px solid #FFC107;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
        }
        .unavailable-popup h2 {
            color: #DC3545;
        }
        .unavailable-popup p {
            color: #333333;
        }
    </style>
    <div id="unavailable-popup" class="unavailable-popup">
        <h2>CUDA toolkit is not available for acceleration</h2>
        <p>The CUDA toolkit is not detected in this environment.</p>
        <p>Please make sure you are using a GPU-enabled runtime environment.</p>
    </div>
    <script>
        // Function to hide the popup after 2 seconds
        setTimeout(function() {
            var popup = document.getElementById('unavailable-popup');
            popup.style.display = 'none';
        }, 12000);
    </script>
    """
    display(HTML(unavailable_html))

run_installation()


# Step 1: Install the gdown library outside the function block
!pip install -q gdown

# Step 2: Import the necessary libraries
import gdown
import os
from IPython.display import clear_output

# Clear the output after installing
clear_output()

# Step 3: Create a function to download images
def download_image_from_gdrive(gdrive_url, save_path):
    """
    Download an image from Google Drive and save it to a specified path.

    Parameters:
    gdrive_url (str): The Google Drive URL of the file.
    save_path (str): The path where the file should be saved.
    """
    # Extract the file ID from the URL
    file_id = gdrive_url.split('/')[-2]
    download_url = f'https://drive.google.com/uc?id={file_id}'
    
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    # Download the file using gdown
    gdown.download(download_url, save_path, quiet=True)

# Step 4: Define the Google Drive URLs and save paths
gdrive_urls = [
    'https://drive.google.com/file/d/10z1_ukVfDNQxB96MmTs34VUAd5UkgA-u/view?usp=drivesdk',
    'https://drive.google.com/file/d/10w9Yu7yx6-klXubAkeb0BL1XwKPh2c-4/view?usp=drivesdk',
    'https://drive.google.com/file/d/10xIVD7CDWWZAeCzQQg2kFUBJXiFE9Um0/view?usp=drivesdk'
]

# Use Colab's file system path
save_paths = [
    '/content/Rupantarak/Rupantarak_Pro/Rupantarak_I/Rupantarak_B_0.png',
    '/content/Rupantarak/Rupantarak_Pro/Rupantarak_O/Rupantarak_Output.png',
    '/content/Rupantarak/Rupantarak_Pro/Rupantarak_I/Me.jpg',
]

# Step 5: Download the images
for url, path in zip(gdrive_urls, save_paths):
    download_image_from_gdrive(url, path)

# Clear the output to hide the download process
clear_output()

# Step 6: Verify that files were downloaded (if needed)
downloaded_files = os.listdir('/content')
