#!/bin/sh
        #filter all vm ids, remove line 1
all_vms=`vim-cmd vmsvc/getallvms | sed '1d' | awk '{print $1}'`
for vmid in $all_vms
do
        curr_state=`vim-cmd vmsvc/power.getstate ${vmid} | grep "off"`
        if [ "$curr_state" = "Powered off" ]
        then
                # poweron vm and redirect the message
                vim-cmd vmsvc/power.on ${vmid} > /dev/null
        fi
done
