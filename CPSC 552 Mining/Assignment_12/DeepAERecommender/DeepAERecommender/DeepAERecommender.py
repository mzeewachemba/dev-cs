import sys
import Utils
import numpy as np
from AEModel import AutoEncoder
from MSELoss_with_Mask import MSELoss_with_Mask
import torch.optim as optim


def train(model, criterion, optimizer, train_dl, test_dl, num_epochs=50):
    """
    Trains the AutoEncoder model.

    Args:
        model (AutoEncoder): The AutoEncoder model to train.
        criterion (nn.Module): The loss function to use for training.
        optimizer (optim.Optimizer): The optimizer to use for updating weights.
        train_dl (DataLoader): The training data loader.
        test_dl (DataLoader): The testing data loader.
        num_epochs (int, optional): The number of epochs to train for (default: 50).
    """

    for epoch in range(num_epochs):
        train_loss, valid_loss = [], []
        logs = {}
        prefix = ''

        # Training Part
        model.train()
        for i, data in enumerate(train_dl, 0):
            inputs = labels = data
            inputs = inputs.cuda()
            labels = labels.cuda()

            inputs = inputs.float()
            labels = labels.float()

            optimizer.zero_grad()

            # forward + backward + optimize
            outputs = model(inputs)
            outputs = outputs.cuda()
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            # Zero the gradients
            optimizer.zero_grad()
            outputs = model(outputs.detach())
            outputs = outputs.cuda()
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            train_loss.append(loss.item())
            print('MMSE loss ', loss.item())

        for i, data in enumerate(test_dl, 0):
            model.eval()
            inputs = labels = data
            inputs = inputs.cuda()
            labels = labels.cuda()

            inputs = inputs.float()
            labels = labels.float()

            outputs = model(inputs)
            outputs = outputs.cuda()
            loss = criterion(outputs, labels)

            valid_loss.append(loss.item())
            prefix = 'val_'
            print('MMSE loss', loss.item())

        print("---------output----------")
        print(outputs[0])
        print()
        print("Epoch:", epoch + 1, " Training Loss: ", np.mean(train_loss), " Valid Loss:", np.mean(valid_loss))

def main():
    """
    The main function to train the AutoEncoder model.
    """

    # Utils.prepare_train_validation_movielens_step1()  # Uncomment if needed
    # Utils.prepare_traintest_movielens_step2()       # Uncomment if needed

    train_loader, test_loader = Utils.get_traintestloaders()

    layer_sizes = [9559, 512, 512, 1024]
    model = AutoEncoder(layer_sizes=layer_sizes, nl_type='selu', is_constrained=True, dp_drop_prob=0.0, last_layer_activations=False)
    model = model.cuda()

    criterion = MSELoss_with_Mask()
    criterion = criterion.cuda()

    optimizer = optim.Adam(model.parameters(), lr=0.001)

    out = train(model, criterion, optimizer, train_loader, test_loader, 40)

if __name__ == "__main__":
    sys.exit(int(main() or 0))
