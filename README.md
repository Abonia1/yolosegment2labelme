# YOLO Predictions to Labelme and Anylabeling-Compatible JSON

<p align="center">
  <img alt="yolosegment2labelme" style="width: 128px; max-width: 100%; height: auto;" src="https://raw.githubusercontent.com/Abonia1/yolosegment2labelme/main/images/labelme_test/logo.png"/>
  <h1 align="center">🌟 yolosegment2labelme 🌟</h1>
  <p align="center">Convert your yolo model prediction results to json to view and edit in Labelme and Anylabeling. <b>YOLO Result to Json with single line cmd</b>!</p>
  <p align="center"><b>yolosegment2labelme = Easy Coversion + Predicted to Json  + Auto-labeling</b></p>
</p>

![](https://user-images.githubusercontent.com/18329471/234640541-a6a65fbc-d7a5-4ec3-9b65-55305b01a7aa.png)

[![PyPI](https://img.shields.io/pypi/v/yolosegment2labelme)](https://pypi.org/project/yolosegment2labelme/)
[![license](https://img.shields.io/github/license/abonia1/yolosegment2labelme.svg)](https://github.com/Abonia1/yolosegment2labelme/blob/main/LICENSE)
[![open issues](https://isitmaintained.com/badge/open/abonia1/yolosegment2labelme.svg)](https://github.com/abonia1/yolosegment2labelme/issues)
[![Website](https://img.shields.io/website?url=https%3A//abonia1.github.io&style=flat&logo=github&logoColor=white)](https://abonia1.github.io/)
[![Follow](https://img.shields.io/badge/+Follow-abonia-blue)](https://www.linkedin.com/in/aboniasojasingarayar/)
[![YouTube](https://img.shields.io/badge/-YouTube-red?style=flat-square&logo=youtube)](https://www.youtube.com/channel/UCGphGM_oeR4r9dqVs71Jc5w)
[![Medium](https://img.shields.io/badge/-Medium-black?style=flat-square&logo=medium)](https://medium.com/@abonia)
[![GitHub](https://img.shields.io/badge/-GitHub-black?style=flat-square&logo=github)](https://github.com/Abonia1)


> ⭐ Follow [AboniaSojasingarayar](https://www.linkedin.com/in/aboniasojasingarayar) for project updates.

**yolosegment2labelme** is a Python package that allows you to convert YOLO segmentation prediction results to LabelMe JSON format. This tool facilitates the annotation process by generating JSON files that are compatible with [Labelme](https://github.com/labelmeai/labelme) and [Anylabeling](https://github.com/vietanhdev/anylabeling) annotation tools.

## Features

- Convert YOLO segmentation prediction results to LabelMe JSON format.
- Compatible with various YOLO models.
- Easy-to-use command-line interface.
- Supports batch processing of images.
- Customizable confidence threshold for predictions.
- Highly customizable and extensible for specific use cases.

## Installation

You can install **yolosegment2labelme** via pip:

```bash
pip install yolosegment2labelme
```

## Usage

After installation, you can use the `yolosegment2labelme` command-line interface to convert YOLO segmentation prediction results to LabelMe JSON format. Here's a basic example:

```bash
yolosegment2labelme --images /path/to/images
```

or with custom yolo segmentation model

```bash
yolosegment2labelme --model yolov8n-seg.pt --images /path/to/images --conf 0.3
```

This command will process the images located in the specified directory (`/path/to/images`), using the YOLO model weights file `yolov8n-seg.pt` and here you can add path/to/your/customYOLOModel, and generate LabelMe JSON files with a confidence threshold of your choice and here it is of 0.3.


## Sample Output in Anylabeling Annotation Tool

Below are examples of image annotations created using yolosegment2labelme and viewed in the [Anylabeling](https://github.com/vietanhdev/anylabeling) annotation tool:

| Sample Image 1                                      | Sample Image 2                                      |
|-----------------------------------------------------|-----------------------------------------------------|
| ![Sample Image 1](https://raw.githubusercontent.com/Abonia1/yolosegment2labelme/main/images/labelme_test/sample1.png)      | ![Sample Image 2](https://raw.githubusercontent.com/Abonia1/yolosegment2labelme/main/images/labelme_test/sample2.png)      |
| Sample Annotation for Image 1                      | Sample Annotation for Image 2                      |

| Sample Image 3                                      | Sample Image 4                                      |
|-----------------------------------------------------|-----------------------------------------------------|
| ![Sample Image 3](https://raw.githubusercontent.com/Abonia1/yolosegment2labelme/main/images/labelme_test/sample3.png)      | ![Sample Image 4](https://raw.githubusercontent.com/Abonia1/yolosegment2labelme/main/images/labelme_test/sample4.png)      |
| Sample Annotation for Image 3                      | Sample Annotation for Image 4                      |


## Documentation

The documentation for **yolosegment2labelme** can be found on GitHub: [yolosegment2labelme Documentation](https://github.com/Abonia1/yolosegment2labelme)

## Contributing

#### If you like this work do star to this repo ⭐ and contribute...💁💁💁

---
Contributions are welcome! If you'd like to contribute to **yolosegment2labelme**, please check out the [Contribution Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors

- Abonia Sojasingarayar - [GitHub](https://github.com/Abonia1)

## Support

If you encounter any issues or have questions about **yolosegment2labelme**, please feel free to open an issue on GitHub: [yolosegment2labelme Issues](https://github.com/Abonia1/yolosegment2labelme/issues)