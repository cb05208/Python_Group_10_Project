from os import path
from pydub import AudioSegment
import os

class AudioHandler:
    def __init__(self, file_full):
        """
        Attempts to import audio using name & extension of file.
        MAKE SURE FILE IS WITHIN THE AUDIO_HOLDER directory.
        If import fails, sets the sound to an empty audio segment.
        """

        self._sound_name = path.splitext(file_full)[0]
        self._message = 'Lorem Ipsum'

        try:
            self._sound = (
                AudioSegment.from_file(
                    path.join('Audio_File_Holder', file_full)
                )
            )
            self.set_message('Audio successfully imported!')
        except:
            self._sound = AudioSegment.empty()
            self.set_message('Audio failed to import!')

    # Mutators & Accessors
    def set_sound_name(self, sound_name):
        """
        Changes the name of the audio segment.
        Do not specify filetype.
        """
        self._sound_name = sound_name

    def get_sound_name(self):
        return self._sound_name

    def set_message(self, message):
        self._message = message

    def get_message(self):
        return self._message

    @staticmethod
    def audio_file_holder_path():
        # Returns the proper filepath for Audio_File_Holder directory
        cwd = os.getcwd()
        return path.join(cwd, "Audio_File_Holder")

    # Member methods
    def export_sound_as_wav(self):
        """
        Exports sound as a .wav file within the Audio_Holder directory,
        using the name of the sound as the file name
        """
        if self._sound == AudioSegment.empty():
            self.set_message(
                'Can\'t export audio file, ' +
                'as the audio segment is empty!'
            )
        else:
            self._sound.export(
                out_f = path.join('Audio_File_Holder', self.get_sound_name() + '.wav'),
                format = 'wav')
            output_dir = self.audio_file_holder_path()
            output_path = path.join(output_dir, self.get_sound_name() + ".wav")
            return output_path

#test
audio = AudioHandler('ProjectClap.m4a')
audio.set_sound_name('Converted_Clap')
audio.export_sound_as_wav()