#!/usr/bin/env python3

import telemetri_verileri as tv

def calistir():
	# pil gerilimi burada olculecek
	tv.pil_gerilim -= tv.min_gerilim
	tv.pil_yuzde = (tv.pil_gerilim / tv.gerilim_araligi) * 100
