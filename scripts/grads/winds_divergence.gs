* Levels in hPa (37):
* 1000 975 950 925 900 875 850 825 800 775 
*  750 700 650 600 550 500 450 400 350 300 
*  250 225 200 175 150 125 100  70  50  30 
*   20  10   7   5   3   2   1

reinit

'open /work/hbarbosa/ERA_Interim_Full/u_mmeans/mmeans_u.ctl'
'open /work/hbarbosa/ERA_Interim_Full/v_mmeans/mmeans_v.ctl'
'set map 1 1 6'
'set mpdset mres'
'set lat -50 10'
'set lon -90 -30'
'set t 3'
'set z 7'
'set gxout contour'
'set gxout shaded'
'd hdivg(u, v.2)'
'cbarn'
'd u; skip(v.2, 3)'
'draw title Divergence of winds'
