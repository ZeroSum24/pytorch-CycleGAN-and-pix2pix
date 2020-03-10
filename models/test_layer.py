
from networks import RelationalLayer
import torch

# output_nc, batch_size=batch_size, gpu_ids=gpu_ids


def test_with_tensor(b, oc, oh, ow):

    model = RelationalLayer(None, batch_size=2, gpu_ids=[-1])

    x = torch.randn(b, oc, oh, ow)
    model.forward(x)
    print('FUCK YEAH')


if __name__ == "__main__":

    # test_with_tensor(b=2, oc=98, oh=20, ow=20)
    test_with_tensor(b=2, oc=64, oh=20, ow=20)
