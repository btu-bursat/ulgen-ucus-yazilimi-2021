#!/usr/bin/env python3

import telemetri_verileri as tv

def calistir():
	# pil gerilimi burada olculecek
	tv.pil_gerilimi -= tv.min_gerilim
	tv.pil_yuzde = (tv.pil_gerilimi / tv.gerilim_araligi) * 100
