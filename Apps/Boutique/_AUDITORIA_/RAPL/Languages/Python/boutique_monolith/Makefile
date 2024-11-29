NTIMES=10

export NTIMES

measure:
	sudo modprobe msr
	sudo ../../../RAPL/main "python3 manage.py auditoria" Python test_auditoria_1_monolith $(NTIMES)
run:
	python3 manage.py auditoria

mem: 
	{ /usr/bin/time -v python3 manage.py auditoria > /dev/null; } 2>&1 | grep "Maximum resident" #| sed "s/[^0-9]\+\([0-9]\+\).*/\1/"