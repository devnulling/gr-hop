#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2016 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
import pmt
from gnuradio import gr

class frequency_sweeper(gr.sync_block):
    """
    docstring for block freq_swepper
    """
    def __init__(self, freq1, freq2, freq3): 
        gr.sync_block.__init__(
            self,
            name='freq_swepper',
            in_sig=[],
            out_sig=[]
        )

        self.cur_freq = freq1
        self.start_freq = freq1
        self.stop_freq = freq2
        self.step_freq = freq3

        self.message_port_register_in(pmt.intern('in'))
        self.set_msg_handler(pmt.intern('in'), self.handler)
        self.message_port_register_out(pmt.intern('out'))

    def handler(self, pdu):
        if self.cur_freq > self.stop_freq:
            self.cur_freq = self.start_freq

        self.cur_freq += self.step_freq
        self.message_port_pub(pmt.intern('out'), pmt.cons(pmt.intern("freq"), pmt.to_pmt(self.cur_freq)))
        
    def work(self, input_items, output_items):
        pass