#!/bin/bash
declare -A hosts_names
hosts_names=( ['devops']='10.1.2.16' )

for host in ${!hosts_names[@]}
do
	`ssh $host@${hosts_names[${host}]}` '~/Desktop/git/bash/ws_vmware/ex11_monitor_vm.sh'
done
