dataset_paths = {
	'celeba_train': './data_train',
	'celeba_test': './data_test',
	'celeba_train_sketch': '',
	'celeba_test_sketch': '',
	'celeba_train_segmentation': '',
	'celeba_test_segmentation': '',
	'ffhq': '/kaggle/input/zhoudualstylegan-encode/data/head2/images/train',
}

model_paths = {
	'stylegan_ffhq': '/kaggle/input/zhoudualstylegan-encode/checkpoint/stylegan2-ffhq-config-f.pt',
	'ir_se50': '/kaggle/input/zhoudualstylegan-encode/checkpoint/model_ir_se50.pth',
	'circular_face': '/kaggle/input/zhoudualstylegan-encode/checkpoint/CurricularFace_Backbone.pth',
	'mtcnn_pnet': '/kaggle/input/zhoudualstylegan-encode/checkpoint/mtcnn/pnet.npy',
	'mtcnn_rnet': '/kaggle/input/zhoudualstylegan-encode/checkpoint/mtcnn/rnet.npy',
	'mtcnn_onet': '/kaggle/input/zhoudualstylegan-encode/checkpoint/mtcnn/onet.npy',
	'shape_predictor': 'shape_predictor_68_face_landmarks.dat',
	'moco': '/kaggle/input/zhoudualstylegan-encode/checkpoint/moco_v2_800ep_pretrain.pth.tar'
}