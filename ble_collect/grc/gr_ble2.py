#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Bluetooth LE Receiver
# Author: Jan Wagner
# Generated: Tue Sep  4 16:30:08 2018
##################################################

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import time


class gr_ble2(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Bluetooth LE Receiver")

        ##################################################
        # Variables
        ##################################################
        self.transition_width = transition_width = 300e3
        self.sample_rate = sample_rate = 4e6
        self.data_rate = data_rate = 1e6
        self.cutoff_freq = cutoff_freq = 500e3
        self.ble_channel_spacing = ble_channel_spacing = 2e6
        self.ble_channel = ble_channel = 12
        self.ble_base_freq = ble_base_freq = 2402e6
        self.squelch_threshold = squelch_threshold = -96
        self.sensivity = sensivity = 1.0
        self.rf_gain = rf_gain = 74
        self.lowpass_filter = lowpass_filter = firdes.low_pass(1, sample_rate, cutoff_freq, transition_width, firdes.WIN_HAMMING, 6.76)
        self.gfsk_sps = gfsk_sps = int(sample_rate / data_rate)
        self.gfsk_omega_limit = gfsk_omega_limit = 0.005
        self.gfsk_mu = gfsk_mu = 0.5
        self.gfsk_gain_mu = gfsk_gain_mu = 0.175
        self.freq_offset = freq_offset = 0
        self.freq = freq = ble_base_freq+(ble_channel_spacing * ble_channel)
        self.filter_center_freq = filter_center_freq = 0
        self.filename = filename = "filename"

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(sample_rate)
        self.uhd_usrp_source_0.set_center_freq(freq, 0)
        self.uhd_usrp_source_0.set_gain(rf_gain, 0)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(1, (lowpass_filter), filter_center_freq, sample_rate)
        self.digital_gfsk_demod_0 = digital.gfsk_demod(
        	samples_per_symbol=gfsk_sps,
        	sensitivity=sensivity,
        	gain_mu=gfsk_gain_mu,
        	mu=gfsk_mu,
        	omega_relative_limit=gfsk_omega_limit,
        	freq_error=0.0,
        	verbose=False,
        	log=False,
        )
        self.blocks_unpacked_to_packed_xx_0 = blocks.unpacked_to_packed_bb(1, gr.GR_LSB_FIRST)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, filename, False)
        self.blocks_file_sink_0.set_unbuffered(False)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_unpacked_to_packed_xx_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.digital_gfsk_demod_0, 0), (self.blocks_unpacked_to_packed_xx_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.digital_gfsk_demod_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))

    def get_transition_width(self):
        return self.transition_width

    def set_transition_width(self, transition_width):
        self.transition_width = transition_width
        self.set_lowpass_filter(firdes.low_pass(1, self.sample_rate, self.cutoff_freq, self.transition_width, firdes.WIN_HAMMING, 6.76))

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate
        self.set_lowpass_filter(firdes.low_pass(1, self.sample_rate, self.cutoff_freq, self.transition_width, firdes.WIN_HAMMING, 6.76))
        self.set_gfsk_sps(int(self.sample_rate / self.data_rate))
        self.uhd_usrp_source_0.set_samp_rate(self.sample_rate)

    def get_data_rate(self):
        return self.data_rate

    def set_data_rate(self, data_rate):
        self.data_rate = data_rate
        self.set_gfsk_sps(int(self.sample_rate / self.data_rate))

    def get_cutoff_freq(self):
        return self.cutoff_freq

    def set_cutoff_freq(self, cutoff_freq):
        self.cutoff_freq = cutoff_freq
        self.set_lowpass_filter(firdes.low_pass(1, self.sample_rate, self.cutoff_freq, self.transition_width, firdes.WIN_HAMMING, 6.76))

    def get_ble_channel_spacing(self):
        return self.ble_channel_spacing

    def set_ble_channel_spacing(self, ble_channel_spacing):
        self.ble_channel_spacing = ble_channel_spacing
        self.set_freq(self.ble_base_freq+(self.ble_channel_spacing * self.ble_channel))

    def get_ble_channel(self):
        return self.ble_channel

    def set_ble_channel(self, ble_channel):
        self.ble_channel = ble_channel
        self.set_freq(self.ble_base_freq+(self.ble_channel_spacing * self.ble_channel))

    def get_ble_base_freq(self):
        return self.ble_base_freq

    def set_ble_base_freq(self, ble_base_freq):
        self.ble_base_freq = ble_base_freq
        self.set_freq(self.ble_base_freq+(self.ble_channel_spacing * self.ble_channel))

    def get_squelch_threshold(self):
        return self.squelch_threshold

    def set_squelch_threshold(self, squelch_threshold):
        self.squelch_threshold = squelch_threshold

    def get_sensivity(self):
        return self.sensivity

    def set_sensivity(self, sensivity):
        self.sensivity = sensivity

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        self.uhd_usrp_source_0.set_gain(self.rf_gain, 0)


    def get_lowpass_filter(self):
        return self.lowpass_filter

    def set_lowpass_filter(self, lowpass_filter):
        self.lowpass_filter = lowpass_filter
        self.freq_xlating_fir_filter_xxx_0.set_taps((self.lowpass_filter))

    def get_gfsk_sps(self):
        return self.gfsk_sps

    def set_gfsk_sps(self, gfsk_sps):
        self.gfsk_sps = gfsk_sps

    def get_gfsk_omega_limit(self):
        return self.gfsk_omega_limit

    def set_gfsk_omega_limit(self, gfsk_omega_limit):
        self.gfsk_omega_limit = gfsk_omega_limit

    def get_gfsk_mu(self):
        return self.gfsk_mu

    def set_gfsk_mu(self, gfsk_mu):
        self.gfsk_mu = gfsk_mu

    def get_gfsk_gain_mu(self):
        return self.gfsk_gain_mu

    def set_gfsk_gain_mu(self, gfsk_gain_mu):
        self.gfsk_gain_mu = gfsk_gain_mu

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.uhd_usrp_source_0.set_center_freq(self.freq, 0)

    def get_filter_center_freq(self):
        return self.filter_center_freq

    def set_filter_center_freq(self, filter_center_freq):
        self.filter_center_freq = filter_center_freq
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.filter_center_freq)

    def get_filename(self):
        return self.filename

    def set_filename(self, filename):
        self.filename = filename
        self.blocks_file_sink_0.open(self.filename)


def main(top_block_cls=gr_ble2, options=None):

    tb = top_block_cls()
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
