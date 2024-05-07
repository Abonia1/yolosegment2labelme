import argparse
from .polygon_saver import PolygonSaver
from ultralytics import YOLO

def main():
    parser = argparse.ArgumentParser(description='Convert YOLO results to JSON files.')
    parser.add_argument('--model', default='yolov8n-seg.pt', help='Path to YOLO model weights file (default is yolov8n)')
    parser.add_argument('--images', required=True, help='Path to folder containing images')
    parser.add_argument('--conf', type=float, default=0.2, help='Confidence threshold')
    args = parser.parse_args()

    # Use the input images directory as the output directory for JSON files
    output_dir = args.images

    # Instantiate the PolygonSaver class
    polygon_saver = PolygonSaver()

    # Load the YOLO model
    yolo_model = YOLO(args.model)

    # Get results from YOLO model predictions
    results = yolo_model.predict(args.images, save=True, conf=args.conf)

    # Generate JSON files with results
    polygon_saver.generate_json_with_results(results, output_dir)

if __name__ == "__main__":
    main()
