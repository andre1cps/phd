reinit

variable = 'Z'
'open /work/hbarbosa/ERA_Interim_Full/invariant.ctl'
'set map 1 1 6'
'set mpdset mres'
'set lat -50 10'
'set lon -90 -30'
'set gxout contour'
'set gxout shaded'
'd ' variable
'cbarn'
'draw title ' variable
