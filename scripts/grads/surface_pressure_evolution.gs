reinit

'open /work/hbarbosa/ERA_Interim_Full/sp_mmeans/mmeans_sp.ctl'
'set map 1 1 6'
'set mpdset mres'
'set dbuff on'
'set gxout contour'
'set gxout shaded'
'set lat -50 10'
'set lon -90 -30'
t = 1
while (t <= 414)
  'set t 't
  'draw title Pressure monthly mean \ month=' t
  'd sp'  
  'cbarn'
  'swap'
  t = t + 1
endwhile
