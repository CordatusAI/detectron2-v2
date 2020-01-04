import ipywidgets as widgets

def get_model(model_name):
    model_dict = {'fast_rcnn_R_50_FPN_1x':'detectron2://COCO-Detection/fast_rcnn_R_50_FPN_1x/137635226/model_final_e5f7ce.pkl',
              'faster_rcnn_R_101_C4_3x':'detectron2://COCO-Detection/faster_rcnn_R_101_C4_3x/138204752/model_final_298dad.pkl',
              'faster_rcnn_R_101_DC5_3x':'detectron2://COCO-Detection/faster_rcnn_R_50_DC5_3x/137849425/model_final_68d202.pkl',
              'faster_rcnn_R_101_FPN_3x':'detectron2://COCO-Detection/faster_rcnn_R_101_FPN_3x/137851257/model_final_f6e8b1.pkl',
              'faster_rcnn_R_50_C4_1x':'detectron2://COCO-Detection/faster_rcnn_R_50_C4_1x/137257644/model_final_721ade.pkl',
              'faster_rcnn_R_50_C4_3x':'detectron2://COCO-Detection/faster_rcnn_R_50_C4_3x/137849393/model_final_f97cb7.pkl',
              'faster_rcnn_R_50_DC5_1x':'detectron2://COCO-Detection/faster_rcnn_R_50_DC5_1x/137847829/model_final_51d356.pkl',
              'faster_rcnn_R_50_DC5_3x':'detectron2://COCO-Detection/faster_rcnn_R_50_DC5_3x/137849425/model_final_68d202.pkl',
              'faster_rcnn_R_50_FPN_1x':'detectron2://COCO-Detection/faster_rcnn_R_50_FPN_1x/137257794/model_final_b275ba.pkl',
              'faster_rcnn_R_50_FPN_3x':'detectron2://COCO-Detection/faster_rcnn_R_50_FPN_3x/137849458/model_final_280758.pkl',
              'faster_rcnn_X_101_32x8d_FPN_3x':'detectron2://COCO-Detection/faster_rcnn_X_101_32x8d_FPN_3x/139173657/model_final_68b088.pkl',
              'retinanet_R_101_FPN_3x':'detectron2://COCO-Detection/retinanet_R_101_FPN_3x/138363263/model_final_59f53c.pkl',
              'retinanet_R_50_FPN_1x':'detectron2://COCO-Detection/retinanet_R_50_FPN_1x/137593951/model_final_b796dc.pkl',
              'retinanet_R_50_FPN_3x':'detectron2://COCO-Detection/retinanet_R_50_FPN_3x/137849486/model_final_4cafe0.pkl',
              'rpn_R_50_C4_1x':'detectron2://COCO-Detection/rpn_R_50_C4_1x/137258005/model_final_450694.pkl',
              'rpn_R_50_FPN_1x':'detectron2://COCO-Detection/rpn_R_50_FPN_1x/137258492/model_final_02ce48.pkl',
              'mask_rcnn_R_101_C4_3x':'detectron2://COCO-InstanceSegmentation/mask_rcnn_R_101_C4_3x/138363239/model_final_a2914c.pkl',
              'mask_rcnn_R_101_DC5_3x':'detectron2://COCO-InstanceSegmentation/mask_rcnn_R_101_DC5_3x/138363294/model_final_0464b7.pkl',
              'mask_rcnn_R_101_FPN_3x':'detectron2://COCO-InstanceSegmentation/mask_rcnn_R_101_FPN_3x/138205316/model_final_a3ec72.pkl',
              'mask_rcnn_R_50_C4_1x':'detectron2://COCO-InstanceSegmentation/mask_rcnn_R_50_C4_1x/137259246/model_final_9243eb.pkl',
              'mask_rcnn_R_50_DC5_3x':'detectron2://COCO-InstanceSegmentation/mask_rcnn_R_50_DC5_3x/137849551/model_final_84107b.pkl',
              'mask_rcnn_R_50_FPN_1x':'detectron2://COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_1x/137260431/model_final_a54504.pkl',
              'mask_rcnn_R_50_FPN_3x':'detectron2://COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x/137849600/model_final_f10217.pkl',
              'mask_rcnn_X_101_32x8d_FPN_3x':'detectron2://COCO-InstanceSegmentation/mask_rcnn_X_101_32x8d_FPN_3x/139653917/model_final_2d9806.pkl',
              'keypoint_rcnn_R_101_FPN_3x':'detectron2://COCO-Keypoints/keypoint_rcnn_R_101_FPN_3x/138363331/model_final_997cc7.pkl',
              'keypoint_rcnn_R_50_FPN_1x':'detectron2://COCO-Keypoints/keypoint_rcnn_R_50_FPN_1x/137261548/model_final_04e291.pkl',
              'keypoint_rcnn_R_50_FPN_3x':'detectron2://COCO-Keypoints/keypoint_rcnn_R_50_FPN_3x/137849621/model_final_a6e10b.pkl',
              'keypoint_rcnn_X_101_32x8d_FPN_3x':'detectron2://COCO-Keypoints/keypoint_rcnn_X_101_32x8d_FPN_3x/139686956/model_final_5ad38f.pkl',
              'panoptic_fpn_R_101_3x':'detectron2://COCO-PanopticSegmentation/panoptic_fpn_R_101_3x/139514519/model_final_cafdb1.pkl',
              'panoptic_fpn_R_50_1x':'detectron2://COCO-PanopticSegmentation/panoptic_fpn_R_50_1x/139514544/model_final_dbfeb4.pkl',
              'panoptic_fpn_R_50_3x':'detectron2://COCO-PanopticSegmentation/panoptic_fpn_R_50_3x/139514569/model_final_c10459.pkl'}
    
    return model_dict[model_name]

def get_xavier_od_widget():
    od = widgets.Dropdown(
        options=['fast_rcnn_R_50_FPN_1x', 'faster_rcnn_R_101_C4_3x',
                 'faster_rcnn_R_101_DC5_3x', 'faster_rcnn_R_101_FPN_3x',
                 'faster_rcnn_R_50_C4_1x','faster_rcnn_R_50_C4_3x ',
                 'faster_rcnn_R_50_DC5_1x','faster_rcnn_R_50_DC5_3x',
                 'faster_rcnn_R_50_FPN_1x','faster_rcnn_R_50_FPN_3x',
                 'faster_rcnn_X_101_32x8d_FPN_3x','retinanet_R_101_FPN_3x',
                 'retinanet_R_101_FPN_3x','retinanet_R_50_FPN_1x',
                 'retinanet_R_50_FPN_3x','rpn_R_50_C4_1x','rpn_R_50_FPN_1x'],
        value='faster_rcnn_R_50_FPN_3x',
        description='Model:',
        disabled=False,
    )
    od.observe(on_change)
    return od

def get_xavier_iseg_widget():
    iseg = widgets.Dropdown(
        options=['mask_rcnn_R_101_C4_3x','mask_rcnn_R_101_DC5_3x',
                 'mask_rcnn_R_101_FPN_3x','mask_rcnn_R_50_C4_1x',
                 'mask_rcnn_R_50_C4_3x','mask_rcnn_R_50_DC5_1x ',
                 'mask_rcnn_R_50_DC5_3x','mask_rcnn_R_50_FPN_1x',
                 'mask_rcnn_R_50_FPN_3x','mask_rcnn_X_101_32x8d_FPN_3x'],
        value='mask_rcnn_R_50_FPN_3x',
        description='Model:',
        disabled=False,
    )
    iseg.observe(on_change)
    return iseg

def get_xavier_pkd_widget():
    pkd = widgets.Dropdown(
        options=['keypoint_rcnn_R_101_FPN_3x', 'keypoint_rcnn_R_50_FPN_1x',
                 'keypoint_rcnn_R_50_FPN_3x', 'keypoint_rcnn_X_101_32x8d_FPN_3x'],
        value='keypoint_rcnn_R_50_FPN_3x',
        description='Model:',
        disabled=False,
    )
    pkd.observe(on_change)
    return pkd

def get_xavier_ps_widget():
    ps = widgets.Dropdown(
        options=['panoptic_fpn_R_101_3x', 'panoptic_fpn_R_50_1x',
                 'panoptic_fpn_R_50_3x'],
        value='panoptic_fpn_R_50_3x',
        description='Model:',
        disabled=False,
    )
    ps.observe(on_change)
    return ps

def on_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        print("changed to %s" % change['new'])
    
def test():
    iseg = get_xavier_iseg_widget()
    iseg.observe(on_change)
    return display(iseg)