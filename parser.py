import argparse
from pytorch_lightning import Trainer
from config import data_config, train_config


def get_args():
    parser = argparse.ArgumentParser(
        'Meta-DRN: Meta-Learning for 1-Shot Image Segmentation')
    parser = Trainer.add_argparse_args(parser)
    parser.add_argument('--algo', type=str, default='maml',
                        help='A meta learning algorithms to use out of maml,\
                        fomal, meta-sgd and reptile')
    parser.add_argument('--folder', type=str, default=data_config['data_root'],
                        help='Path to the folder the data is downloaded to.')
    parser.add_argument('--n_epochs', type=int,
                        default=train_config['n_epochs'],
                        help='Number of epochs to train the meta learner')
    parser.add_argument('--num-workers', type=int,
                        default=data_config['num_workers'],
                        help='Number of workers for data loading\
                                 (default: 1).')
    parser.add_argument('--batch_size', type=int,
                        default=data_config['batch_size'],
                        help='Number of tasks in a mini-batch of tasks\
                        (default: 16).')
    parser.add_argument('--output-folder', type=str, default=None,
                        help='Path to the output folder for saving\
                                 the model (optional).')
    parser.add_argument('--mode', type=str, default='train',
                        help='Whether the network is used\
                        for training or testing.')

    args = parser.parse_args()
    return args
