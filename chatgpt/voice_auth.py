#! /home/sougato97/miniconda3/envs/hri/bin/python
# -*- encoding: UTF-8 -*-

from pyannote.audio import Model
from pyannote.audio import Inference
import os
from scipy.spatial.distance import cdist
import numpy as np
import torch

def user_auth(voice_clip_path, name,pyannote_key):
  
  pyannote_model = Model.from_pretrained("pyannote/embedding", use_auth_token = pyannote_key)
  # voice_clip_path = "/home/sougato97/Human_Robot_Interaction/nao_dev/recordings/"
  # Define device to be used (GPU or CPU)
  Device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
  inference = Inference(pyannote_model, window="whole", device = Device)

  ref = inference(voice_clip_path + "recording_sougato_1.mp3")
  recording = inference(voice_clip_path + name)

  # Convert these 1d Numpy to 2d numpy array 
  unsqueezed_ref = np.expand_dims(ref, axis=0)
  unsqueezed_rec = np.expand_dims(recording, axis=0)

  # Compute the distance
  distance1 = cdist(unsqueezed_ref, unsqueezed_rec, metric="cosine")[0,0]

  if (distance1 < 0.50):
    return True
  else:
    False 