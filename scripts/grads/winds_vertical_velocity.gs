* Levels in hPa (37):
* 1000 975 950 925 900 875 850 825 800 775 
*  750 700 650 600 550 500 450 400 350 300 
*  250 225 200 175 150 125 100  70  50  30 
*   20  10   7   5   3   2   1

reinit

'open /work/hbarbosa/ERA_Interim_Full/w_mmeans/mmeans_w.ctl'
'set map 1 1 6'
'set mpdset mres'
'set lat -50 10'
'set lon -90 -30'
'set t 12'
z = 12
'set z ' z
'set gxout contour'
'set gxout shaded'
'd w'
'cbarn'
'draw title Vertical velocity \ z=' z
