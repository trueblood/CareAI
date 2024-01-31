import torch

class DeviceHelper():
    def get_device():
        # Check whether GPU is available and use it if yes.
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        device = torch.device("cpu")
        print(f"Using device: {device}")
        return device