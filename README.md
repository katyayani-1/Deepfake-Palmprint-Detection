# Deepfake Palmprint Detector

A Flask web app to detect deepfake (AI-generated) palmprint images using a trained ResNet model.

## Features
- Stunning landing page and modern UI
- Upload palmprint images and get instant results
- Shows original/deepfake prediction and confidence
- Live image preview before upload

## Requirements
- Python 3.8+
- See `requirements.txt` for dependencies
- Pre-trained model file: `updated_resnet_model_best.h5` (must be in the project root)

## How to Run

1. **Clone or download this repository**
2. **Install dependencies**:
   ```in the terminal
   pip install -r requirements.txt
   ```
3.  Note: The trained model file `updated_resnet_model_best.h5` (178 MB) is not included in this repository due to GitHub file size limits.  
Please contact the author to obtain the file or use your own trained model.
4. **Run the Flask app**:
   ```in the terminal
   python app.py
   ```
5. **Open your browser** and go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Project Structure
```
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   ├── index.html
│   ├── upload.html
│   └── result.html
├── static/
│   └── uploads/
└── updated_resnet_model_best.h5
```

## Notes
- Uploaded images are saved in `static/uploads/`.
- For best results, use palmprint images similar to your training data.

---
If you have issues or questions, feel free to ask!
