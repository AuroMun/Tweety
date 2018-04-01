rm -rf report result.jtl
jmeter -n  -t Sample.jmx -l result.jtl -e -o report
open report/index.html
