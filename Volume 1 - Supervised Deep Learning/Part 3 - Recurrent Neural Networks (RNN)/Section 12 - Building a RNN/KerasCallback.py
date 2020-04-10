from keras.callbacks import Callback
import slack


slack_token = "xoxb-2627103541-985741901650-FBjpF8aQ95TWNLGnb4CssCVA"

def Send_Notification(msg_string):
    client = slack.WebClient(token=slack_token)
    client.chat_postMessage(
        channel="GTTPAJB7E",
        text = msg_string
    )


class Notify(Callback):
    def on_train_begin(self, logs={}):
        self.epoch = 0

    def on_epoch_end(self, epoch, logs={}):
        accuracy = logs.get('accuracy')
        loss = logs.get('loss')
        # val_loss = logs.get('val_loss')
        # val_acc = logs.get('val_acc')
        message = "Epoch: " + str(self.epoch) + " Loss: " + \
        str(loss)[0:5] + " Accuracy: " + str(accuracy)[0:5]
        Send_Notification(message)
        self.epoch += 1
