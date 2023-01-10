import numpy as np
import argparse
import os
import tensorflow as tf
import cv2
from util import label_map_util
from util import visualization_utils as vis_util
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' 


def classify(filepath):
    # path to the frozen graph:
    PATH_TO_FROZEN_GRAPH = 'inference_model/inference_graph.pb'
    
    # path to the label map
    PATH_TO_LABEL_MAP = 'inference_model/label.pbtxt'
    
    # number of classes 
    NUM_CLASSES = 8
    
    cap = cv2.VideoCapture(filepath)
    
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))   
    size = (frame_width, frame_height)

    #reads the frozen graph
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.compat.v1.GraphDef()
        with tf.compat.v2.io.gfile.GFile(PATH_TO_FROZEN_GRAPH, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')
    
    label_map = label_map_util.load_labelmap(PATH_TO_LABEL_MAP)
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
    category_index = label_map_util.create_category_index(categories)

    
    # Detection
    with detection_graph.as_default():
        with tf.compat.v1.Session(graph=detection_graph) as sess:
            while True:
                # Read frame from camera
                ret, image_np = cap.read()
                # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
                image_np_expanded = np.expand_dims(image_np, axis=0)
                # Extract image tensor
                image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
                # Extract detection boxes
                boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
                # Extract detection scores
                scores = detection_graph.get_tensor_by_name('detection_scores:0')
                # Extract detection classes
                classes = detection_graph.get_tensor_by_name('detection_classes:0')
                # Extract number of detections
                num_detections = detection_graph.get_tensor_by_name(
                    'num_detections:0')
                # Actual detection.
                (boxes, scores, classes, num_detections) = sess.run(
                    [boxes, scores, classes, num_detections],
                    feed_dict={image_tensor: image_np_expanded})
                # Visualization of the results of a detection.
                vis_util.visualize_boxes_and_labels_on_image_array(
                    image_np,
                    np.squeeze(boxes),
                    np.squeeze(classes).astype(np.int32),
                    np.squeeze(scores),
                    category_index,
                    use_normalized_coordinates=True,
                    line_thickness=10,
                    )
                # Display output
                cv2.imshow('Pothole Classification', cv2.resize(image_np, (1200, 700)))
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    break

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Pothole Classifier')
    parser.add_argument('--inputvideo', type=str, help='Path to the input video file')
    
    opt = parser.parse_args()
    
    if not opt.inputvideo:
        print('Please provide an input video using the --inputvideo parameter')
        quit()
    
    classify(opt.inputvideo)