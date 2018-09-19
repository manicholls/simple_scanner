#!/bin/bash
echo "Content-type: text/html"
echo ""
echo "<html><head><title>HP Scan tool"
echo "</title></head><body>"

today=`date +%Y-%m-%d.%H:%M:%S`
filename="hp-scan-$today.pdf"
cd /var/www/html/scans/
if [[ $(echo "$QUERY_STRING" | grep -i true ) ]]
then
	hp-scan --dest pdf --adf > /dev/null 2>&1
else
	hp-scan --dest pdf > /dev/null 2>&1
fi
mv /var/www/html/cgi-bin/hpscan001.pdf /var/www/html/scans/$filename
echo "<br><b>Scan completed</b>"
echo "<br>Find your scan here: <a href=http://192.168.10.21/scans/>http://192.168.10.21/scans</a>"
echo "<br><a href=http://192.168.10.21>Scan again</a>"
echo "</body></html>"
exit 0
