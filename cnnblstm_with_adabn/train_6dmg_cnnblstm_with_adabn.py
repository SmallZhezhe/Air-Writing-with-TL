import torch
# local class
import sys
sys.path.append("..")
import tools_6dmg
from cnnblstm_with_adabn import cnnblstm_with_adabn

enable_CORAL = True
TRAIN_PATH = r"../dataset/train_6dmg"
TEST_PATH = r"../dataset/test_6dmg"

if __name__ == '__main__':
	torch.manual_seed(2)

	# whether use cuda
	use_cuda = torch.cuda.is_available()
	if use_cuda:
		m_cnnblstm_with_adabn = cnnblstm_with_adabn(use_cuda = 1, params_dir = "./params_6dmg", enable_CORAL = enable_CORAL).cuda()
	else:
		m_cnnblstm_with_adabn = cnnblstm_with_adabn(use_cuda = 0, params_dir = "./params_6dmg", enable_CORAL = enable_CORAL)
	print(m_cnnblstm_with_adabn)
	# get train_x, train_y
	X_all, y_all = tools_6dmg.preprocess(TRAIN_PATH)
	train_x = torch.from_numpy(X_all)
	train_y = torch.from_numpy(y_all)
	# get test_x, test_y
	X_all, y_all = tools_6dmg.preprocess(TEST_PATH)
	test_x = torch.from_numpy(X_all)
	test_y = torch.from_numpy(y_all)
	# trainAllLayers
	m_cnnblstm_with_adabn.trainAllLayers(train_x, train_y, test_x)
	# get test accuracy
	m_cnnblstm_with_adabn.getTestAccuracy(test_x, test_y)
