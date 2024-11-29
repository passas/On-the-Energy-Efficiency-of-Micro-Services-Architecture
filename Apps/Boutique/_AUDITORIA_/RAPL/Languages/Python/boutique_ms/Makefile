NTIMES=10

export NTIMES

measure:
	sudo modprobe msr
	sudo ../../../RAPL/main "python3 manage.py test app.tests.AuditoriaTestCase.test_auditoria_1" Python test_auditoria_1_ms $(NTIMES)
run:
	python3 manage.py test app.tests.AuditoriaTestCase.test_auditoria_1

mem: 
	{ /usr/bin/time -v python3 manage.py test app.tests.AuditoriaTestCase.test_auditoria_1 > /dev/null; } 2>&1 | grep "Maximum resident" #| sed "s/[^0-9]\+\([0-9]\+\).*/\1/"