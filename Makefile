.PHONY: rpm download-sources


download-sources: SOURCES/qm-dsp-1.7.1.tar.gz

rpm: SRPMS/qm-dsp-1.7.1-1.el6.src.rpm
	mkdir -p RPMS
	rpmbuild --define "_topdir `pwd`" --rebuild $<

SRPMS/qm-dsp-1.7.1-1.el6.src.rpm: SPECS/qm-dsp.spec SOURCES/qm-dsp-1.7.1.tar.gz
	mkdir -p SRPMS
	rpmbuild -bs --define "_topdir `pwd`" SPECS/qm-dsp.spec

SOURCES/qm-dsp-1.7.1.tar.gz:
	mkdir -p SOURCES
	curl -o SOURCES/qm-dsp-1.7.1.tar.gz https://code.soundsoftware.ac.uk/attachments/download/1582/qm-dsp-1.7.1.tar.gz

clean:
	rm -Rf SOURCES/* RPMS/* SRPMS/*
