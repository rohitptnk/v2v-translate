from transformers import BarkModel, AutoProcessor
import torch
import scipy 

def text_to_speech(text, voice_preset="v2/hi_speaker_2"):
    """
    Convert text to speech using Bark model

    Args:
        text (str): Text to convert to speech
        voice_preset (str): Voice preset to use for the speech synthesis

    Returns:
        torch.Tensor: Generated speech audio
        sampling_rate (int): Sampling rate of the generated audio
    """
    # Check if CUDA is available and set device accordingly
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    
    # Load the model and processor
    model = BarkModel.from_pretrained("suno/bark-small")
    processor = AutoProcessor.from_pretrained("suno/bark")

    # Move model and inputs to the appropriate device
    model = model.to(device)
    inputs = processor(text=text, voice_preset=voice_preset)
    for key, value in inputs.items():
        inputs[key] = value.to(device)
    
    # prepare the inputs
    inputs = processor(text, voice_preset=voice_preset)
    for key, value in inputs.items():
        inputs[key] = inputs[key].to(device)

    # generate speech
    speech_output = model.generate(**inputs)
    sampling_rate = model.generation_config.sample_rate
    path = "output_audio.wav"

    # Save the generated audio to a fileimport scipy
    scipy.io.wavfile.write("output_audio.wav", rate=sampling_rate, data=speech_output[0].cpu().numpy())

    return path 
