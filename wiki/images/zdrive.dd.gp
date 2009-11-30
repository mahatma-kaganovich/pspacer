set terminal postscript enhanced monochrome
set terminal png
set output "zdrive.dd.png"
set size 0.7,0.7
set key right top
#set key box
#set title "filter performance test"
set xlabel "bs size (byte)"
set ylabel "Bandwidth (MB/s)"
#set xrange [1:4096]
#set xrange [1:15000]
set yrange [1:600]
#set ytics 200
set logscale x
#set ytics nomirror
plot \
"zdrive.dd.log" usi 1:2 axis x1y1 ti "seq. write" w l lw 2, \
"zdrive.dd.log" usi 1:3 axis x1y1 ti "seq. read" w l lw 2


