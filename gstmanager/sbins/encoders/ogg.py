#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gstmanager.sbins.encoder import VideoEncoder, AudioEncoder
from gstmanager.sbins.muxer import Muxer

class TheoraEncoder(VideoEncoder):
    def __init__(self, profile):
        self.description = "Theora encoder"
        self.type = "video"
        sbin = "theoraenc bitrate=%s" %profile.video_bitrate
        VideoEncoder.__init__(self, sbin, profile=profile)

class VorbisEncoder(AudioEncoder):
    def __init__(self, profile):
        self.description = "Vorbis encoder"
        self.type = "audio"
        sbin = "vorbisenc bitrate=%s" %profile.audio_bitrate
        AudioEncoder.__init__(self, sbin)

class OggMuxer(Muxer):
    def __init__(self):
        self.description = "Ogg Muxer"
        self.type = "audio/video"
        sbin = "oggmux"
        Muxer.__init__(self, sbin)

from gstmanager.sbinmanager import SBinManager
from gstmanager.profile import DefaultEncodingProfile

class OggEncoder(SBinManager):
    def __init__(self, filename="/tmp/test.ogg",profile=DefaultEncodingProfile()):
        SBinManager.__init__(self)
        self.check_for_compat = False
        self.venc = TheoraEncoder(profile)
        self.aenc = VorbisEncoder(profile)
        self.muxer = OggMuxer()
        self.add(self.venc)
        self.add(self.aenc)
        self.add(self.muxer)
        self.tags = ["a_src", "v_src"]
        self.type = "audio-video"
        self.description = "Ogg to File Encoder"
        self.filename = filename
        self.sbin = "%s muxer_tee. ! filesink location=%s" %(self.pipeline_desc, filename)

    def get_file(self):
        return self.filename
