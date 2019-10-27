reinit

** Surface pressure **
t = 15
'open /work/hbarbosa/ERA_Interim_Full/sp_mmeans/mmeans_sp.ctl'
'set mpdset brmap_hires'
'set map 1 1 6'
'set lat -50 10'
'set lon -90 -30'
'set t 't
'set gxout contour'
'set gxout shaded'
'd sp'
'cbarn'
'draw title Pressure and moisture flux'
'close 1'

** Moisture flux **
'open /work/hbarbosa/ERA_Interim_Full/qv_mmeans/mmeans_qv.ctl'
'set lat -50 10'
'set lon -90 -30'
'set t 't
'd qu; skip(qv, 3)'
