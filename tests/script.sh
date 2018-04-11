rm -rf report result.jtl
jmeter -n  -t Sample.jmx -l result_200.jtl -e -o report_200
open report/index.html
